from django.shortcuts import render
from blog_app.models import Article


def blog_view(request):

    featured_articles = Article.objects.filter(featured=True)
    articles = Article.objects.exclude(featured=True)

    context = {
        'featured_articles': featured_articles,
        'articles': articles,
    }

    return render(request, 'blog_app/index.html', context)
