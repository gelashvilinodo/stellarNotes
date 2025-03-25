from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator


class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Articles(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    thumbnail = models.ImageField(upload_to="media/")
    title = models.CharField(max_length=200)
    tags = models.ManyToManyField(Tag, blank=True)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)

    def rating(self):
        reviews = self.review_set.all()
        if not reviews:
            return 0
        rating = sum([review.rating for review in reviews]) / len(reviews)
        return rating


class Comment(models.Model):
    article = models.ForeignKey(Articles, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text


class Review(models.Model):

    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    article = models.ForeignKey(Articles, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(validators=[MaxValueValidator(5)])

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user", "article"], name="unique_user_article"
            )
        ]
