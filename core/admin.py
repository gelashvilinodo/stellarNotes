from django.contrib import admin
from core.models import Tag, Comment, Review, ArticleModel

# Register your models here.
admin.site.register(Tag)
admin.site.register(ArticleModel)
admin.site.register(Comment)
admin.site.register(Review)