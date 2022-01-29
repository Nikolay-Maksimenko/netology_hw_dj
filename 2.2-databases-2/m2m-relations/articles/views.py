from django.shortcuts import render

from articles.models import Article


def articles_list(request):
    template = 'articles/news.html'
    object_list = Article.objects.prefetch_related().order_by('-published_at').all()
    context = {'object_list': object_list}

    return render(request, template, context)
