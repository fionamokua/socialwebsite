from django.urls import path
from .views import user_login,dashboard
from django.contrib.auth import views as auth_views
urlpatterns=[
   # path("",user_login,name="login"),
    path('login/',auth_views.LoginView.as_view(),name='login'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    path('passwordchange/',auth_views.PasswordChangeView.as_view(),name='passwordchange'),
    path('passwordchangedone/',auth_views.PasswordChangeDoneView.as_view(),name='passwordchangedone'),
    path('passwordreset/',auth_views.PasswordResetView.as_view(),name='passwordreset'),
    path('passwordresetdone/',auth_views.PasswordResetDoneView.as_view(),name='passwordresetdone'),
    path('passwordresetconfirm/',auth_views.PasswordResetConfirmView.as_view(),name='passwordresetconfirm'),
    path('passwordresetcomplete/',auth_views.PasswordResetCompleteView.as_view(),name='passwordresetcompletecomplete'),
    
    path("",dashboard,name='dashboard')
]
