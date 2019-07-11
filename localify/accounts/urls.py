from django.urls import path
from . import views
# from .views import SignUpView

urlpatterns = [
    # path('signup/', views.SignUpView.as_view() , name='signup'),
    path('register/', views.register_page, name='register_page')

]
