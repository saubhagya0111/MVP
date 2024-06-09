
from django.contrib import admin
from django.urls import path
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TweetViewSet, VideoViewSet, create_tweet

router = DefaultRouter()
router.register(r'tweets', TweetViewSet)
router.register(r'videos', VideoViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('create-tweet/', create_tweet, name='create_tweet'),
]


urlpatterns = [
    path('admin/', admin.site.urls),
]
