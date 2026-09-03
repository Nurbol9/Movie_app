from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from phonenumber_field.modelfields import PhoneNumberField

STATUS_CHOICES = [
    ('pro', 'pro'),
    ('simple', 'simple'),
]

class UserProfile(AbstractUser):
    phone_number = PhoneNumberField(null=True, blank=True)
    age = models.PositiveSmallIntegerField(validators=[MinValueValidator(16), MaxValueValidator(80)], null=True, blank=True )
    profile_image = models.ImageField(upload_to='profile_photo/', null=True, blank=True)
    status = models.CharField(max_length=32, choices=STATUS_CHOICES, default='simple')
    date_registered = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name}-{self.last_name}'


class Category(models.Model):
    category_name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.category_name


class Genre(models.Model):
    genre_name = models.CharField(max_length=32,)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,related_name='genre_category')

    def __str__(self):
        return self.genre_name


class Country(models.Model):
    country_name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.country_name


class Director(models.Model):
    full_name = models.CharField(max_length=150)
    director_image = models.ImageField(upload_to='director_photo/', null=True, blank=True)
    director_bio = models.TextField()
    birth_date = models.DateField()

    def __str__(self):
        return self.full_name


class Actor(models.Model):
    full_name = models.CharField(max_length=150)
    actor_image = models.ImageField(upload_to='actor_photo/', null=True, blank=True)
    actor_bio = models.TextField()
    birth_date = models.DateField()

    def __str__(self):
        return self.full_name


class Movie(models.Model):
    movie_name = models.CharField(max_length=150)
    slogan = models.CharField(max_length=200, verbose_name='Слоган')
    year = models.DateField()
    country = models.ManyToManyField(Country, related_name='movie_list')
    director = models.ManyToManyField(Director, related_name='director_list')
    genre = models.ManyToManyField(Genre, related_name='genre_move')

    MovieTypeChoices = [
        ('360p', '360p'),
        ('480p', '480p'),
        ('720p', '720p'),
        ('1080p', '1080p'),
        ('1080p Ultra', '1080p Ultra'),
    ]

    movie_type = models.CharField(max_length=22, choices=MovieTypeChoices)
    movie_time = models.PositiveSmallIntegerField()
    actor = models.ManyToManyField(Actor,related_name='actor_list')
    descriptions = models.TextField()
    movie_image = models.ImageField(upload_to='movie_image/',)
    movie_trailer = models.URLField()
    movie_status = models.CharField(max_length=32, choices=STATUS_CHOICES)

    def __str__(self):
        return self.movie_name


class MovieVideo(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movie_language')
    video_name = models.CharField(max_length=32)
    movie_video = models.FileField(upload_to='movie_video/')


class MovieFrame(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movie_moment')
    moment = models.ImageField(upload_to='movie_moments/')

    def __str__(self):
        return self.movie.movie_video


class Review(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movie_review')
    parent = models.ForeignKey(to='self', on_delete=models.CASCADE, null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} {self.movie.movie_name}'


class ReviewLike(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='review_like')
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    like = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username} {self.like}'


class History(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    viewed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.viewed_at
