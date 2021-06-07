from django.db.models.deletion import CASCADE
from rutineapp.models import Rutine
from django.db import models
from django.urls import reverse

class Event(models.Model):
    start_time = models.DateTimeField("시작시간")
    title = models.ForeignKey(Rutine, on_delete=models.CASCADE, related_name='title1')
    content = models.ForeignKey(Rutine, on_delete=models.CASCADE, related_name='content1')

    class Meta:
        verbose_name = "이벤트 데이터"
        verbose_name_plural = "이벤트 데이터"

    def __str__(self):
        return self.title

    @property
    def get_html_url(self):
        url = reverse('calendarapp:edit', args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'