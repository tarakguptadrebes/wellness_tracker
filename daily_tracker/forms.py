from django import forms
from .models import DailyEntry

class DailyEntryForm(forms.ModelForm):
    class Meta:
        model = DailyEntry
        fields = ['mood', 'sleep']
        widgets = {
            'mood': forms.NumberInput(attrs={'min': 1, 'max': 10}),
            'sleep': forms.NumberInput(attrs={'min': 0, 'max': 24}),
        }