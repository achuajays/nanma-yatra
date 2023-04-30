from django.shortcuts import render , redirect
from .models import s ,  dser , a , log  , Review
from django.core.mail import send_mail

from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout
from .forms import logf , ReviewForm 
import datetime
from django.utils import timezone

# Create your views here.



def home(request):
    user = request.session.get('user')
    form = a.objects.filter(c_n=user).first() if user else None
    return render(request , 'app/home.html', {'form': form, 'user': user})


def bas(request):
    if request.method == 'POST':
        
        n = request.session['user']
        e= request.POST['e']
        p = request.POST['p']
        pl = request.POST['pl']
        dc = request.POST['dc']
        dt = request.POST['dt']
        print(n)
        s(name = n , email = e , phno = p , po = pl , do = dc , dt = dt ).save()
        return redirect (home)

    return render(request , 'app/bas.html',{})


def b(request):
    form = s.objects.all()
    
    bas = request.session['bas']
    return render (request , 'app/d.html',{'bas':bas,'form':form})

def aa(request , id, name):
    form = s.objects.get(id = id)
    
    # Create a datetime object for the specific time
    
     # year, month, day, hour, minute, second
    current_time = datetime.datetime.now()

    # Add 30 minutes to the specific time using timedelta
    new_time = current_time + datetime.timedelta(minutes=30)

    # Print the new time
    print(new_time)

    
    c_time = datetime.datetime.now()
    l = form.dt
    if(l == "normal"):
        p = 20 * 5
    elif(l == "women"):
        p = 20 * 10 
    else:
        p = 20 * 100 
    # Define the time threshold
    threshold_time = c_time - timezone.timedelta(hours=1)  # for example, delete items older than 1 hour

    # Delete items with time lower than the threshold time
    time = a.objects.filter(t__lt=threshold_time)
    time.delete()

    l = dser.objects.get(name = name ) 
    subject = "vechicle"
    message = f"your vechicle is now avilable with driver name  =  { l.name } \nvechicle number = { l.v_no }\nphone number = { l.phno }\nprice = { p }"
    recipient_list = [ form.email ]
    a( d_n = l.name , c_n = form.name , t = current_time , price = p   ).save()
    send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list, fail_silently=False)
    form.delete()
    return redirect (home)



def login(request):
    
    if(request.method == "POST" ):
        form = logf(request.POST)
        if (form.is_valid()):

            u=form.cleaned_data['user']
            request.session['user'] = u
            p=form.cleaned_data['password']
            a = log.objects.filter(user = u ,  password = p).first()
            if (a is not None):
                return redirect(home)
            else:
                return render (request , 'app/login.html' , {'form':form,'key':"not identified "})
    form = logf()         

    

                
    

    return render (request , 'app/login.html' , {'form':form,'key':""})


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'app/register.html', {'form': form})



def driverlogin(request):
    if request.method == 'POST':
        
        n = request.POST['name']
        e= request.POST['email']
        p = request.POST['v']
        pl = request.POST['ph']
        print(n)
        request.session['bas'] = n 
        dser(name = n , email = e , v_no = p , phno = pl).save()
        return redirect (b)
    return render (request , 'app/driverlogin.html',{})


def logout_view(request):
    logout(request)
    return redirect(login)





# from .models import MyModel

# def my_view(request):
#     my_model = MyModel.objects.get(pk=1)
#     context = {
#         'map_location': my_model.location,
#     }
#     return render(request, 'app/my.html', cont

import datetime 
import requests
from datetime import date
from django.http import JsonResponse

def get_holidays(request):
    url = "https://www.checkiday.com/api/3/?d=" + date.today().strftime('%m/%d/%Y') + "&k=Kma6qQRZRosMTPziVGOgsdWQrfzY0AFC"
    response = requests.get(url)
    data = response.json()
    return render (request , 'app/holiday.html',{'data':data})
    



def submit_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reviews')
    else:
        form = ReviewForm()
    return render(request, 'app/submit_review.html', {'form': form})

def view_reviews(request):
    reviews = Review.objects.all()
    return render(request, 'app/view_reviews.html', {'reviews': reviews})


def c(request):
    return render (request , 'app/c.html',{})


from django.shortcuts import render
from .models import Location

def map_view(request):
    
    return render(request, 'app/map.html')