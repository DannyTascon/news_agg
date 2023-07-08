import feedparser
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.timezone import make_aware
import datetime

from .models import Article, Source

def home(request):
    articles = Article.objects.order_by('-published_date')[:10]
    return render(request, 'home.html', {'articles': articles})

def categories(request):
    categories = ["Local News", "USA Todays News", "International News"]
    return render(request, 'categories.html', {'categories': categories})

def sources(request):
    sources = Source.objects.all()
    return render(request, 'sources.html', {'sources': sources})

def source_articles(request, source_id):
    source = get_object_or_404(Source, pk=source_id)
    articles = source.article_set.order_by('-published_date')[:10]
    return render(request, 'source_articles.html', {'source': source, 'articles': articles})

def fetch_news(request):
    sources = [
        ("Google News", "https://news.google.com/news/rss"),
        ("Huffington Post", "https://www.huffingtonpost.com/section/front-page/feed"),
        ("CNN", "http://rss.cnn.com/rss/edition.rss"),
    ]

    for source_name, source_url in sources:
        feed = feedparser.parse(source_url)

        source, created = Source.objects.get_or_create(name=source_name, url=source_url)

        for entry in feed.entries:
            title = entry.get('title', '')
            description = entry.get('description', '')
            url = entry.get('link', '')
            published_date = entry.get('published_parsed')

            if published_date:
                published_date_str = datetime.datetime(*published_date[:6]).isoformat()
                published_date = make_aware(datetime.datetime.fromisoformat(published_date_str))
            else:
                published_date = datetime.datetime.now()

            article, created = Article.objects.get_or_create(
                title=title,
                #description=description,
                url=url,
                published_date=published_date,
                source=source
            )

    return redirect('home')




