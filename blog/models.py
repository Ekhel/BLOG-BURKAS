from django.db import models
from django.conf import settings

class Article(models.Model):
    id_article = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150)
    slug = models.SlugField()
    deskripsi = models.CharField(max_length=250)
    body = models.TextField()
    video = models.CharField(max_length=200)
    date_created = models.DateField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

