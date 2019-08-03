from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.conf import settings
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from phonenumber_field.modelfields import PhoneNumberField
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.db.models import Q
from django.core.mail import send_mail

MENTOR = 'mentor'
MENTEE = 'mentee'

USER_TYPE_CHOICES = (
    (MENTOR, 'mentor'),
    (MENTEE, 'mentee'),
)


# Models created here.
class User(AbstractUser):
    """Model Representing a User"""
    is_admin = models.BooleanField('admin status', default=False)
    is_paired = models.BooleanField('paired status', default=False)
    is_active = models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)
    first_name = models.CharField(blank=True, max_length=120, help_text='Please enter your first name.')
    family_name = models.CharField(blank=True, max_length=120, help_text='Please enter your family name.')
    email_address = models.EmailField(blank=True, max_length=254, help_text='Please enter a valid email address.')
    why = models.TextField(blank=True, max_length=200, help_text='Please briefly describe why you want to become a foster mentor.')
    availability = models.TextField(blank=True, max_length=200, help_text='Please list the days and times you would be available to mentor.')
    address = models.CharField(blank=True, max_length=80, help_text='Please enter your full address')
    reference_name = models.CharField(blank=True, max_length=30, help_text='Please enter a professional reference.')
    reference_phone = PhoneNumberField(blank=True, help_text='Please enter your professional reference\'s phone number.')
    reference_name2 = models.CharField(blank=True, max_length=30, help_text='Please enter a personal reference name.')
    reference_phone2 = PhoneNumberField(blank=True, help_text='Please enter your personal reference\'s phone number.')
    # date_of_birth = models.DateField(help_text='Please enter your date of birth. (i.e. YYYY-MM-DD)')
    
    HIGH_SCHOOL_GED = 'High School / GED'
    SOME_COLLEGE = 'Some College'
    ASSOCIATES_DEGREE = 'Associate\'s Degree'
    BACHELORS_DEGREE = 'Bachelor\'s Degree'
    MASTERS_DEGREE = 'Masters\' Degree'
    PHD = 'PhD'
    NONE = 'None'

    EDUCATION_CHOICES = [
        (HIGH_SCHOOL_GED, 'High School / GED'),
        (SOME_COLLEGE, 'Some College'),
        (ASSOCIATES_DEGREE, 'Associate\'s Degree'),
        (BACHELORS_DEGREE, 'Bachelor\'s Degree'),
        (MASTERS_DEGREE, 'Master\'s Degree'),
        (PHD, 'PhD'),
        (NONE, 'None'),
    ]

    education = models.CharField(
        help_text='Please enter your highest level of education.',
        max_length=30,
        choices=EDUCATION_CHOICES,
        default=NONE
    )

    def save (self, *args, **kwargs):
        if self.is_superuser: self.is_active=True
        return super().save(*args, **kwargs)

    def save (self, *args, **kwargs):
    # Only when we update an element. Not when we create it
        if self.pk:
        # We get the old values of the model
            old = User.objects.get(pk=self.pk)
        # If it's approved and it wasn't before
            if self.is_active == True and old.is_active == False:
                send_mail('Account Activation', 'Congrats, your Project Impact account is now active! You may log in now.', 'projectimpact919@gmail.com',
                [self.email_address], fail_silently=False)
        super(User, self).save(*args, **kwargs)


class Category(models.Model):
    """Model representing to identify the category for resource content."""
    name = models.CharField(max_length=200, help_text='Enter a resource category (e.g. Educational, Career)')
    parent = models.ForeignKey('self',blank=True, null=True, related_name='children', on_delete=models.CASCADE)

    def __str__(self):
        """String for representing the Model object."""
        return self.name

    class Meta:
        verbose_name_plural = 'categories'



class Person(models.Model):
    """Model Representing a Person"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=120, help_text='Please enter your first name.')
    family_name = models.CharField(max_length=120, help_text='Please enter your family name.')
    date_of_birth = models.DateField(help_text='Please enter your date of birth. (i.e. YYYY-MM-DD)')
    email_address = models.EmailField(max_length=254, help_text='Please enter a valid email address.')
    categories = models.ManyToManyField(Category)
    # pairs = models.ManyToManyField('self', through='Pair', symmetrical=False)
    role = models.CharField(max_length=100,  choices=USER_TYPE_CHOICES)

    def __str__(self):
      """Returns human-readable representation of the model instance."""
      return self.first_name

    @property
    def pairs(person):
        pairs = Pair.objects.filter(Q(mentor=person)|Q(mentee=person))
        return pairs


class Pair(models.Model):
    """ Model representing the pair of a mentor and mentee """
    mentor = models.ForeignKey(Person, related_name='mentor', on_delete=models.PROTECT)
    mentee = models.ForeignKey(Person, related_name='mentee', on_delete=models.PROTECT)

    def __str__(self):
        """Returns human-readable representation of the model instance."""
        return f"{self.mentor} - {self.mentee}"


class Chat(models.Model):
    """ Model representing the chat functionality for a pair """
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    slug = models.CharField(max_length=50)
    pair = models.ForeignKey(Pair, on_delete=models.CASCADE)

    def __str__(self):
        """Returns human-readable representation of the model instance."""
        return self.name


class Forum(models.Model):
    """ Model Representing a Forum """
    title = models.CharField(max_length=120)
    description = models.TextField(max_length=500)
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Person, on_delete=models.CASCADE)


class Comment(models.Model):
    """Model representing a comment to a forum post."""
    comment = models.TextField(max_length=200, help_text='Enter a comment here')
    date_posted = models.DateTimeField(auto_now_add=True)
    target_post = models.ForeignKey(Forum, on_delete=models.CASCADE, null=True)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-date_posted']

    def __str__(self):
        """String for representing the Model object."""
        return self.comment                             


class Goal(models.Model):
    """Model representing the goal board."""
    name = models.TextField(max_length=255 )
    pair = models.ForeignKey(Pair, on_delete=models.CASCADE)
    how_to_achieve = models.TextField(max_length=500)
    completed = models.BooleanField(default=False)

    def __str__(self):
        """String for representing the Model object."""
        return self.name


class Resource(models.Model):
    """ Model Representing a resource. """

    title = models.CharField(max_length=120)
    description = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    url_address = models.URLField(max_length=200, unique=True, help_text='Enter the url for this resource')
    category = models.ForeignKey(Category, help_text='Select a category for this resource', on_delete=models.CASCADE)


    def __str__(self):              
        return self.title

    def get_absolute_url(self):
        """Returns the url to access a detail record for this resource."""
        return reverse('resource-detail', args=[str(self.id)])


class BlogPost(models.Model):
    """ Model representing a blog post."""
    title    = models.CharField(max_length= 100)
    content  = models.TextField(null=True, blank=True)
    publish_date = models.DateTimeField(auto_now_add= True)
    author = models.ForeignKey(Person, on_delete=models.PROTECT)

    class Meta:
        ordering = ['-publish_date']

    def __str__(self):              
        return self.title
    
    def get_absolute_url(self):
        """Returns the url to access a detail record for this blog."""
        return reverse('blog-detail', args=[str(self.id)])


    
class Questionnaire(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE, primary_key=True)
    email = models.EmailField(max_length=254, help_text='Please enter a valid email address.')
    first_name = models.CharField(max_length=120, help_text='Please enter your first name.')
    family_name = models.CharField(max_length=120, help_text='Please enter your family name.')
    reference_name = models.CharField(max_length=30, null=False, help_text='Please enter a professional reference.')
    reference_phone = PhoneNumberField(null=False, help_text='Please enter your professional reference\'s phone number.')
    reference_name2 = models.CharField(max_length=30, null=False, help_text='Please enter a personal reference name.')
    reference_phone2 = PhoneNumberField(null=False, help_text='Please enter your personal reference\'s phone number.')
    date_of_birth = models.DateField(null=False, help_text='Please enter your date of birth. (i.e. YYYY-MM-DD)')
    category = models.ManyToManyField(Category, blank=True, help_text='Please select a skill speciality.')
    why = models.TextField(null=False, max_length=200, help_text='Please briefly describe why you want to become a foster mentor.')
    availabilty = models.TextField(null=False, max_length=200, help_text='Please list the days and times you would be available to mentor.')
    address = models.CharField(null=False, max_length=80, help_text='Please enter your full address')
    

    HIGH_SCHOOL_GED = 'High School / GED'
    SOME_COLLEGE = 'Some College'
    ASSOCIATES_DEGREE = 'Associate\'s Degree'
    BACHELORS_DEGREE = 'Bachelor\'s Degree'
    MASTERS_DEGREE = 'Masters\' Degree'
    PHD = 'PhD'
    NONE = 'None'

    EDUCATION_CHOICES = [
        (HIGH_SCHOOL_GED, 'High School / GED'),
        (SOME_COLLEGE, 'Some College'),
        (ASSOCIATES_DEGREE, 'Associate\'s Degree'),
        (BACHELORS_DEGREE, 'Bachelor\'s Degree'),
        (MASTERS_DEGREE, 'Master\'s Degree'),
        (PHD, 'PhD'),
        (NONE, 'None'),
    ]

    education = models.CharField(
        max_length=30,
        choices=EDUCATION_CHOICES,
        default=NONE
    )


