from django.shortcuts import render, redirect
from .models import Article, Comment, Reply
from django.utils import timezone
from datetime import datetime
# Create your views here.

def main(request):
    articles = Article.objects.all()
    a=0
    b=0
    c=0
    for article in articles:
        if article.category == 'programming':
            a+=1
        if article.category == 'music':
            b+=1
        if article.category == 'study':
            c+=1
    return render(request, 'main.html',{'a' :a, 'b':b, 'c':c, 'articles':articles})

def new(request):
    if request.method == 'POST':
        print(request.POST)

        #model에 어떻게 담길 것인지 지정해주는 것이 필요하다.
        new_article=Article.objects.create(
            title=request.POST['title'],
            content=request.POST['content'],
            category=request.POST['category']
        )
        return redirect('detail',new_article.id)
    return render(request, 'new.html', {})

def list(request):
    articles = Article.objects.all()
    a=0
    b=0
    c=0
    for article in articles:
        if article.category == 'programming':
            a+=1
        if article.category == 'music':
            b+=1
        if article.category == 'study':
            c+=1
    return render(request, 'list.html', {'articles':articles, 'a' :a, 'b':b, 'c':c})

def detail(request, article_id):
    article=Article.objects.get(id = article_id)
    ###댓글###

    comments_all=Comment.objects.all() #comments_all : 댓글과 대댓글 전체를 가져옴
    replies=Reply.objects.all()
    comments_for=[]
    for comment in comments_all:
        if article.id == comment.article_id:
            comments_for.append(comment)  #comments_for : 해당 글과 관련된 댓글과 대댓글 들만 가져옴

    if request.method =="POST":
                comment=Comment.objects.create( #그냥 댓글로 만드세요
                    article=article,
                    content=request.POST['content'],
                    created_at=datetime.now(),
                )
                return redirect('detail', article_id)
    ###댓글 관련
    return render(request, 'detail.html', {'article':article, 'comments_for':comments_for, 'replies':replies})

def category(request, category):
    articles =Article.objects.filter(category=category)

    return render(request, 'category.html', {'articles':articles, 'category':category})

def update(request, article_id):
    article=Article.objects.get(id=article_id)

    if request.method =='POST':
        Article.objects.filter(id=article_id).update(
            title=request.POST['title'],
            content=request.POST['content'],
            category=request.POST['category'],
            updated_at=datetime.now()
        )

        return redirect('detail',article_id)
    return render(request, 'update.html', {'article':article})

def delete(request, article_id):
    article=Article.objects.get(id=article_id)
    article.delete()
    return redirect('list')

def alldelete(request):
    articles=Article.objects.all()
    for article in articles:
        article.delete()
    return redirect('list')

def delete_comment(request, article_id, comment_id):
    comment=Comment.objects.get(id=comment_id)
    comment.delete()
    return redirect('detail', article_id)

def delete_reply(request, article_id, comment_id, reply_id):
    reply=Reply.objects.get(id=reply_id)
    reply.delete()
    return redirect('detail', article_id)

def like(request, article_id, comment_id):
    comment=Comment.objects.get(id=comment_id)
    Comment.objects.filter(id=comment_id).update(
        like=comment.like+1
    )
    return redirect('detail', article_id)

def like_reply(request, article_id, comment_id, reply_id):
    reply=Reply.objects.get(id=reply_id)
    Reply.objects.filter(id=reply_id).update(
        like=reply.like+1
    )
    return redirect('detail', article_id)

def reply(request, article_id, comment_id):
    comment=Comment.objects.get(id=comment_id)
    if request.method =="POST":
        reply=Reply.objects.create( #그냥 댓글로 만드세요
            comment=comment,
            content=request.POST['content'],
            created_at=datetime.now(),
        )
        return redirect('detail', article_id)
    #     return redirect('detail', article_id)