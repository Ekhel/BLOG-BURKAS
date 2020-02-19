from django.contrib import admin
from .models import Article

class PageArticle(admin.ModelAdmin):
    list_display = ('id_article','title','video','date_created')
    list_display_links = ('id_article','title','video','date_created')
    search_fields = ('id_article','title','video','date_created')
    list_per_page = 10
    prepopulated_fields = {'slug': ('title', )}


admin.site.register(Article,PageArticle)
