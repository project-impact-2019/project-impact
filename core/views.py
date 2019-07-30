from django.shortcuts import render
from core.models import User, Forum, Comment, Category, Resource, BlogPost, ProgressTracker, VisionBoard
import json
from django.views import generic

# Views Created Here
def index(request):
    """View function for home page of site."""
    
    return render(request, 'index.html')

def give_back(request):
    """View for How to Give Back to Foster Children Aging Out of System"""
    view = 'give_back'
    return render(request, 'give_back.html')

class BlogPostListView(generic.ListView):
    """View for Blog Post List"""
    model = BlogPost
    paginate_by = 5

class BlogPostDetailView(generic.DetailView):
    """View for Blog Post Details"""
    model = BlogPost



