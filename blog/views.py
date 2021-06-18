from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse

from .forms import PostCreateForm, PostUpdateForm
from .models import Post


@login_required
def create_post(request):
    form = PostCreateForm()
    context = {
        'form': form,
    }
    if request.method == 'POST':
        form = PostCreateForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('blog:list-post')
    return render(request, 'blog/create.html', context)


@login_required
def list_post(request):
    context = {
        'posts': Post.objects.all().order_by('-created_at')
    }
    return render(request, 'blog/list.html', context)


@login_required
def detail_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    context = {
        'post': post,
    }
    return render(request, 'blog/detail.html', context)


@login_required
def update_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = PostUpdateForm(instance=post)
    context = {
        'form': form,
    }
    if request.method == 'POST':
        form = PostUpdateForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect(reverse('blog:detail-post', kwargs={'pk': post.id}))
    return render(request, 'blog/update.html', context)


@login_required
def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    context = {
        'post': post,
    }
    if request.method == 'POST':
        instance = post
        post.delete()
        messages.success(request, f'{instance.title} deleted successfully')
        return redirect('blog:list-post')
    return render(request, 'blog/delete.html', context)