from django.shortcuts import render
from core.models import BlogPost
from django.views import generic


def give_back(request):
    view = 'give_back'
    return render(request, 'give_back.html')

class BlogPostListView(generic.ListView):
    model = BlogPost
    paginate_by = 5

class BlogPostDetailView(generic.DetailView):
    model = BlogPost


# Create your views here.
