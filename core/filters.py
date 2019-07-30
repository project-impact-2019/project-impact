import django_filters
from core.models import Forum, Resource, BlogPost

# Using Django Filter to search via different models

class ForumFilter(django_filters.FilterSet):

    class Meta:
        model=Forum

        fields = {
            'title': ['icontains',], 
            'description': ['icontains',], 
            'owner': ['exact',], 
        }


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