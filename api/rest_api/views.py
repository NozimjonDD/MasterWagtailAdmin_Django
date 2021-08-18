from rest_framework.generics import ListAPIView, CreateAPIView

from api.rest_api.serializers import BlogPageListSerializer
from blogs.models import BlogPage


class BlogPageListAPIView(ListAPIView):
    queryset = BlogPage.objects.all()
    serializer_class = BlogPageListSerializer
