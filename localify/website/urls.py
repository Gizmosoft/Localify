from django.urls import path,include
from . import views

urlpatterns = [
    # path('', HomePageView.as_view() , name='test'),
    path('', views.home_page, name='home_page'),
    path('login/', views.login_page, name='login_page'),
    path('', include('accounts.urls')),
    path('profile/', views.user_profile, name='user_profile')
]
