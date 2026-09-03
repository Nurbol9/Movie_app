from django.urls import path, include
from rest_framework import routers

from .views import (RegisterView,LoginView,LogoutView,
    UserProfileDetailAPIView,UserProfileListAPIView,CategoryListAPIView,CategoryDetailAPIView,GenreListAPIView,CountryListAPIView,DirectorListAPIView,DirectorDetailAPIView,ActorListAPIView,ActorDetailAPIView,MovieListAPIView,MovieVideoViewSet,
    MovieFrameViewSet,ReviewViewSet,CountryDetailAPIView,
    ReviewLikeViewSet,HistoryViewSet,GenreDetailAPIView,MovieListAPIView,MovieDetailAPIView
)

router = routers.DefaultRouter()

router.register('movie-video', MovieVideoViewSet)
router.register('movie-frame', MovieFrameViewSet)
router.register('review', ReviewViewSet)
router.register('review-like', ReviewLikeViewSet)
router.register('history', HistoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('user/', UserProfileListAPIView.as_view(),name= 'user-list'),
    path('user/<int:pk>',UserProfileDetailAPIView.as_view(), name='user-detail'),
    path('category/', CategoryListAPIView.as_view(), name='category_list'),
    path('category/<int:pk>',CategoryDetailAPIView.as_view(),  name='category_detail'),
    path('genre/',GenreListAPIView.as_view(),name='genre_list'),
    path('genre/<int:pk>',GenreDetailAPIView.as_view(),name='genre_detail'),
    path('movie/', MovieListAPIView.as_view(), name='movie-list'),
    path('movie/<int:pk>', MovieDetailAPIView.as_view(), name='movie-detail'),
    path('country/', CountryListAPIView.as_view(), name='country-list'),
    path('country/<int:pk>', CountryDetailAPIView.as_view(), name='country-detail'),
    path('director/', DirectorListAPIView.as_view(), name='director_list'),
    path('director/<int:pk>', DirectorDetailAPIView.as_view(), name='director_detail'),
    path('actor/', ActorListAPIView.as_view(), name='actor_list'),
    path('actor/<int:pk>', ActorDetailAPIView.as_view(), name='actor_detail')

]