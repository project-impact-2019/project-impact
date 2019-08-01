from django import forms
from .models import BlogPost, User, Questionnaire
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from phonenumber_field.formfields import PhoneNumberField

class BlogForm(forms.ModelForm):

    class Meta:
        model = BlogPost
        fields = ('title', 'content',)

