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
from core import views

urlpatterns = [
    # Django Registration Redux
    path('accounts/', include('registration.backends.admin_approval.urls')),
    path('admin/', admin.site.urls),
    path('blog/', views.BlogPostListView.as_view(), name='blog'),
    path('blog/<int:pk>', views.BlogPostDetailView.as_view(), name='blog-detail'),
    path('give_back/', views.give_back, name='give_back'),
]

# Django Debug Toolbar
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

    ] + urlpatterns
