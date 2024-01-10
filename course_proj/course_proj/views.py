from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


def main_page(request):
    return render(request, "index.html")