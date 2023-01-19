from django.urls import path
from . import views

urlpatterns = [
 path('', views.NewCreateView.as_view(), name='reg'),
 path('login', views.logins, name='login')
]