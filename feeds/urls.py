from django.urls import path
from . import views


urlpatterns = [
    path('', views.root),
    path('quint/', views.quint_reader_view),
    path('gwtj/', views.gwtj_reader_view),
    path('moneycontrol/', views.moneycontrol_reader_view),
    path('skysports/', views.skysports_reader_view),
]
