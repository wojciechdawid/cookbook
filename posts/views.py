from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import Post
from .services import PostService as service


def display_post(request) -> HttpResponse:
    return render(
        request,
        "posts/display_post.html",
        {"posts": Post.objects.filter(published=True)}
    )


@login_required
def add_post(request) -> HttpResponse:
    if request.method == "POST":
        title = request.POST.get("post_title")
        content = request.POST.get("post_content")
        author = request.user
        Post.objects.create(
            title=title,
            content=content,
            author=author,
            published=bool(request.POST.get("post_published"))
        )
        return redirect("posts:display_post")

    return render(
        request,
        "posts/add_post.html",
        {}
    )

def post_details(request, id: int) -> HttpResponse:
    return render(
        request,
        "posts/post_details.html",
        {"post_details": Post.objects.get(id=id)}
    )