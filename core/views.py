from django.shortcuts import render, redirect
from core.models import User, Forum, Comment, Category, Resource, BlogPost, Person
import json
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.views.generic import CreateView
from core.filters import BlogPostFilter, ResourceFilter
from core.forms import MenteeSignUpForm, MentorSignUpForm
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
User = get_user_model()



# Views Created Here
def index(request):
    """View function for home page of site."""
    
    return render(request, 'index.html')

def give_back(request):
    """View for How to Give Back to Foster Children Aging Out of System"""
    view = 'give_back'
    return render(request, 'give_back.html')


#BlogPost Model
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

#Resource Model
class ResourceListView(generic.ListView):
    """View for Resource List"""
    model = Resource
    paginate_by = 5

class ResourceDetailView(generic.DetailView):
    """View for Resource Details"""
    model = Resource

# Search Views
def search_resource(request):
    """View function to search for resources. This view is connected with Django Filters."""
    template_name = 'core/search_resource.html'
    resource = Resource.objects.filter()
    resource_filter = ResourceFilter(request.GET, queryset=resource)
   

    return render(request, 'core/search_resource.html', {'filter': resource_filter})


def search_blog(request):
    """View function to search for blogs. This view is connected with Django Filters."""
    template_name = 'core/search_blog.html'
    blog = BlogPost.objects.filter()
    blog_filter = BlogPostFilter(request.GET, queryset=blog)
   

    return render(request, 'core/search_blog.html', {'filter': blog_filter})

# SignUp Views
class MenteeSignUpView(CreateView):
    model = User
    form_class = MenteeSignUpForm
    template_name = 'core/mentee_signup_form.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save().user
        send_mail('New Mentee Application', 'There is a new Mentee Application! Please log into the admin site and review this application at your earliest convenience.', 'projectimpact919@gmail.com',
        ['projectimpact919@gmail.com'], fail_silently=False)
        return redirect('success')

class MentorSignUpView(CreateView):
    model = User
    form_class = MentorSignUpForm
    template_name = 'core/mentor_signup_form.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save().user 
        send_mail('New Mentor Application', 'There is a new Mentor Application! Please log into the admin site and review this application at your earliest convenience.', 'projectimpact919@gmail.com',
        ['projectimpact919@gmail.com'], fail_silently=False)
        return redirect('success')

def success(request):
    """View for a successful submission of a signup form"""
    view = 'success'
    return render(request, 'successful_submission.html')