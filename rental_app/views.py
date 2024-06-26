from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from .models import *
from django.views import View


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
def Profile(request, username):
    
    if request.user.role == 'L':
        profile = Landlord.objects.filter(user=request.user).first()
    if request.user.role == 'R':
        profile = Renter.objects.filter(user=request.user).first()

    return render(request, 'Profile/profile_page.html', {'p' : profile})



@login_required(login_url="sign_in")
def Edit_Profile(request, username):
        
    areaObj = Area.objects.all()
    distObj = District.objects.all()

    if request.user.role == 'L':
        profile = Landlord.objects.filter(user=request.user).first()

    if request.user.role == 'R':
        profile = Renter.objects.filter(user=request.user).first()
    
    if request.method == 'POST':
        
        try:
            profile_image = request.FILES['profile_image']
        except:
            profile_image = None

        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone = request.POST.get('phone')
        occupation = request.POST.get('occupation')
        area = request.POST.get('area')
        district = request.POST.get('district')
        present_address = request.POST.get('present_address')
        permanent_address = request.POST.get('permanent_address')

        if profile_image is not None:
            profile.profile_image = profile_image
        
        profile.first_name = first_name
        profile.last_name = last_name
        profile.phone = phone
        profile.occupation = occupation
        profile.area = area
        profile.district = district
        profile.present_address = present_address
        profile.permanent_address = permanent_address
        
        print(request.POST)
        
        profile.save()
        messages.success(request, 'Profile Uopdated')
        return redirect('profile_post', {'p' : profile})
        
        
    context = {'p' : profile, 'arealist': areaObj, 'distList': distObj}
    return render(request, 'Profile/Edit_profile/edit_profile_general.html', context=context)

@login_required(login_url="sign_in")
def Edit_Profile_user_email(request, username):

        
    if request.user.role == 'L':
        profile = Landlord.objects.filter(user=request.user).first()
    if request.user.role == 'R':
        profile = Renter.objects.filter(user=request.user).first()

    if request.method == 'POST':
        newUsername = request.POST.get('username')
        newEmail = request.POST.get('email')
        password = request.POST.get('password')

        # user = User.objects.filter(username=username).first()

        user = authenticate(username=username, password=password)

        if user is not None :
            user.username = newUsername
            user.email = newEmail

            if User.objects.filter(username=newUsername).exists() and User.objects.filter(username=newUsername).first()!=user:
                messages.error(request, 'Username already used by other user')
            elif User.objects.filter(email=newEmail).exists() and User.objects.filter(email=newEmail).first()!=user:
                messages.error(request, 'Email already used by other user')
            else:
                try:
                    user.save()
                    messages.success(request, 'Information Updated')
                    return redirect('profile_post', {'p' : profile})
                except:
                    messages.error(request, 'Something is wrong')
        else:
            messages.error(request, 'Password is Incorrect')


        print(request.POST)


    context = {'p' : profile}
    return render(request, 'Profile/Edit_profile/edit_profile_user_email.html', context=context)


@login_required(login_url="sign_in")
def Edit_Profile_password(request, username):
        
    if request.user.role == 'L':
        profile = Landlord.objects.filter(user=request.user).first()
    if request.user.role == 'R':
        profile = Renter.objects.filter(user=request.user).first()


    if request.method == 'POST':
        password = request.POST.get('current_password')
        newPassword1 = request.POST.get('new_password')
        newPassword2 = request.POST.get('confirm_password')

        user = authenticate(username=username, password=password)

        if user is not None :

            if newPassword1 == newPassword2:

                try:
                    user.set_password(newPassword1)
                    user.save()
                    update_session_auth_hash(request, user)
                    messages.success(request, 'Information Updated')
                    return redirect('profile_post', {'p' : profile})
                except:
                    messages.error(request, 'Something was wrong')

        else:
            messages.error(request, 'Current Password is wrong')


        print(request.POST)

    return render(request, 'Profile/Edit_profile/edit_profile_password.html', {'p' : profile})









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
        username_email = request.POST.get('username_email')
        password = request.POST.get('password')

        try:
            user = User.objects.filter(username=username_email).first()

            if user is None:
                user = User.objects.filter(email=username_email).first()
            
            username = user.get_username()

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
            messages.error(request, 'Password was incorrect')
            return redirect('home_page')
    
    else:
        return render(request, '404.html')




def Signup_base(request):
    return render('base_signup.html')




def SignUp_landlord(request):

    # if request.method == 'GET':

    #     return render(request, 'Signup/signupLandlord1.html', context=context)

    if request.method == 'POST':

        areaObj = Area.objects.all()

        print(request.POST)

        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        phone = request.POST.get('phone')
        # Address = request.POST.get('Address')
        area = request.POST.get('area')

        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return redirect('home_page')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already used in other account')
            return redirect('home_page')
        
        try:
            new_user = User.objects.create_user(username=username, email=email, password=password, role='L')
            new_landlord = Landlord.objects.create_Landlord(first_name, last_name, phone, area, new_user)
            new_landlord.save()
        except:
            messages.error(request, 'Something went wrong')
            return redirect('home_page')


        messages.success(request, 'Your account has been successfully created')
        messages.success(request, 'You can login NOW!')
        return redirect('home_page')

        # return render(request, 'Signup/signupLandlord1.html')

    else:
        return render(request, '404.html')


def SignUp_renter(request):

    if request.method == 'POST':

        print(request.POST)

        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        phone = request.POST.get('phone')
        area = request.POST.get('area')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return redirect('home_page')
        
        try:
            new_user = User.objects.create_user(username=username, email=email, password=password, role='R')
            new_renter = Renter.objects.create_Renter(first_name, last_name, phone, area, new_user)
            new_renter.save()
        except:
            messages.error(request, 'Something went wrong')
            return redirect('home_page')


        messages.success(request, 'Your account has been successfully created')
        messages.success(request, 'You can login NOW!')
        return redirect('home_page')

        # return render(request, 'Signup/signupLandlord1.html')

    else:
        return render(request, '404.html')

