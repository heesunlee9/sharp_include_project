from django.http import HttpResponse


def index(request):
    return HttpResponse("#include Project: "
                        "Online, Live Computing Education Service for the Underprivileged. "
                        "Contact: jl8867@rit.edu")

