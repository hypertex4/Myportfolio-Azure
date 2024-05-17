from django.urls import path
from . import  views

app_name = 'contacts'

urlpatterns = [
    path('new-message/', views.contact, name="new-message"),
]