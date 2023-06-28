from django.shortcuts import render


def Homepage(request):
    return render(request, 'index.html')

def Apartments(request):
    return render(request, 'Apartments/apartments.html')

def Trends(request):
    return render(request, 'Trends/trends.html')

def About(request):
    return render(request, 'About/about.html')

def Profile(request):
    return render(request, 'Profile/profile_page.html')

def Notification(request):
    return render(request, 'Profile/notification.html')

def Bookmarks(request):
    return render(request, 'Profile/bookmarks.html')

def Settings(request):
    return render(request, 'Profile/settings.html')

def Logout(request):
    return render(request, 'index.html')