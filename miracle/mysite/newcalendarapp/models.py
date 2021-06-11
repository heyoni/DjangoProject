from django.db.models.deletion import CASCADE
from rutineapp.models import Rutine
from django.db import models
from django.urls import reverse
from colorfield.fields import ColorField

class Event(models.Model):
    COLOR_CHOICES = [
        ("#FF0000", "red"),
        ("#FFA500", "orange"),
        ("#FFFF00", "yellow"),
        ("#34A223", "green"),
        ("#0000FF", "blue"),
        ("#00498C", "navy"),
        ("#8B00FF", "red"),
        ("#000000", "black")
    ]


    start_time = models.DateTimeField("시작시간")
    title = models.ForeignKey(Rutine, on_delete=models.CASCADE, related_name='title1')
    color = ColorField(choices=COLOR_CHOICES)


    def __str__(self):
        return str(self.title)

    @property
    def get_html_url(self):
        color = 'blue'
        url = reverse('calendarapp:edit', args=(self.id,))
        return f'<a href="{url}" style="background-color:{self.color}"> dd </a>'