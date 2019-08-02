from django import forms
from .models import BlogPost, User, Questionnaire, Person, Category
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from phonenumber_field.formfields import PhoneNumberField
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()
from django.db import transaction

class BlogForm(forms.ModelForm):

    class Meta:
        model = BlogPost
        fields = ('title', 'content',)

class MentorSignUpForm(UserCreationForm):


    categories = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    email_address = forms.EmailField(max_length=254, help_text='Please enter a valid email address.')
    first_name = forms.CharField(max_length=120, help_text='Please enter your first name.')
    family_name = forms.CharField(max_length=120, help_text='Please enter your family name.')
    reference_name = forms.CharField(max_length=30, help_text='Please enter a professional reference.')
    reference_Phone = PhoneNumberField(help_text='Please enter your professional reference\'s phone number.')
    reference_name2 = forms.CharField(max_length=30, help_text='Please enter a personal reference name.')
    reference_phone2 = PhoneNumberField(help_text='Please enter your personal reference\'s phone number.')
    date_of_birth = forms.DateField(help_text='Please enter your date of birth. (i.e. YYYY-MM-DD)')
    why = forms.CharField(max_length=200, help_text='Please briefly describe why you want to become a foster mentor.')
    availabilty = forms.CharField(max_length=200, help_text='Please list the days and times you would be available to mentor.')
    address = forms.CharField(max_length=80, help_text='Please enter your full address')
    
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'first_name', 'date_of_birth')
    
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        date_of_birth=self.cleaned_data.get('date_of_birth')
        first_name=self.cleaned_data.get('first_name')
        family_name=self.cleaned_data.get('family_name')
        email_address=self.cleaned_data.get('email_address')
        why=self.cleaned_data.get('why')
        user.save()
        person = Person.objects.create(user=user, date_of_birth=date_of_birth, first_name=first_name, family_name=family_name, email_address=email_address)
        person.categories.add(*self.cleaned_data.get('categories'))
        person.role = 'mentor'
        person.save()
        return person

class MenteeSignUpForm(UserCreationForm):

    categories = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    email_address = forms.EmailField(max_length=254, help_text='Please enter a valid email address.')
    first_name = forms.CharField(max_length=120, help_text='Please enter your first name.')
    family_name = forms.CharField(max_length=120, help_text='Please enter your family name.')
    reference_name = forms.CharField(max_length=30, help_text='Please enter a professional reference.')
    reference_Phone = PhoneNumberField(help_text='Please enter your professional reference\'s phone number.')
    date_of_birth = forms.DateField(help_text='Please enter your date of birth. (i.e. YYYY-MM-DD)')

    class Meta:
        model = User
        fields = ('username',)
    
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.save()
        date_of_birth=self.cleaned_data.get('date_of_birth')
        first_name=self.cleaned_data.get('first_name')
        family_name=self.cleaned_data.get('family_name')
        email_address=self.cleaned_data.get('email_address')
        why=self.cleaned_data.get('why')
        person = Person.objects.create(user=user, date_of_birth=date_of_birth, first_name=first_name, family_name=family_name, email_address=email_address)
        person.categories.add(*self.cleaned_data.get('categories'))
        person.role = 'mentee'
        person.save()
        return person