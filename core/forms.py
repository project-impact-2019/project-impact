from django import forms
from .models import ResourcesPost
from .models import User

class ResourcesPostModelForm(forms.ModelForm):
    class Meta:
        model = ResourcesPost
        fields=['title', 'description', 'publish_date']
    
    def clean_title(self, *args, **kwargs):
        instance = self.instance
        title = self.cleaned_data.get('title')
        queryset = ResourcePost.objects.filter(title__iexact=title)
        if instance is not None:
            queryset = queryset.exclude(pk=instance.pk)
        if queryset.exists():
            raise forms.ValidationError('This title has already been used')
        return title



