from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.conf import settings
from django.urls import reverse
from .utils import unique_slug_generator

# Models created here.
class User(AbstractUser):
    """Model Representing a User"""

    is_mentee = models.BooleanField('mentee status', default=False)
    is_mentor = models.BooleanField('mentor status', default=False)


class Forum(models.Model):
    """ Model Representing a Forum """

    title = models.CharField(max_length=120)
    description = models.TextField(max_length=500)
    date_posted = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)


class Comment(models.Model):
    """Model representing a comment to a forum post."""
    
    comment = models.TextField(max_length=200, help_text='Enter a comment here')
    date_posted = models.DateTimeField(auto_now_add=True)
    target_post = models.ForeignKey(Forum, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-date_posted']

    def __str__(self):
        """String for representing the Model object."""
        return self.comment                             
                            


class VisionBoard(models.Model):
    """Model representing the vision board for mentees"""
    goals = models.TextField(max_length=500)
    
    

class Category(models.Model):
    """Model representing to identify the category for resource content."""
    name = models.CharField(max_length=200, help_text='Enter a resource category (e.g. Educational, Career)')
    
    def __str__(self):
        """String for representing the Model object."""
        return self.name

    class Meta:
        verbose_name_plural = 'categories'


class ResourcesPost(models.Model):
    """ Model Representing a resource. """

    title = models.CharField(max_length=120)
    description = models.TextField()
    publish_date = models.DateTimeField(auto_now_add=True)
    url_address = models.URLField(max_length=200, unique=True, help_text='Enter the url for this resource')
    category = models.ManyToManyField(Category, help_text='Select a category for this resource')
    
    
    def get_absolute_url(self):
         return reverse('resources-detail', args=[str(self.id)])

    def __str__(self):              
        return self.title


class BlogPost(models.Model):
    """ Model representing a blog post."""
    title    = models.CharField(max_length= 100)
    content  = models.TextField(null=True, blank=True)
    publish_date = models.DateTimeField(auto_now_add= True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-publish_date']

    def __str__(self):              
        return self.title

    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('blog-detail', args=[str(self.id)])

    

class ProgressTracker(models.Model):
    """Model representing the progress tracker."""
    activity = models.CharField(max_length=200, help_text="What activity are you performing?")
    completed = models.BooleanField(default=False)

    def __str__(self):              
        return self.activity

