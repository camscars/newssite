from django.shortcuts import render
from .models import Story
import datetime
from django.utils.timezone import utc
# Create your views here.

def score(Story, gravity=1.8, timebase=120):
	points = (Story.points - 1)**0.8
	now = datetime.datetime.utcnow().replace(tzinfo=utc)
	age = int((now - Story.created).total_seconds())/60

	return points/(age+timebase)**1.8

def top_stories(top=180, consider=1000):
	latest_stories = Story.objects.all().order_by('-created')[:consider]
	ranked_stories = sorted(latest_stories, key=lambda story: story.points, reverse=True)
	return[story for story in ranked_stories][:top]


def index(request):
	stories = top_stories(top=30)
	return render(request, 'stories/index.html', {'stories':stories})