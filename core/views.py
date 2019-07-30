from django.shortcuts import render, redirect
from core.models import User, Forum, Comment, Category, Resource, BlogPost, ProgressTracker, VisionBoard
import json
from django.views import generic
from django.contrib.auth.decorators import login_required

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



@login_required
def add_new_blog(request):
    from core.forms import BlogForm
    from django.views.generic.edit import CreateView
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            form.save()
            return redirect('blog')
    else:
        form = BlogForm()
    return render(request, 'core/blogpost_form.html', {'form': form})