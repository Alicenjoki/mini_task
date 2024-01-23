from django.shortcuts import render,redirect
from .models import *
from .forms import CreateBlogForm

# Create your views here.
def home(request ):
    posts = Post.objects.all()

    context ={
        'posts':posts,
        'post':post,
    }
    return render(request, 'pages/home.html', context)

def post(request, uuid):
    post = Post.objects.get(id = uuid)

    context ={
        'post':post,
    }
    return render(request, 'pages/post.html', context)

def create_post(request):
    if request.method == 'POST':
        form = CreateBlogForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            # instance.user = request.user
            instance.save()
            return redirect('home')
        else:
            print(form.errors)
            return redirect('create_post')
    else:
        form = CreateBlogForm()

    context ={
        'form' :form,
    }
    return render(request, 'pages/create_post.html', context)

def edit(request, uuid):
    post = Post.objects.get(id=uuid)
    print('bet')
    if request.method == 'POST':
        print('post')
        form = CreateBlogForm(request.POST, request.FILES ,instance=post)
        if form.is_valid():
            form.save()
            print('sure')
            return redirect('post', uuid)  #post.id
        else:
            # print(form.errors)
            print('me')
            return redirect('post', post.id)
    else:
        form= CreateBlogForm(instance=post)

    context={
        'post':post,
        'form':form,
    }
    return render(request, 'pages/edit.html', context)

def delete(request, uuid):
    post = Post.objects.get(id=uuid)
    if request.method == 'POST':
        post.delete()
        return redirect('home')
    
    context={
        'post':post,
    }
    return render(request, 'pages/delete.html', context)