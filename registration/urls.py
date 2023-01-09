from django.urls import path
from . import views

urlpatterns = [
 path('', views.NewCreateView.as_view(), name='reg')
]