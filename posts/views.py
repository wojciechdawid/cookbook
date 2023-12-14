from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import PostForm, PostForm2
from .models import Post, Comment
from .services import PostService as service


def display_post(request) -> HttpResponse:
    return render(
        request,
        "posts/display_post.html",
        {"posts": Post.objects.filter(published=True)}
    )


@login_required
def add_post(request) -> HttpResponse:

    form = PostForm2()

    if request.method == "POST":
        form = PostForm2(data=request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published = False
            post.save()
            messages.add_message(request, messages.INFO, "Post utworzony")


        # title = request.POST.get("title")
        # content = request.POST.get("content")
        # author = request.user
        # Post.objects.create(
        #     title=title,
        #     content=content,
        #     author=author,
        #     published=bool(request.POST.get("published"))
        # )
        return redirect("posts:display_post")

    return render(
        request,
        "posts/add_post.html",
        {"form": form}
    )


def post_details(request, id: int) -> HttpResponse:
    if request.method == "POST":
        author = request.user
        text = request.POST.get("comment_text")
        Comment.objects.create(
            # post=Post.objects.get(id=id),
            post_id=id,
            author=author,
            text=text
        )

    return render(
        request,
        "posts/post_details.html",
        {"post_details": Post.objects.get(id=id)}
    )
