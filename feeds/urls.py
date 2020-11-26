from django.urls import path
from . import views


urlpatterns = [
    path('livemint/', views.livemint_reader_view),
    path('quint/', views.quint_reader_view),
]
