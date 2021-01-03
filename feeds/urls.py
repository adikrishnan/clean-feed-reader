from django.urls import path, include
from rest_framework.routers import SimpleRouter
from . import views


sources = SimpleRouter()
sources.register(r'sources', views.FeedSourcesViewset)

summary = SimpleRouter()
summary.register(r'summary', views.FeedSummaryViewset)


urlpatterns = [
    path('', include(sources.urls)),
    path('', include(summary.urls)),
]
