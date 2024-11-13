from datetime import datetime

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django_extensions.db.fields import AutoSlugField


class StaffMovie(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = AutoSlugField(
        max_length=100, populate_from=['name']
    )
    description = models.TextField(null=True, blank=True)
    poster = models.URLField(null=True, blank=True)

    class Meta:
        abstract = True
        ordering = ("name",)

    def __str__(self):
        return self.name


class Genre(StaffMovie):
    pass


class Star(StaffMovie):
    pass


class Director(StaffMovie):
    pass


class Certification(StaffMovie):
    pass


class Movie(models.Model):
    name = models.CharField(max_length=250)
    slug = AutoSlugField(
        max_length=100,
        populate_from=['name']
    )
    year = models.IntegerField(
        validators=[
            MinValueValidator(1888),
            MaxValueValidator(datetime.now().year + 2)
        ]
    )
    time = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(600)
        ]
    )
    imdb = models.FloatField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(10)
        ]
    )
    votes = models.IntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(10000000)
        ]
    )
    meta_score = models.FloatField(
        null=True,
        blank=True,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100)
        ]
    )
    gross = models.FloatField(
        null=True,
        blank=True,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(1000000000)
        ]
    )
    description = models.TextField()
    price = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
        blank=True
    )

    certification = models.ForeignKey(
        'Certification',
        on_delete=models.PROTECT,
        related_name='movies'
    )

    genres = models.ManyToManyField(
        Genre,
        through='MovieGenre',
        related_name='movies'
    )
    directors = models.ManyToManyField(
        Director,
        through='MovieDirector',
        related_name='movies'
    )
    stars = models.ManyToManyField(
        Star,
        through='MovieStar',
        related_name='movies'
    )

    class Meta:
        ordering = ('name', 'year')
        constraints = [
            models.UniqueConstraint(fields=['name', 'year', 'time'], name='unique_movie_constraint')
        ]

    def __str__(self):
        return f'{self.name} - {self.year}'


class MovieGenre(models.Model):
    class ImportanceLevel(models.IntegerChoices):
        VERY_LOW = 1, 'Very Low'
        LOW = 2, 'Low'
        MEDIUM = 3, 'Medium'
        HIGH = 4, 'High'
        VERY_HIGH = 5, 'Very High'

    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    importance_level = models.IntegerField(
        choices=ImportanceLevel.choices,
        null=True,
        blank=True
    )
    added_date = models.DateField(auto_now_add=True)
    notes = models.TextField(null=True, blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['movie', 'genre'], name='unique_movie_genre_constraint')
        ]

    def __str__(self):
        return f'{self.movie} - {self.genre}'


class MovieDirector(models.Model):
    class RoleType(models.TextChoices):
        MAIN_DIRECTOR = 'Main Director', 'Main Director'
        ASSISTANT_DIRECTOR = 'Assistant Director', 'Assistant Director'
        CO_DIRECTOR = 'Co-Director', 'Co-Director'
        EXECUTIVE_PRODUCER = 'Executive Producer', 'Executive Producer'

    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)

    role = models.CharField(
        max_length=20,
        choices=RoleType.choices,
        null=True,
        blank=True
    )
    collaboration_years = models.IntegerField(null=True, blank=True)
    comments = models.TextField(null=True, blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['movie', 'director'], name='unique_movie_director_constraint')
        ]

    def __str__(self):
        return f'{self.movie} - {self.director}'


class MovieStar(models.Model):
    class RoleType(models.TextChoices):
        LEAD = 'Lead', 'Lead'
        SUPPORTING = 'Supporting', 'Supporting'
        CAMEO = 'Cameo', 'Cameo'
        EPISODIC = 'Episodic', 'Episodic'

    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    star = models.ForeignKey(Star, on_delete=models.CASCADE)

    role = models.CharField(
        max_length=20,
        choices=RoleType.choices,
        null=True,
        blank=True
    )
    screen_time = models.IntegerField(null=True, blank=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    character_name = models.CharField(max_length=100, null=True, blank=True)
    debut = models.BooleanField(null=True, blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['movie', 'star'], name='unique_movie_star_constraint')
        ]

    def __str__(self):
        return f'{self.movie} - {self.star}'
