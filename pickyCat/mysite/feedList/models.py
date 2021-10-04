from django.db import models


class FeedList(models.Model):
    name = models.CharField(verbose_name='사료 이름', max_length=20)
    crude_protein = models.IntegerField(blank=True)
    crude_Fat = models.IntegerField(blank=True)
    phosphorus = models.IntegerField(blank=True)

    LIKE = '좋아!'
    DISLIKE = '그냥 그래..'
    HATE = '싫어!'
    PAL_CHOICE = (
        ('LIKE',LIKE),
        ('DISLIKE',DISLIKE),
        ('HATE',HATE)
    )
    liking = models.CharField(max_length=7, choices=PAL_CHOICE)

    def __str__(self):
        return self.name