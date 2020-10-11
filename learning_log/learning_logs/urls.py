"""Defines URL patterns for learning_logs."""


from django.urls import path
from . import views


app_name = 'learning_logs'
urlpatterns = [
    # Home page.
    path('', views.index, name='index'),
    # Page that allows all topics.
    path('topics/', views.topics, name='topics')
]
