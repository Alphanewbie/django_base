from boards.forms import PostForm
from boards.models import Post
from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods

# Create your views here.
def index(request) :
    return render(request, 'boards/index.html')

@require_http_methods({'POST', 'GET'})
def insert(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
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