from django.urls import path
from . import views

urlpatterns = [
    path('', views.daily_entry_view, name='daily-entry'),
]