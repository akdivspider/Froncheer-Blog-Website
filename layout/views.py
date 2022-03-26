from django.shortcuts import render
from layout.models import Topic 

from layout.models import Heading

# Create your views here.
def about(request):
    return render(request, 'about.html')
def blog(request):
    return render(request, 'blog.html')

def gallery(request):

    headings = Heading.objects.all()
    topics = Topic.objects.all()
    
    return render(request, 'gallery.html', {'headings':headings, 'topics':topics},)