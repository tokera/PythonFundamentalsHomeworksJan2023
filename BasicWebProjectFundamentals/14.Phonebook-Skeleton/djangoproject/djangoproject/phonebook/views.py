from django.shortcuts import render, redirect

from djangoproject.phonebook.models import Contact


def landing_page(request):
    context = {
        "contacts": Contact.objects.all(),
    }
    return render(request, "phonebook/index.html")


def create_contact(request):
    name = request.POST["name"]
    number = request.POST["number"]
    contact = Contact(
        name=name,
        number=number
    )
    contact.save()
    return redirect("landing-page")
