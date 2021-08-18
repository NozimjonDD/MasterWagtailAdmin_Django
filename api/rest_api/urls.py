from django.urls import path, include, re_path

from api.rest_api.views import BlogPageListAPIView

urlpatterns = [
    path('list/', BlogPageListAPIView.as_view()),
]
