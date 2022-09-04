from django.contrib import admin
from blog_app.models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display=['title', 'featured']


admin.site.register(Article, ArticleAdmin)
