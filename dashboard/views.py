import json 
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Avg  
from daily_tracker.models import DailyEntry

# Create your views here.
@login_required
def dashboard_view(request):
    entries = DailyEntry.objects.filter(user=request.user).order_by('date')[:30]
    entries = sorted(entries, key=lambda x: x.date)
    dates = []
    moods = []
    sleeps = []
    for entry in entries:
        dates.append(entry.date.strftime('%d %b'))
        moods.append(entry.mood if entry.mood is not None else 0)
        sleeps.append(entry.sleep if entry.sleep is not None else 0)
    context = {
        'dates': json.dumps(dates),
        'moods': json.dumps(moods),
        'sleeps': json.dumps(sleeps),
    }
    return render(request, 'dashboard/dashboard.html', context)