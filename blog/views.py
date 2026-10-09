from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .forms import PostForm, RegistrationForm
from .models import Post


def post_list(request):
    posts = Post.objects.filter(status=Post.Status.PUBLISHED).select_related("author")
    query = request.GET.get("q", "").strip()
    tag = request.GET.get("tag", "").strip()

    if query:
        posts = posts.filter(Q(title__icontains=query) | Q(content__icontains=query))
    if tag:
        posts = posts.filter(tags__icontains=tag)

    return render(request, "blog/post_list.html", {
        "posts": posts,
        "query": query,
        "tag": tag,
    })


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.status != Post.Status.PUBLISHED and (
        not request.user.is_authenticated or
        (request.user != post.author and not request.user.is_staff)
    ):
        # No revelar si un borrador/archivado existe a usuarios sin permiso.
        from django.http import Http404
        raise Http404("La publicación no existe.")
    return render(request, "blog/post_detail.html", {"post": post})


@login_required
def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, "La publicación se guardó correctamente.")
            return redirect(post.get_absolute_url())
    else:
        form = PostForm()
    return render(request, "blog/post_form.html", {"form": form, "heading": "Nueva publicación"})


@login_required
def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.author_id != request.user.id and not request.user.is_staff:
        from django.core.exceptions import PermissionDenied
        raise PermissionDenied
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, "La publicación se actualizó correctamente.")
            return redirect(post.get_absolute_url())
    else:
        form = PostForm(instance=post)
    return render(request, "blog/post_form.html", {"form": form, "heading": "Editar publicación"})


@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.author_id != request.user.id and not request.user.is_staff:
        from django.core.exceptions import PermissionDenied
        raise PermissionDenied
    if request.method == "POST":
        post.delete()
        messages.success(request, "La publicación se eliminó correctamente.")
        return redirect("post_list")
    return render(request, "blog/post_confirm_delete.html", {"post": post})


def register(request):
    if request.user.is_authenticated:
        return redirect("post_list")
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Tu cuenta se creó correctamente.")
            return redirect("post_list")
    else:
        form = RegistrationForm()
    return render(request, "registration/register.html", {"form": form})
