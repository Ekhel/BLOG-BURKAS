from django.db import models
from django.conf import settings

class Article(models.Model):
    id_article = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150)
    slug = models.SlugField()
    deskripsi = models.CharField(max_length=250)
    body = models.TextField()
    video = models.TextField()
    gambar = models.ImageField(upload_to='article/', default='default.jpg')
    date_created = models.DateField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        ordering = ('id_article',)

    def __str__(self):
        return self.title


class Kategori(models.Model):
    id_kategori = models.AutoField(primary_key=True)
    kategori = models.CharField(max_length=50)
    deskripsi = models.CharField(max_length=200)

    class Meta:
        ordering = ('id_kategori',)

    def __str__(self):
        return self.kategori

