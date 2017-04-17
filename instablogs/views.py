from django.shortcuts import render
from .models import Topic

# Create your views here.
def index(request):
    """ index of instablogs """
    return render(request, 'instablogs/index.html')

def topics(request):
    """ display all topics """
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'instablogs/topics.html', context)

def topic(request, topic_id):
    """ disply specific topic """
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'instablogs/topic.html', context)