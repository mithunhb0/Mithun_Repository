from django.contrib import admin
from django.urls import path
from courses import views
from django.conf.urls.static import static
from coursewebsite.settings import MEDIA_ROOT, MEDIA_URL

urlpatterns = [
    #path('', views.home_page, name='home' ),
    path('', views.HomePageView.as_view(), name='home' ),
    
    path('signup/', views.SignupView.as_view(), name='signup' ),
    path('signin/', views.SigninView.as_view(), name='signin' ),
    path('signout/', views.signout_page, name='signout' ),
    
    #path('my-courses/', views.my_courses_page, name='mycourses' ),
    path('my-courses/', views.MyCourseList.as_view(), name='mycourses' ),

    
    path('check-out/<str:slug>/', views.checkout_page, name='checkout' ),
    path('course/<str:slug>/', views.course_page, name='coursepage' ),
    
    path('varify_payment/', views.varifyPayment, name='varifypayment' ),
    
    
]+ static(MEDIA_URL, document_root=MEDIA_ROOT)