from django.urls import path
from core.views import home_view, register_view, login_view, logout_view, article_view, user_articles_view, create_article_view, article_by_tag_view

urlpatterns = [
    path("home", home_view, name="home"),
    path("register/", register_view, name="register"),
    path("", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("article/<int:pk>/", article_view, name="article"),
    path("user/<str:username>/", user_articles_view, name="user_articles"),
    path("create_article/", create_article_view, name="create_article"),
    path("tag/<str:tag_name>/", article_by_tag_view, name="article_by_tag"),
]
