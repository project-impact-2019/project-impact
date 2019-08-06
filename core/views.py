from django.views.generic.base import TemplateView
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods, require_POST
from django.views.generic.base import TemplateView
from core.models import User, Forum, Comment, Category, Resource, BlogPost, Person, Pair, Goal, Chat
import json
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.views.generic import CreateView
from core.filters import BlogPostFilter, ResourceFilter
from core.forms import MenteeSignUpForm, MentorSignUpForm, GoalForm
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.http import HttpResponse
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
            blog.author = request.user.person
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



def user_profile(request, user_id):
    user = User.objects.get(pk=user_id)
    person = Person.objects.get(user=request.user)
    goals_by_user = Goal.objects.filter(person=person)
    context={
        'user': user,
        'goals_by_user': goals_by_user,
    }
    return render(request, 'core/user_profile.html', context)
   

# Twilio Chat

def chatrooms(request):
    chatrooms = Chat.objects.all()
    return render(request, 'twilio/chatrooms.html', {'chatrooms': chatrooms})

def chatroom_detail(request, slug):
    chatroom = Chat.objects.get(slug=slug)
    return render(request, 'twilio/chatroom_detail.html', {'chatroom': chatroom})

def app(request):
    return render(request, 'twilio/chat.html')

@login_required
def token(request):
    username = None
    if request.user.is_authenticated:
        username = request.user.get_username()
    return generateToken(username)

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

    # Create a Chat grant and add to token
    if chat_service_sid:
        chat_grant = ChatGrant(service_sid=chat_service_sid)
        token.add_grant(chat_grant)

    # Return token info as JSON
    return JsonResponse({'identity':identity,'token':token.to_jwt().decode('utf-8')})


@login_required
def create_pair(request):
    if request.user.is_superuser or request.user.is_admin:
        from core.forms import PairForm
        from django.views.generic.edit import CreateView
        if request.method == "POST":
            form = PairForm(request.POST)
            chatrooms = Chat.objects.all()
            if form.is_valid():
                # blog = form.save(commit=False)
                form.save()
                return redirect('index')
        else:
            chatrooms = Chat.objects.all()
            form = PairForm()
        return render(request, 'core/new_pair_form.html', {'form': form, 'chatrooms': chatrooms})
    else:
        return redirect('index')


class PairListView(generic.ListView):
    """View for Pair List"""
    model = Pair

#Goal Views

# class GoalListView(generic.ListView):
#     """View for Goal List"""
#     model = Goal

def goal_list_view(request):
    person = Person.objects.get(user=request.user)
    goals_by_user = Goal.objects.filter(person=person)
    context={
        'goals_by_user': goals_by_user,
    }
    return render(request, 'core/user_profile.html', context=context)

@login_required
def add_new_goal(request):
    print('goal')
    from core.forms import GoalForm
    from django.views.generic.edit import CreateView
    if request.method == "POST":
        form = GoalForm(request.POST)
        if form.is_valid():
            goal = form.save(commit=False)
            goal.person = Person.objects.get(user=request.user)
            form.save()
    else:
        form = GoalForm()
    return HttpResponse()

@login_required
def add_new_step(request, pk):
    print('step')
    from core.forms import StepForm
    from django.views.generic.edit import CreateView
    if request.method == "POST":
        form = StepForm(request.POST)
        if form.is_valid():
            step = form.save(commit=False)
            step.person = Person.objects.get(user=request.user)
            step.goal = get_object_or_404(Goal, pk=pk)
            form.save()
    else:
        form = StepForm()
    return HttpResponse()

# class UserProfileView(generic.ListView):
#     model = Goal
#     template_name = 'core/user_profile.html'

#     def get_queryset(self):
#         """
#         Return list of Goal objects created by Person (owner id specified in URL)
#         """
#         id = self.kwargs['pk']
#         target_person = Person.objects.get(user=request.user)
#         return Goal.objects.filter(person=target_person)

#     def get_context_data(self, **kwargs):
#         """
#         Add goal owner to context so they can be displayed in the template
#         """
#         # Call the base implementation first to get a context
#         context = super(UserProfileView, self).get_context_data(**kwargs)
#         # Get the owner object from the "pk" URL parameter and add it to the context
#         context['person'] = Person.objects.get(user=request.user)
#         return context