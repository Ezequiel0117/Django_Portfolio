from django.shortcuts import render, get_object_or_404  #Intenta retornar un objeto si no una vista 404
from .models import Post
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def render_posts(request):
    posts = Post.objects.all()
    return render(request, 'posts.html', {'posts': posts})

@login_required
def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'post_detail.html', {"post": post})