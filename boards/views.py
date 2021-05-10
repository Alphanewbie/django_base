from boards.forms import PostForm
from boards.models import Post
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse

# Create your views here.
def index(request) :
    posts = Post.objects.all()
    context = {
        'posts' : posts,
    }
    return render(request, 'boards/index.html', context)

@login_required
@require_http_methods({'POST', 'GET'})
def insert(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('boards:index')
    else :
        form = PostForm()
    context = {
        'form' : form,
    }
    return render(request, 'boards/insert.html', context)

def detail(request, pk) :
    post = Post.objects.get(pk = pk)
    context = {
        'post' : post,
    }
    return render(request, 'boards/detail.html', context)

def get_all_post(request):
    posts = Post.objects.all()
    posts = posts.values('pk', 'user', 'title', 'content')
    context = {
        'posts' : list(posts),
    }
    return JsonResponse(context)