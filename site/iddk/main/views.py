# views.py
from django.shortcuts import render, get_object_or_404
from .models import News, Image, SliderImage, About, Authors, Editors, Readers  # Импортируйте новые модели

def index(request):
    news = News.objects.filter(is_published=True).order_by('-published_date')
    images = Image.objects.all()
    slider_images = SliderImage.objects.all()
    return render(request, 'main/index.html', {'news': news, 'images': images, 'slider_images': slider_images})

def about(request):
    about_content = About.objects.first()
    return render(request, 'main/about.html', {'about': about_content})

def authors(request):
    authors_content = Authors.objects.first()  # Получаем первый объект Authors
    return render(request, 'main/authors.html', {'authors': authors_content})

def news(request):
    news = News.objects.filter(is_published=True).order_by('-published_date')
    return render(request, 'main/news.html', {'news': news})

def readers(request):
    readers_content = Readers.objects.first()  # Получаем первый объект Readers
    return render(request, 'main/readers.html', {'readers': readers_content})

def editors(request):
    editors_content = Editors.objects.first()  # Получаем первый объект Editors
    return render(request, 'main/editors.html', {'editors': editors_content})

def like_news(request, news_id):
    news = get_object_or_404(News, id=news_id)
    news.likes += 1
    news.save()
    return redirect('news')

def dislike_news(request, news_id):
    news = get_object_or_404(News, id=news_id)
    news.dislikes += 1
    news.save()
    return redirect('news')