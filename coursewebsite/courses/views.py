from django.shortcuts import render, redirect
from django.http import HttpResponse
from courses.models import *
from courses.forms import *
from django.views.generic import View
from django.contrib.auth import logout, login
import razorpay
from coursewebsite.settings import * 
from time import time
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import FormView
from django.views.generic import *
from django.utils.decorators import method_decorator


'''def home_page(request):
    courses = Course.objects.all()
    print(courses)
    my_dict = {'courses':courses}
    return render(request=request, template_name='courses/homepage.html', context=my_dict)'''
    
class HomePageView(ListView):
    template_name = 'courses/homepage.html'
    queryset = Course.objects.filter(active = True)
    context_object_name = 'courses'

def course_page(request, slug):
    course = Course.objects.get(slug=slug)
    serial_number = request.GET.get('lecture')
    videos = course.video_set.all().order_by('serial_number')

    next_lecture = 2
    prev_lecture = None
    if serial_number is None:
        serial_number = 1
    else:
        next_lecture = int(serial_number) + 1
        if len(videos)<next_lecture:
            next_lecture = None
            
        prev_lecture = int(serial_number) - 1
        
    
    video = Video.objects.get(serial_number=serial_number, course=course)

    if video.is_preview==False:
        if request.user.is_authenticated==False:
            return redirect("signin")
        else:
            user = request.user
            try:
                usercourse = UserCourse.objects.get(user=user,course=course)
                error = "You are already enrolled in this course"
            except:
                return redirect("checkout", slug=course.slug) 
        
        
    my_dict = {'course':course, 'video':video, 'videos':videos, 'next_lecture':next_lecture,'prev_lecture':prev_lecture}
    return render(request, 'courses/coursepage.html', context=my_dict)

'''class SignupView(View):
    def get(self, request):
        form = SignupForm()
        context = {'form':form}
        return render(request, 'courses/signup.html',context)
    
    def post(self,request):
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            print(user.email)
            if user is not None:
                return redirect('signin')
        context = {'form':form}
        return render(request, 'courses/signup.html',context)'''

class SignupView(FormView):
    template_name = 'courses/signup.html'
    form_class = SignupForm
    success_url = "/signin/"
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

        
'''class SigninView(View):
    def get(self, request):
        form = SigninForm()
        context = {'form':form}
        return render(request, 'courses/signin.html',context)
    
    def post(self,request):
        form = SigninForm(request=request,data=request.POST)
        if form.is_valid():
             return redirect('/')
         
        context = {'form':form}
        return render(request, 'courses/signin.html',context)'''
        
class SigninView(FormView):
    template_name = 'courses/signin.html'
    form_class = SigninForm
    success_url = "/"
    
    def form_valid(self, form):
        login(self.request, form.cleaned_data)  #session creation
        next_page = self.request.GET.get('next') # next page --> ?next in address bar
        if next_page is not None:
            return redirect(next_page)
        return super().form_valid(form)
        
def signout_page(request):
    logout(request)
    return redirect("home")

client = razorpay.Client(auth=(KEY_ID, KEY_SECRET))

@login_required(login_url="signin")
def checkout_page(request,slug):
    course = Course.objects.get(slug=slug)
    user = request.user
    action = request.GET.get('action')
    order = None
    payment = None
    error = None
    
    try:
        usercourse = UserCourse.objects.get(user=user,course=course)
        error = "You are already enrolled in this course"
    except:
            pass
    amount = None
    if error is None:
        amount =  int((course.price - ( course.price * course.discount * 0.01 )) * 100)
    
    # if amount zero dont make payment, only save enrollment object
    if amount == 0:   #direct enroll
        usercourse = UserCourse(user = user, course=course)
        usercourse.save()
        return  redirect('mycourses')
    
    if action == 'create_payment':
            currency = 'INR'
            notes = {
                "email":user.email,
                "name":f"{user.first_name} {user.last_name} ",
                
            }
            receipt = f"onlinecoursewebsite{int(time())}"
            order = client.order.create({
                "receipt":receipt, 
                "notes":notes, 
                "amount":amount, 
                "currency":currency
                })
            
            payment = Payment()
            payment.user = user
            payment.course = course
            payment.order_id = order.get('id')
            payment.save()
            
    my_dict = {'course':course, 'order':order, 'payment':payment,'user':user,'error':error}
    return render(request, 'courses/checkout.html', context=my_dict)

@login_required(login_url="signin")
@csrf_exempt
def varifyPayment(request):
    if request.method == 'POST':
        data = request.POST
        context = {}
        print(data)
        try:
            client.utility.verify_payment_signature(data)
            razorpay_order_id = data['razorpay_order_id']
            razorpay_payment_id = data['razorpay_payment_id']
            
            payment = Payment.objects.get(order_id=razorpay_order_id)
            payment.payment_id = razorpay_payment_id
            payment.status = True
            
            usercourse = UserCourse(user = payment.user, course=payment.course)
            usercourse.save()
            
            payment.user_course = usercourse
            payment.save()
            
            return redirect('mycourses')
        
        except:
            return HttpResponse("Invalid payment Details")
        
'''@login_required(login_url="signin")       
def my_courses_page(request):
    user = request.user
    try:
        usercourse = UserCourse.objects.filter(user=user)
    except:
        return HttpResponse("You don't have any courses")
    
    context = {'usercourse':usercourse}
    return render(request, 'courses/mycourse.html',context=context)'''
 
@method_decorator(login_required(login_url="signin"), name='dispatch')   
class MyCourseList(ListView):
    template_name = 'courses/mycourse.html'
    context_object_name = 'usercourse'
    
    def get_queryset(self):
        return UserCourse.objects.filter(user=self.request.user)