from django import forms
from .models import BlogPost, User, Questionnaire, Person, Category, Pair
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
        required=True,
        help_text='Please select the categories you are interesting in mentoring.'
    )

    # email_address = forms.EmailField(max_length=254, help_text='Please enter a valid email address.')
    first_name = forms.CharField(max_length=120, help_text='Please enter your first name.')
    family_name = forms.CharField(max_length=120, help_text='Please enter your family name.')
    reference_name = forms.CharField(max_length=30, help_text='Please enter a professional reference.')
    reference_phone = PhoneNumberField(max_length=15, help_text='Please enter your professional reference\'s phone number.')
    reference_name2 = forms.CharField(max_length=30, help_text='Please enter a personal reference name.')
    reference_phone2 = PhoneNumberField(max_length=15, help_text='Please enter your personal reference\'s phone number.')
    date_of_birth = forms.DateField(help_text='Please enter your date of birth. (Format: MM-DD-YYYY or YYYY-MM-DD)')
    why = forms.CharField(max_length=200,widget=forms.Textarea, help_text='Please briefly describe why you want to become a foster mentor.')
    availability = forms.CharField(max_length=200,widget=forms.Textarea, help_text='Please list the days and times you would be available to mentor.')
    address = forms.CharField(max_length=80,widget=forms.Textarea, help_text='Please enter your full address.')
    
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'first_name', 'family_name', 'email_address', 'date_of_birth', 'education')
    
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password1')
        education = self.cleaned_data.get('education')
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
        user = User.objects.create(username=username,first_name=first_name, family_name=family_name, email_address=email_address, why=why, reference_name=reference_name, reference_phone=reference_phone, reference_name2=reference_name2, reference_phone2=reference_phone2, availability=availability, address=address, education=education)
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
        required=True,
        help_text='Please select the categories you would like help with from a Mentor.'
    )

    email_address = forms.EmailField(max_length=254, help_text='Please enter a valid email address.')
    first_name = forms.CharField(max_length=120, help_text='Please enter your first name.')
    family_name = forms.CharField(max_length=120, help_text='Please enter your family name.')
    reference_name = forms.CharField(max_length=30, help_text='Please enter your foster home reference name. (i.e. Foster Parent, Social Worker, etc.)')
    reference_phone = PhoneNumberField(max_length=15, help_text='Please enter your reference\'s phone number.')
    date_of_birth = forms.DateField(help_text='Please enter your date of birth. (i.e. YYYY-MM-DD)')

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'first_name', 'family_name', 'email_address', 'date_of_birth',)
    
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
        user = User.objects.create(username=username, first_name=first_name, family_name=family_name, email_address=email_address, reference_name=reference_name, reference_phone=reference_phone)
        user.set_password(password)
        user.save()
        person = Person.objects.create(user=user, date_of_birth=date_of_birth, first_name=first_name, family_name=family_name, email_address=email_address)
        person.categories.add(*self.cleaned_data.get('categories'))
        person.role = 'mentee'
        person.save()
        return person

class PairForm(forms.ModelForm):
    class Meta:
        model = Pair
        fields = ('mentee', 'mentor',)

    def __init__(self, *args, **kwargs):
        super(PairForm, self).__init__(*args, **kwargs)
        self.fields['mentee'].queryset = Person.objects.filter(role='mentee')
        self.fields['mentor'].queryset = Person.objects.filter(role='mentor')
    