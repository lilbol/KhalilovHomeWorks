from django.db import models
from django.contrib.auth.models import User


class Director(models.Model):
    name = models.CharField(max_length=200)

    @property
    def count_movies(self):
        return self.movies.all().count()

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    duration = models.FloatField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE,
                                 related_name='movies')

    def __str__(self):
        return self.title

    @property
    def rating(self):
        p = 0
        for i in self.reviews.all():
            p += int(i.stars)
        return p / self.reviews.all().count()


class Review(models.Model):
    STARS_CHOICE = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )
    text = models.TextField(max_length=200)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE,
                              related_name='reviews')
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               null=True, blank=True)
    stars = models.CharField(choices=STARS_CHOICE, max_length=100)

    def __str__(self):
        return self.text
