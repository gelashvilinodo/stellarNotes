from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from core.forms import RegisterForm, LoginForm, CommentForm, ArticleForm, ReviewForm
from .models import ArticleModel, Comment, Tag, Review
from django.contrib.auth.models import User


def home_view(request):
    articles = ArticleModel.objects.all().order_by("-created_at")
    return render(request, "home.html", {"articles": articles})


def article_view(request, pk):
    article = get_object_or_404(ArticleModel, pk=pk)
    article.views += 1
    article.save()
    comments = Comment.objects.filter(article=article).order_by("-created_at")
    reviews = Review.objects.filter(article=article)
    rating = article.rating()
    
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.user = request.user
            comment.save()
            return redirect("article", pk=pk)
    else:
        form = CommentForm()
        
    if request.method == "POST":
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.article = article
            review.user = request.user
            review.save()
            return redirect("article", pk=pk)
    else:
        review_form = ReviewForm()
    
    
    context = {
        "form": form,
        "article": article,
        "comments": comments,
        "reviews": reviews,
        "rating": rating,
        "review_form": review_form,
    }
    return render(request, "article.html", context)


def user_articles_view(request, username):
    user = get_object_or_404(User, username=username)
    articles = ArticleModel.objects.filter(author=user).order_by("-created_at")
    return render(request, "user_articles.html", {"articles": articles, "user": user})


def create_article_view(request):
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            form.save_m2m()
            return redirect("home")
    else:
        form = ArticleForm()
    return render(request, "create_article.html", {"form": form})


def article_by_tag_view(request, tag_name):
    tag = get_object_or_404(Tag, name=tag_name)
    articles = ArticleModel.objects.filter(tags=tag).order_by("-created_at")
    return render(request, "articles_by_tag.html", {"articles": articles, "tag": tag})


def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect("login")
    else:
        form = RegisterForm()
    return render(request, "register.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("home")
    else:
        form = LoginForm()
    return render(request, "login.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("login")
