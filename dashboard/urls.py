from django.urls import path
from . import views
from daily_tracker import views as tracker_views 

urlpatterns = [
    path('', views.dashboard_view, name='dashboard'),
    path('daily-entry/', tracker_views.daily_entry_view, name='daily-entry'),
]