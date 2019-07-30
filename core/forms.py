from django import forms
from core.models import BlogPost

class BlogForm(forms.ModelForm):

    class Meta:
        model = BlogPost
        fields = ('title', 'content',)