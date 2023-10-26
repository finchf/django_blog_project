from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpRequest
from .models import Article, Comment, User
from django.http import Http404


def about_blog(request: HttpRequest) -> HttpResponse:
    return HttpResponse(f"This is blog")


def show_home(request: HttpRequest) -> HttpResponse:
    articles = Article.objects.all()
    return render(request, 'blog/first.html', {'articles': articles})


def view_article(request: HttpRequest, article_id: int) -> HttpResponse:
    article = get_object_or_404(Article, pk=article_id)
    return render(request, 'blog/article.html', {'article': article})


def add_comment(request: HttpRequest, article_id: int) -> HttpResponse:
    return HttpResponse(f"This is comment of article {article_id}")


def create_article(request: HttpRequest) -> HttpResponse:
    return HttpResponse(f"This is the article creation form page")


def article_update(request: HttpRequest, article_id: int) -> HttpResponse:
    return HttpResponse(f"This is page for update  {article_id} ")


def article_delete(request: HttpRequest, article_id: int) -> HttpResponse:
    return HttpResponse(f"This is page for delete  {article_id} ")


def view_topics(request: HttpRequest) -> HttpResponse:
    return HttpResponse(f"This is all topics on blog")


def subscribe_topic(request: HttpRequest, topic_id: int) -> HttpResponse:
    return HttpResponse(f"Subscribe topic")


def unsubscribe_topic(request: HttpRequest, topic_id: int) -> HttpResponse:
    return HttpResponse(f"Unsubscribe topic")


def user_profile(request: HttpRequest, username: str) -> HttpResponse:
    user = get_object_or_404(User, username=username)
    articles = Article.objects.filter(author=user)
    return render(request, 'blog/user_profile.html', {'user': user, 'articles': articles})


def set_password(request: HttpRequest) -> HttpResponse:
    return HttpResponse(f"Please, set your new password")


def set_userdata(request: HttpRequest) -> HttpResponse:
    return HttpResponse(f"Please, update user info")


def deacivate_account(request: HttpRequest) -> HttpResponse:
    return HttpResponse(f"On this page you can deactivate your account")


def register(request: HttpRequest) -> HttpResponse:
    return HttpResponse(f"Create new profile!")


def login(request: HttpRequest) -> HttpResponse:
    return HttpResponse(f"Hello! log in, please!")


def logout(request: HttpRequest) -> redirect:
    logout(request)
    return redirect("home")
