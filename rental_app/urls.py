from django.urls import path
from .import views

urlpatterns = [
    path('', views.Homepage, name='home_page'),
    path('apartments/', views.Apartments, name='apartments'),
    path('trends/', views.Trends, name='trends'),
    path('about/', views.About, name='about'),
    path('profile/', views.Profile, name='profile'),
    path('notification/', views.Notification, name='notification'),
    path('bookmarks/', views.Bookmarks, name='bookmarks'),
    path('settings/', views.Settings, name='settings'),
    path('', views.Logout, name='log_out'),
    path('signin/', views.Signin, name='sign_in'),
    path('signup/', views.SignUp, name='sign_up')
]
