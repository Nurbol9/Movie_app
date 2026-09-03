from rest_framework import serializers
from .models import ( UserProfile, Category, Country,Director, Genre,
                      Actor,Movie,MovieVideo,  MovieFrame,Review,ReviewLike,History,)

from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('username', 'email', 'password', 'first_name', 'last_name',
                  'age', 'phone_number',)
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = UserProfile.objects.create_user(**validated_data)
        return user

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Неверные учетные данные")

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }

class UserProfileListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name','last_name']

class UserProfileDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'



class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','category_name']

class GenreNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['genre_name']

class DirectorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ['full_name']



class DirectorNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ['full_name', ]


class GenreListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id','genre_name', ]

class ActorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['full_name']




class ActorNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['full_name']



class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['movie_name','slogan','year','director', 'country','genre','actor','descriptions','movie_trailer','movie_status',]

class CountryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['id', 'country_name']


class MovieListSerializer(serializers.ModelSerializer):
    genre = GenreNameSerializer(many=True,)
    class Meta:
        model = Movie
        fields = ['id','movie_name','year','movie_image','genre','movie_status']

class MovieVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieVideo
        fields = ['video_name','movie_video']

class DirectorDetailSerializer(serializers.ModelSerializer):
    director_list = MovieListSerializer(many=True,read_only=True)
    class Meta:
        model = Director
        fields = ['full_name', 'director_bio','director_image','birth_date','director_list']

class ActorDetailSerializer(serializers.ModelSerializer):
    actor_list = MovieListSerializer(many=True)
    class Meta:
        model = Actor
        fields = ['full_name','actor_image','actor_bio','birth_date','actor_list']

class MovieFrameSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieFrame
        fields = ['moment']


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class ReviewLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewLike
        fields = '__all__'



class CountryDetailSerializer(serializers.ModelSerializer):
    movie_list = MovieListSerializer( many=True, read_only=True)
    class Meta:
        model = Country
        fields = ['country_name', 'movie_list']


class MovieDetailSerializer(serializers.ModelSerializer):
    country = CountryListSerializer(many=True,read_only=True)
    genre = GenreNameSerializer(many=True,)
    director = DirectorNameSerializer(many=True)
    actor = ActorNameSerializer(many=True)
    movie_language = MovieVideoSerializer(many=True,read_only=True)
    movie_moment = MovieFrameSerializer(many=True,read_only=True)
    movie_review = ReviewSerializer(many=True,read_only=True)
    class Meta:
        model = Movie
        fields = ['movie_name','movie_status','slogan','year','director','country','genre','movie_image',
                  'movie_trailer','movie_type','movie_time','actor','descriptions','movie_moment','movie_language','movie_review']




class GenreDetailSerializer(serializers.ModelSerializer):
    genre_move = MovieListSerializer(many=True)

    class Meta:
        model = Genre
        fields = ['id', 'genre_name', 'genre_move']

class CategoryDetailSerializer(serializers.ModelSerializer):
    genre_category = GenreListSerializer(read_only=True,many=True)

    class Meta:
        model = Category
        fields = ['category_name','genre_category']



class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = '__all__'