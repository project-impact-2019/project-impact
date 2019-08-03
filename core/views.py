from django.shortcuts import render, redirect
from core.models import User, Forum, Comment, Category, Resource, BlogPost, Person, Pair
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

# Twilio Chat
from faker import Factory
from django.http import JsonResponse
from django.conf import settings
from twilio.rest import Client
from twilio.jwt.access_token import AccessToken
from twilio.jwt.access_token.grants import (
    SyncGrant,
    ChatGrant
)


# Views Created Here
def index(request):
    """View function for home page of site."""
    """ If user is connect with profile page """
    
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


#Profile
def user_profile(request, user_id):
    user = User.objects.get(pk=user_id)
  
    context={
        'user': user,
    
    }
    return render(request, 'core/user_profile.html', context)
   

# Twilio Chat

def app(request):
    return render(request, 'twilio/chat.html')

def token(request):
    fake = Factory.create()
    return generateToken(fake.user_name())

def generateToken(identity):
    # Get credentials from environment variables
    account_sid      = settings.TWILIO_ACCT_SID
    chat_service_sid = settings.TWILIO_CHAT_SID
    sync_service_sid = settings.TWILIO_SYNC_SID
    api_sid          = settings.TWILIO_API_SID
    api_secret       = settings.TWILIO_API_SECRET

# Create access token with credentials
    token = AccessToken(account_sid, api_sid, api_secret, identity=identity)

 # Create a Sync grant and add to token
    if sync_service_sid:
        sync_grant = SyncGrant(service_sid=sync_service_sid)
        token.add_grant(sync_grant)

# Return token info as JSON
    return JsonResponse({'identity':identity,'token':token.to_jwt().decode('utf-8')})


@login_required
def create_pair(request):
    from core.forms import PairForm
    from django.views.generic.edit import CreateView
    if request.method == "POST":
        form = PairForm(request.POST)
        if form.is_valid():
            # blog = form.save(commit=False)
            form.save()
            return redirect('index')
    else:
        form = PairForm()
    return render(request, 'core/new_pair_form.html', {'form': form})