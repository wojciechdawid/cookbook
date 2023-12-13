from django import forms


class PostForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField(widget=forms.Textarea)
    email = forms.EmailField()
    published = forms.BooleanField(required=False)
