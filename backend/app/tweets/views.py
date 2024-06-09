from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .models import Tweet, Video
from .serializers import TweetSerializer, VideoSerializer
from .conversion import tweet_to_video

# Function-based view for creating a tweet and converting it to video
def create_tweet(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        tweet = Tweet.objects.create(user=request.user, content=content)
        video_file = f'media/videos/{tweet.id}.mp4'
        tweet_to_video(content, video_file)
        Video.objects.create(tweet=tweet, video_file=video_file)
        return HttpResponse('Tweet created and video generated!')
    return render(request, 'create_tweet.html')

# ViewSets for the API
class TweetViewSet(viewsets.ModelViewSet):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer

class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
