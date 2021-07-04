from django.db.models.deletion import CASCADE
from routineapp.models import Routine
from django.db import models
from django.urls import reverse


class CalendarModel(models.Model):
    start_time = models.DateField("날짜")
    title = models.ForeignKey(Routine, on_delete=models.CASCADE, related_name='title1')


    def __str__(self):
        return f'{self.title},{self.title.color},{self.title.time}'

    @property
    def get_html_url(self):
        color = self.title.color
        url = reverse('calendarapp:edit', args=(self.id,))
        return f'<a href="{url}" class="cal_color {color}" style="background-color:{color};color:{color};float:left;margin:3px 3px; border-radius: 50%;width:12px;height:12px">  </a>'
