from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.shortcuts import redirect

def about_blog(request: HttpRequest) -> HttpResponse:
    return HttpResponse(f"This is blog")


def show_home(request: HttpRequest) -> HttpResponse:
    return HttpResponse(f"This is home page")


def view_article(request: HttpRequest, article_id: int) -> HttpResponse:
    return HttpResponse(f"This is page of article {article_id}")


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
    return HttpResponse(f"Username is {username}")


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
