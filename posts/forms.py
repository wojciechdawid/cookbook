from django import forms

from .models import Post


class PostForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField(widget=forms.Textarea)
    email = forms.EmailField()
    published = forms.BooleanField(required=False)


class PostForm2(forms.ModelForm):

    class Meta:
        model = Post
        fields = ["title", "content"]