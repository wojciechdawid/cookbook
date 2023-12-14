from django import forms

from .models import Problem


class ContactForm(forms.Form):
    name = forms.CharField()
    title = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)
    email = forms.EmailField()
    telephone = forms.RegexField(regex="\d{9}")

    # def clean_name(self):
    #     data = self.cleaned_data["name"]
    #     return data.capitalize()
    #
    # def clean_email(self):
    #     email = self.cleaned_data["email"]
    #     return email.lower()

    def clean(self):
        data = self.cleaned_data
        data["name"] = data["name"].capitalize()
        data["email"] = data["email"].lower()
        return data


class ContactForm2(forms.ModelForm):
    def clean(self):
        data = self.cleaned_data
        data["name"] = data["name"].capitalize()
        data["email"] = data["email"].lower()
        return data

    class Meta:
        model = Problem
        exclude = ["done"]
