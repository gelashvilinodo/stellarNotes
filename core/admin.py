from django.contrib import admin
from core.models import Tag, Articles, Comment, Review

# Register your models here.
admin.site.register(Tag)
admin.site.register(Articles)
admin.site.register(Comment)
admin.site.register(Review)