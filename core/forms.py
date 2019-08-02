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
    reference_phone = PhoneNumberField(help_text='Please enter your professional reference\'s phone number.')
    reference_name2 = forms.CharField(max_length=30, help_text='Please enter a personal reference name.')
    reference_phone2 = PhoneNumberField(help_text='Please enter your personal reference\'s phone number.')
    date_of_birth = forms.DateField(help_text='Please enter your date of birth. (i.e. YYYY-MM-DD)')
    why = forms.CharField(max_length=200,widget=forms.Textarea, help_text='Please briefly describe why you want to become a foster mentor.')
    availability = forms.CharField(max_length=200,widget=forms.Textarea, help_text='Please list the days and times you would be available to mentor.')
    address = forms.CharField(max_length=80,widget=forms.Textarea, help_text='Please enter your full address')
    
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'first_name', 'date_of_birth')
    
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password1')
        date_of_birth=self.cleaned_data.get('date_of_birth')
        first_name=self.cleaned_data.get('first_name')
        family_name=self.cleaned_data.get('family_name')
        email_address=self.cleaned_data.get('email_address')
        reference_name=self.cleaned_data.get('reference_name')
        reference_phone=self.cleaned_data.get('reference_phone')
        reference_name2=self.cleaned_data.get('reference_name2')
        reference_phone2=self.cleaned_data.get('reference_phone2')
        availability=self.cleaned_data.get('availability')
        address=self.cleaned_data.get('address')
        why=self.cleaned_data.get('why')
        user = User.objects.create(username=username,first_name=first_name, family_name=family_name, email_address=email_address, why=why, reference_name=reference_name, reference_Phone=reference_Phone, reference_name2=reference_name2, reference_phone2=reference_phone2, availability=availability, address=address)
        user.set_password(password)
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
    reference_name = forms.CharField(max_length=30, help_text='Please enter your fosterhome reference name.')
    reference_Phone = PhoneNumberField(help_text='Please enter your reference\'s phone number.')
    date_of_birth = forms.DateField(help_text='Please enter your date of birth. (i.e. YYYY-MM-DD)')

    class Meta:
        model = User
        fields = ('username',)
    
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password1')
        date_of_birth=self.cleaned_data.get('date_of_birth')
        first_name=self.cleaned_data.get('first_name')
        family_name=self.cleaned_data.get('family_name')
        email_address=self.cleaned_data.get('email_address')
        reference_name=self.cleaned_data.get('reference_name')
        reference_phone=self.cleaned_data.get('reference_phone')
        user = User.objects.create(username=username, first_name=first_name, family_name=family_name, email_address=email_address, reference_name=reference_name, reference_Phone=reference_Phone)
        user.set_password(password)
        user.save()
        person = Person.objects.create(user=user, date_of_birth=date_of_birth, first_name=first_name, family_name=family_name, email_address=email_address)
        person.categories.add(*self.cleaned_data.get('categories'))
        person.role = 'mentee'
        person.save()
        return person