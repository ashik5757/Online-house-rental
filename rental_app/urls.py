from django.urls import path
from .import views

urlpatterns = [
    path('', views.Homepage, name='home_page'),
    path('apartments/', views.Apartments, name='apartments'),
    path('trends/', views.Trends, name='trends'),
    path('about/', views.About, name='about'),
    
    path('<str:username>/profile/', views.Profile, name='profile_post'),
    path('<str:username>/about/', views.Profile, name='profile_about'),
    path('<str:username>/photos/', views.Profile, name='profile_photos'),
    path('<str:username>/videos/', views.Profile, name='profile_videos'),

    path('<str:username>/edit-profile/general', views.Edit_Profile, name='edit_profile_general'),
    path('<str:username>/edit-profile/change_user_email', views.Edit_Profile_user_email, name='edit_profile_user_email'),
    path('<str:username>/edit-profile/change_password', views.Edit_Profile_password, name='edit_profile_password'),

    path('notification/', views.Notification, name='notification'),
    path('bookmarks/', views.Bookmarks, name='bookmarks'),
    path('settings/', views.Settings, name='settings'),
    path('logout/', views.LogoutUser, name='log_out'),
    path('sigin/', views.Signin, name='sign_in'),
    path('sigup_base/', views.Signup_base, name='signup_base'),
    path('signup_landlord/', views.SignUp_landlord, name='sign_up_landlord'),
    path('signup_renter/', views.SignUp_renter, name='sign_up_renter')

    

]
