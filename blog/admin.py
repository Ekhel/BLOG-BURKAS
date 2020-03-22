from django.contrib import admin
from .models import Article, Kategori
from django_summernote.admin import SummernoteModelAdmin

class PageArticle(SummernoteModelAdmin):
    list_display = ('id_article','title','deskripsi','date_created')
    list_display_links = ('id_article','title','deskripsi','date_created')
    search_fields = ('id_article','title','deskripsi','date_created')
    list_per_page = 10
    prepopulated_fields = {'slug': ('title', )}
    summernote_fields = ('body',)


admin.site.register(Article,PageArticle)
admin.site.register(Kategori)
