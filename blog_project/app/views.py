from django.shortcuts import render, redirect
from .models import Article, Category
# Create your views here.

def main(request):
    return render(request, 'main.html')

def new(request):
    categories=Category.objects.all()
    if request.method == 'POST':
        print(request.POST)

        #model에 어떻게 담길 것인지 지정해주는 것이 필요하다.
        new_article=Article.objects.create(
            title=request.POST['title'],
            content=request.POST['content'],
            category=request.POST['category']
        )
        return redirect('list')
    return render(request, 'new.html', {'categories':categories})

def list(request):
    articles = Article.objects.all()
    return render(request, 'list.html', {'articles':articles})

def detail(request, article_id):
    article=Article.objects.get(id = article_id)
    return render(request, 'detail.html', {'article':article})

def new_menu(request):
    if request.method =='POST':
        print(request.POST)

        new_menu=Category.objects.create(
            name=request.POST['category']
        )
        return redirect('menu')
    return render(request, 'new_menu.html')

def menu(request):
    categories = Category.objects.all()
    return render(request, 'menu.html', {'categories':categories})

def category(request, category_name):
    category_articles =Article.objects.filter(name=category_name)
    categories = Category.objects.all()

    return render(request, 'category.html', {'category_posts':category_articles, 'categories':categories, 'category_name':category_name})