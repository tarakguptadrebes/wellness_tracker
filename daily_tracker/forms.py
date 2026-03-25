from django import forms
from .models import DailyEntry

class DailyEntryForm(forms.ModelForm):
    class Meta:
        model = DailyEntry
        fields = ['mood', 'sleep']
        widgets = {
            'mood': forms.HiddenInput(attrs={'id': 'id_mood'}),
            'sleep': forms.NumberInput(attrs={'min': 0, 'max': 24}),
        }