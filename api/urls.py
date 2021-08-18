from django.urls import path, include, re_path

urlpatterns = [
    path('rest/', include('api.rest_api.urls')),
    path('', include('api.wagtail_api.urls')),


]
