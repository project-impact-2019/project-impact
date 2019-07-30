<<<<<<< HEAD
from django.shortcuts import render, get_object_or_404
from .models import ResourcePost
from .forms import ResourcesPostModelForm
from django.contrib.auth.decorators import login_required


# Create your views here.

# Resource model views
@login_required
def resources_post_create_view(request):
    form = ResourcesPostModelForm(request.POST or None)
    if form.is_valid():
       obj = form.save(commit=False)
       obj.user = request.user
       obj.save()
       form = ResourcesPostModelForm()
    context={'form': form}
    return render(request, 'core/form.html', context)

@login_required
def blog_post_update_view(request, slug):
    obj = get_object_or_404(BlogPost,slug=slug)
    form = BlogPostModelForm(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
        return redirect("/blog")
    context={'form': form, 'title': f"Update {obj.title}" }
    return render(request, 'core/form.html', context)

def resources_post_list_view(request):

    queryset = Resource.objects.all()
    context={'object_list': queryset}

    return render(request, 'core/resources_post_list.html', context)

def resources_post_detail_view(request, slug):
    obj = get_object_or_404(BlogPost,slug=slug)
    context = {'object': obj}

    return render(request, 'core/resources_post_detail.html', context)
=======
from django.shortcuts import render
from core.models import User, Forum, Comment, Category, Resource, BlogPost, ProgressTracker, VisionBoard
import json
from django.views import generic

# Views Created Here


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



>>>>>>> f6522029524e2ee73da9017a0895f4bbd42e7f71
