import django_filters
from core.models import Forum, Resource, BlogPost

# Using Django Filter to search via different models


class ResourceFilter(django_filters.FilterSet):

    class Meta:
        model=Resource

        fields = {
            'title': ['icontains',], 
            'description': ['icontains',], 
            'category': ['exact',], 
        }


class BlogPostFilter(django_filters.FilterSet):

    class Meta:
        model=BlogPost

        fields = {
            'title': ['icontains',], 
            'content': ['icontains',], 
            'author': ['exact',], 
        }