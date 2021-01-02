from django.urls import path
from . import views


urlpatterns = [
    path('quint/', views.quint_reader_view),
    path('gwtj/', views.gwtj_reader_view),
]
