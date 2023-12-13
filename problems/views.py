from django.shortcuts import render

from .forms import ContactForm


def contact(request):
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(data=request.POST)
        print(form.data)
        # print(f"Title: {request.POST['title']}\n"
        #       f"Message: {request.POST['message']}\n"
        #       f"E-mail: {request.POST['email']}\n"
        #       f"Telephone: {request.POST['telephone']}\n")
    return render(
        request,
        "problems/contact.html",
        {"form": form}
    )

