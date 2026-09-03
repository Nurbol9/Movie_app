from modeltranslation.translator import TranslationOptions, register
from .models import (Category,Genre,Country,Director,Actor,Movie,MovieVideo,)


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('category_name',)


@register(Genre)
class GenreTranslationOptions(TranslationOptions):
    fields = ('genre_name',)


@register(Country)
class CountryTranslationOptions(TranslationOptions):
    fields = ('country_name',)


@register(Director)
class DirectorTranslationOptions(TranslationOptions):
    fields = ('director_bio',)


@register(Actor)
class ActorTranslationOptions(TranslationOptions):
    fields = ('actor_bio',)


@register(Movie)
class MovieTranslationOptions(TranslationOptions):
    fields = ('movie_name', 'descriptions','slogan')


@register(MovieVideo)
class MovieVideoTranslationOptions(TranslationOptions):
    fields = ('video_name',)