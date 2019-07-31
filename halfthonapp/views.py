from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from django.utils import timezone
from django.core.paginator import Paginator

from django.contrib.auth.models import User
from django.contrib import auth

def index(request) :
    if request.method == 'POST': 
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None: 
            auth.login(request, user)
            return redirect('index')
        else:
            return render(request, 'index.html', {'error': 'username or password is incorrect.'})
    else:
        blog = Blog.objects
        blog_list = Blog.objects.all()
        paginator = Paginator(blog_list, 18)
        page = request.GET.get('page')
        posts = paginator.get_page(page)
        return render(request, 'index.html', {'blog' : blog, 'posts':posts})
   
    return render(request, 'index.html', {'blog' : blog, 'posts':posts})

def detail(request, blog_id) :
    blog_detail = get_object_or_404(Blog, pk = blog_id)
    return render(request, 'detail.html', {'blog' : blog_detail })


def create(request) : 
    blog = Blog()
    blog.peername = request.GET['peername']
    blog.peercode = request.GET['peercode']
    blog.save()
    return redirect('/blog/'+str(blog.id))

def newpeer(request):
    return render(request,'newpeer.html')

def change(request):
    blog = Blog()
    
    return redirect('index')
