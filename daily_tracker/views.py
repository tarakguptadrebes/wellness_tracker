from django.shortcuts import render, redirect
from .models import DailyEntry
from .forms import DailyEntryForm
from django.contrib.auth.decorators import login_required
from datetime import date   

# Create your views here.

@login_required
def daily_entry_view(request):
    today = date.today()
    entry, created = DailyEntry.objects.get_or_create(user=request.user, date=today)
    if request.method == 'POST':
        form = DailyEntryForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = DailyEntryForm(instance=entry)
    return render(request, 'daily_tracker/daily_entry.html', {'form': form})
