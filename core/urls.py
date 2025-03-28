from django.urls import path
from core.views import home_view, register_view, login_view, logout_view, article_view

urlpatterns = [
    path("home", home_view, name="home"),
    path("register/", register_view, name="register"),
    path("", login_view, name="login"),
    path("logout/", login_view, name="logout"),
    path("article/<int:pk>/", article_view, name="article"),
]
