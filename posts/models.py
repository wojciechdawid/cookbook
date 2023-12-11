from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published = models.BooleanField()
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True, related_name="comments")
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return self.text[:10] + "..."
