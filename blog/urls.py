from django.urls import path
from .views import about_blog, show_home,set_password, set_userdata, register, deacivate_account, \
    login, logout, view_topics, add_comment, create_article, article_update, article_delete, view_article,\
    subscribe_topic, unsubscribe_topic, user_profile

urlpatterns = [
    path("about/", about_blog, name='about'),
    path("", show_home, name='home'),
    path("set-password/",set_password, name='set_password'),
    path("set-userdata/", set_userdata, name='set_userdata'),
    path("register/", register, name='register'),
    path("deactivate/", deacivate_account, name='deactivate'),
    path("login/", login, name='login'),
    path("logout/", logout, name='logout'),
    path("create/", create_article, name='create'),
    path("<int:article_id>/", view_article, name='detail'),
    path("<int:article_id>/comment/", add_comment, name='add_comment'),
    path("<int:article_id>/update/", article_update, name='article_update'),
    path("<int:article_id>/delete/", article_delete, name='article_delete'),
    path("topics/", view_topics, name='topics'),
    path("topics/<int:topic_id>/subscribe/", subscribe_topic, name='subscribe_topic'),
    path("topics/<int:topic_id>/unsubscribe/", unsubscribe_topic, name='unsubscribe_topic'),
    path("profile/<username>/", user_profile, name='user_profile'),
]
