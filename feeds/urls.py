from django.urls import path
from . import views


urlpatterns = [
    path('livemint/', views.feed_reader_view),
]
