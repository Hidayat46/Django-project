from django.shortcuts import render 
from .models import models
from .forms import TweetForm
from django.shortcuts import get_object_or_404 , redirect
# Create your views here.
def index(request):
    return render(request , 'index.html')
def tweet_list(request):
    tweets = TweetForm.object.all().order_by('_created_at')
    return render(request, 'tweets_list.html', {'tweets': tweets})

def tweet_create(request):
    if request.method =="POST":
     form = TweetForm(request.POST, request.FILES)
     if form.is_valid():
        tweet = form.save(commit=False)
        tweet.user = request.user
        tweet.save()
        return redirect('tweet_list')
    else:
        form = TweetForm()
    return render(request, 'tweet_form.html',{'form': form})

def tweet_edit(request, tweet_id):
    tweet = get_object_or_404(tweet, pk=tweet_id , user = request.user)
    if request .method =="POST":
        form = TweetForm(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list')
    else:
       form = TweetForm(instance=tweet)
       return render(request, 'tweet_form.html',{'form': form})

    