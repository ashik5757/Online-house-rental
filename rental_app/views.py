from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User
from .models import *


def Homepage(request):
    return render(request, 'index.html')

@login_required(login_url='sign_in')
def Apartments(request):
    return render(request, 'Apartments/apartments.html')


@login_required(login_url="sign_in")
def Trends(request):
    return render(request, 'Trends/trends.html')

def About(request):
    return render(request, 'About/about.html')

@login_required(login_url="sign_in")
def Profile(request):
    return render(request, 'Profile/profile_page.html')

@login_required(login_url="sign_in")
def Notification(request):
    return render(request, 'Profile/notification.html')

@login_required(login_url="sign_in")
def Bookmarks(request):
    return render(request, 'Profile/bookmarks.html')

@login_required(login_url="sign_in")
def Settings(request):
    return render(request, 'Profile/settings.html')

@login_required(login_url="sign_in")
def LogoutUser(request):
    logout(request)
    messages.warning(request, 'Logged out')
    return redirect('home_page')




# def Signin_hardlink(request):
    
#     if request.user.is_authenticated:
#         return redirect('home_page')

#     if request.method == 'POST':
#     #    username = request.POST['username']
#         username = request.POST.get('username')
#         password = request.POST.get('password')


#         try:
#             user = User.objects.get(username=username)
#             # email = User.objects.get(email=username)  # have to complete
#         except:
#             messages.error(request, 'User not found')

#         user = authenticate(request, username=username, password=password)

#         if user is not None:
#             login(request, user)
#             return redirect('home_page')
#         else:
#             messages.error(request, 'Username or password incorrect')
            
#     return render(request, 'Signin/login_hardlink.html')



def Signin(request):

    if request.user.is_authenticated:
        return redirect('home_page')

    if request.method == 'POST':
    #    username = request.POST['username']
        print(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
            # email = User.objects.get(email=username)  # have to complete
        except:
            # print(Exception)
            messages.error(request, 'User does not exist')
            return redirect('home_page')
        
        user = User.objects.get(username=username)

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Successfully Logged in')
            return redirect('home_page')
        else:
            messages.error(request, 'Username or password incorrect')
            return redirect('home_page')
    
    else:
        return render(request, '404.html')




def Signup_base(request):
    return render('base_signup.html')




def SignUp_landlord(request):

    if request.method == 'POST':

        print(request.POST)

        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        phone = request.POST.get('phone')
        Address = request.POST.get('Address')
        city = request.POST.get('city')

        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        new_user = User.objects.create_user(username=username, email=email, password=password)
        new_user.first_name = first_name
        new_user.last_name = last_name
        new_user.save()

        new_landlord = Landlord.objects.create_Landlord(first_name, last_name, phone, city, new_user)
        new_landlord.save()

        messages.success(request, 'Your account has been successfully created')

        return redirect('home_page')

        # return render(request, 'Signup/signupLandlord1.html')

    else:
        return render(request, '404.html')


def SignUp_renter(request):
    if request.method == 'POST':
        print(request.POST)
        return redirect('home_page')
    
    else:
        return render(request, '404.html')

