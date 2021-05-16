from django.shortcuts import render

from moviesapp.models import movietable
from moviesapp.forms import movietableForm


# Create your views here.
def home_page(request):
    return render(request=request, template_name='moviesapp/homepage.html')

def add_movie(request):
    movie_form=movietableForm()
    my_dict={'movie_form':movie_form}

    #logic to store the data [POST request] entered by end user within the database
    if request.method =='POST':
        form_data=movietableForm(request.POST)
        if form_data.is_valid():
            form_data.save(commit=True)

     #logic to fetch the data from the Form object and display the data on  Django development server
    if request.method =='POST':
        form_data=movietableForm(request.POST)
        if form_data.is_valid():
            print(f'MOVIE NAME:{form_data.cleaned_data["moviename"]}')
            print(f'HERO:{form_data.cleaned_data["hero"]}')
            print(f'HEROINE:{form_data.cleaned_data["heroine"]}')

           
    return render(request=request, template_name='moviesapp/add.html', context=my_dict)

def movie_list(request):
    movie_data=movietable.objects.all()
    my_dict={'movie_data':movie_data}
    movie_form=movietableForm()
    return render(request=request, template_name='moviesapp/list.html', context=my_dict)
    
    
