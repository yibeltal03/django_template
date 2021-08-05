from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Blogs

# Create your views here.
def all_blogs(request):
    blogs = Blogs.objects.all()
    return render(request, 'blog.html',{'blogs':blogs}) 

def detail(request, blog_id):
    blog = get_object_or_404(Blogs, pk=blog_id)
    return render(request,'detail.html', {'blog':blog})