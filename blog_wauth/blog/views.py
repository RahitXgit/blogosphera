from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from .models import Post
from .forms import PostForm
# Create your views here.
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username = username, password  = password)
        if user is not None:
            login(request,user)
            return redirect('blog-home')
    return render(request, 'blog/login.html')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'blog/register.html', {'form': form})


def home_view(request):
    posts = Post.objects.all()
    return render(request, 'blog/home.html', {'posts': posts})
    
def create_post_view(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('blog-home')
    else:
        form = PostForm()
        
    return render(request, 'blog/create_post.html', {'form': form})

def post_detail_view(request, post_id):
    print("Post ID: ", post_id)
    post = get_object_or_404(Post, id=post_id)
    print("Post Retrieved: ", post)
    return render(request, 'blog/post_detail.html', {'post':post})