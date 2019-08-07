"""project_impact URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import include, url
from django.urls import path, include
from django.conf import settings
from django.views.generic import RedirectView
from core import views as core_views
from django.urls import re_path
from django.conf.urls import handler404


urlpatterns = [
    # Index
    path('', core_views.index, name='index'), 
    path('', RedirectView.as_view(url='/index/', permanent=True)),
    path('profile/<int:user_id>', core_views.user_profile, name='profile'),
    
    # How to Give Back to Foster Community
    path('giveback/', core_views.give_back, name='give_back'),
    
    # Blog List and Blog Detail
    path('blog/', core_views.BlogPostListView.as_view(), name='blog'),
    path('blog/<int:pk>', core_views.BlogPostDetailView.as_view(), name='blog-detail'),

    # Resource List and Resource Detail
    path('resource/', core_views.ResourceListView.as_view(), name='resource'),
    path('resource/<int:pk>', core_views.ResourceDetailView.as_view(), name='resource-detail'),

    # Search Results
    path('resource/search', core_views.search_resource, name = 'search_resource'),
    path('blog/search', core_views.search_blog, name = 'search_blog'),

    # Django Registration Redux
    path('accounts/', include('registration.backends.admin_approval.urls')),
    path('admin/', admin.site.urls),

    # Forms
    path('newblog/', core_views.add_new_blog, name='add_new_blog'),
    path('newpair/', core_views.create_pair, name='create_pair'),
    path('newchat/', core_views.create_chat, name='create_chat'),

    # Success URLs
    path('pair_created/', core_views.pair_created, name='pair_created'),
    path('chat_created/', core_views.chat_created, name='chat_created'),

    #  New Account Sign Up
    path('accounts/signup/mentee/', core_views.MenteeSignUpView.as_view(), name='mentee_signup'),
    path('accounts/signup/mentor/', core_views.MentorSignUpView.as_view(), name='mentor_signup'),
    path('success/', core_views.success, name='success'),


    #Goal
    path('goal/', core_views.goal_list_view, name='user-profile'),
    path('goal/add', core_views.add_new_goal, name='add_goal'),
    path('goal/add_step/<int:pk>', core_views.add_new_step, name='add_step'),
    path('profile/goal/check_mark/<int:pk>/', core_views.check_mark, name='check_mark'),
  
   
    # Chat app
    path(r'', include('core.urls')),

]

# Handler for 404 View
handler404 = 'core.views.handler404'

# Django Debug Toolbar
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

    ] + urlpatterns

