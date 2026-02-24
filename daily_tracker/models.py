from django.db import models

# Create your models here.

class DailyEntry(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    date = models.DateField()
    mood = models.IntegerField(null=True, blank=True)
    sleep = models.IntegerField(null=True, blank=True)

    class Meta:
        unique_together = ('user', 'date')

    def __str__(self):
        return f"{self.user.username} - {self.date}"