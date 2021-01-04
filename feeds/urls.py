from django.urls import path, include
from rest_framework.routers import SimpleRouter
from . import views


sources = SimpleRouter()
sources.register(r'sources', views.FeedSourceViewset)

summary = SimpleRouter()
summary.register(r'summary', views.FeedViewset)


urlpatterns = [
    path('', include(sources.urls)),
    path('', include(summary.urls)),
]
