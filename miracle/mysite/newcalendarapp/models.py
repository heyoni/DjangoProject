from django.db.models.deletion import CASCADE
from routineapp.models import Routine
from django.db import models
from django.urls import reverse
from colorfield.fields import ColorField

class CalendarModel(models.Model):

    start_time = models.DateField("날짜")
    title = models.ForeignKey(Routine, on_delete=models.CASCADE, related_name='title1')

    def __str__(self):
        return f'{self.title},{self.title.color}'

    @property
    def get_html_url(self):
        color = self.title.color
        url = reverse('calendarapp:edit', args=(self.id,))
        return f'<a href="{url}" class="cal_color {color}" style="background-color:{color};color:{color};float:left;margin:3px 3px; border-radius: 50%;width:12px;height:12px">  </a>'

# class Event(models.Model):
#     COLOR_CHOICES = [
#         ("#FF0000", "red"),
#         ("#FFA500", "orange"),
#         ("#FFFF00", "yellow"),
#         ("#34A223", "green"),
#         ("#0000FF", "blue"),
#         ("#00498C", "navy"),
#         ("#8B00FF", "red"),
#         ("#000000", "black"),
#         ("#FFFFFF", "white")
#     ]

#     # query = Routine.objects.filter(Routine).values('color')Routine.objects.get('color')
#     start_time = models.DateField("날짜")
#     title = models.ForeignKey(Routine, on_delete=models.CASCADE, related_name='title1')
#     color = ColorField(choices=COLOR_CHOICES)


#     def __str__(self):
#         return str(self.title)

#     @property
#     def get_html_url(self):
#         url = reverse('calendarapp:edit', args=(self.id,))
#         return f'<a href="{url}" class="cal_color {self.color}" style="background-color:{self.color};color:{self.color};float:left;margin:3px 3px; border-radius: 50%;width:12px;height:12px">  </a>'