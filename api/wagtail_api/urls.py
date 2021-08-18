from django.urls import path, include, re_path

from api.wagtail_api.api import api_router

urlpatterns = [
    path('', api_router.urls),
]
