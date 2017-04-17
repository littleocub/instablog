""" define URL of instablogs """
from django.conf.urls import url
from . import views

urlpatterns = [
    # homepage
    url(r'^$', views.index, name='index'),

    # display all topics
    url(r'^topics/$', views.topics, name='topics'),

    # display specific topic
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
    ]