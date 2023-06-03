from django.shortcuts import render, redirect
from .models import Article
# Create your views here.

def main(request):
    return render(request, 'main.html')

def new(request):
    if request.method == 'POST':
        print(request.POST)

        #model에 어떻게 담길 것인지 지정해주는 것이 필요하다.
        new_article=Article.objects.create(
            title=request.POST['title'],
            content=request.POST['content'],
            category=request.POST['category']
        )
        return redirect('list')
    return render(request, 'new.html', {})

def list(request):
    articles = Article.objects.all()
    return render(request, 'list.html', {'articles':articles})

def detail(request, article_id):
    article=Article.objects.get(id = article_id)
    return render(request, 'detail.html', {'article':article})

def category(request, category):
    articles =Article.objects.filter(category=category)

    return render(request, 'category.html', {'articles':articles, 'category':category})