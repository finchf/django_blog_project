from django.urls import path
from blog.views import *

urlpatterns = [
    path("about/", about_blog),
    path("", show_home, name='home'),
    path("set-password/",set_password),
    path("set-userdata/", set_userdata),
    path("register/", create_new_user),
    path("deactivate/", deacivate_account),
    path("login/", login_page),
    path("logout/", logout_user),
    path("topics/", view_topics),
    path("<str:name>/comment/", article_comment, name='article'),
    path("create/", create_article),
    path("<article>/update/", article_update),
    path("<article>/delete/", article_delete),
    path("<str:name>/", view_article, name='article'),
    path("topics/<str:topic>/", topic_change),
    path("topics/<str:topic>/subscribe/", subscribe_topic),
    path("topics/<str:topic>/unsubscribe/", unsubscribe_topic),
    path("profile/<str:username>/", user_profile),
]
