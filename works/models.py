from django.db import models


class Sample(models.Model):
    img = models.ImageField(verbose_name='img', blank=True, null=True)


