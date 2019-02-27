from django.db import models


class Meme(models.Model):
    upload = models.FileField(upload_to='media/', blank=True)