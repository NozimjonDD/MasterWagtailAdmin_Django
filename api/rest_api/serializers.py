from rest_framework.serializers import ModelSerializer

from blogs.models import BlogPage


class BlogPageListSerializer(ModelSerializer):
    class Meta:
        model = BlogPage
        fields = '__all__'
