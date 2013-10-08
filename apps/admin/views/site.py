from django.shortcuts import render


def home(request):
    "Render site home page"
    return render(request, "home.html")
