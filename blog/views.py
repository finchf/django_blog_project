from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.shortcuts import redirect

def about_blog(request: HttpRequest) -> HttpResponse:
    return HttpResponse(f"This is blog")


def show_home(request: HttpRequest) -> HttpResponse:
    return HttpResponse(f"This is home page")


def view_article(request: HttpRequest, name: str) -> HttpResponse:
    return HttpResponse(f"This is page of article {name}")


def article_comment(request: HttpRequest, name: str,) -> HttpResponse:
    return HttpResponse(f"This is comment of article {name}")


def create_article(request: HttpRequest) -> HttpResponse:
    return HttpResponse(f"This is the article creation form page")


def article_update(request: HttpRequest, article: str) -> HttpResponse:
    return HttpResponse(f"This is page for update  {article} ")


def article_delete(request: HttpRequest, article: str) -> HttpResponse:
    return HttpResponse(f"This is page for delete  {article} ")


def view_topics(request: HttpRequest) -> HttpResponse:
    return HttpResponse(f"This is all topics on blog")


def topic_change(request: HttpRequest, topic: str) -> HttpResponse:
    return HttpResponse(f"Topic_change")


def subscribe_topic(request: HttpRequest, topic: str) -> HttpResponse:
    return HttpResponse(f"Subscribe topic")


def unsubscribe_topic(request: HttpRequest, topic: str) -> HttpResponse:
    return HttpResponse(f"Unsubscribe topic")


def user_profile(request: HttpRequest, username: str) -> HttpResponse:
    return HttpResponse(f"Username is {username}")


def set_password(request: HttpRequest) -> HttpResponse:
    return HttpResponse(f"Please, set your new password")


def set_userdata(request: HttpRequest) -> HttpResponse:
    return HttpResponse(f"Please, update user info")


def deacivate_account(request: HttpRequest) -> HttpResponse:
    return HttpResponse(f"On this page you can deactivate your account")


def create_new_user(request: HttpRequest) -> HttpResponse:
    return HttpResponse(f"Create new profile!")


def login_page(request: HttpRequest) -> HttpResponse:
    return HttpResponse(f"Hello! log in, please!")


def logout_user(request: HttpRequest) -> redirect:
    logout(request)
    return redirect("home")
