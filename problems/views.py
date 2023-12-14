from django.shortcuts import render

from .forms import ContactForm, ContactForm2
from .models import Problem


def contact(request):
    if request.method == "POST":
        form = ContactForm2(data=request.POST)
        if form.is_valid():
            # Problem.objects.create(**form.cleaned_data)
            # print("Created")
            form.save()

    form = ContactForm2()
    return render(
        request,
        "problems/contact.html",
        {"form": form}
    )


def update_problem(request, id: int):
    pr = Problem.objects.get(id=id)

    if request.method == "POST":
        form = ContactForm2(instance=pr, data=request.POST)
        if form.is_valid():
            form.save()
            print("Zaktualizowane")

    form = ContactForm2(instance=pr)
    return render(
        request,
        "problems/contact.html",
        {"form": form,
         "problems": Problem.objects.all()}
    )