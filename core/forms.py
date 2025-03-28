from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from core.models import Comment, ArticleModel, Review


class ArticleForm(forms.ModelForm):
    class Meta:
        model = ArticleModel
        fields = ['title', 'thumbnail', 'tags', 'text']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter article title'
            }),
            'thumbnail': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),
            'tags': forms.SelectMultiple(attrs={
                'class': 'form-control'
            }),
            'text': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Write your article here...'
            }),
        }
        
        

class ReviewForm(forms.ModelForm):
    RATING_CHOICES = [
        (0, '0 ~ No rating'),
        (1, '1 ~ Poor'),
        (2, '2 ~ Fair'),
        (3, '3 ~ Good'),
        (4, '4 ~ Very Good'),
        (5, '5 ~ Great'),
    ]
    
    class Meta:
        model = Review
        fields = ['rating']
        widgets = {
            'rating': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Rate article'
            }),
        }
        
    rating = forms.ChoiceField(choices=RATING_CHOICES, widget=forms.Select(attrs={
        'class': 'form-control',
    }))



class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class LoginForm(AuthenticationForm):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["text"]
        widgets = {
            "text": forms.Textarea(
                attrs={"placeholder": "Write your comment here..."}
            ),
        }
