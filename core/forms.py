from django import forms
from .models import BlogPost, User
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from phonenumber_field.formfields import PhoneNumberField



class BlogForm(forms.ModelForm):

    class Meta:
        model = BlogPost
        fields = ('title', 'content',)

class MenteeSignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='*Please enter a valid email address.')
    name = forms.CharField(max_length=30, required=True, help_text='*Please enter your first and last name')
    reference_name = forms.CharField(max_length=30, required=True, help_text='*Please enter your foster home reference')
    reference_Phone = PhoneNumberField(required=True, help_text='*Please enter your reference\'s phone number')
    date_of_birth = forms.DateField()
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('name', 'email', 'date_of_birth', 'reference_name', 'reference_Phone',)

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_mentee = True
        user.save()
        return user