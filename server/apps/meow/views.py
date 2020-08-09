from django.shortcuts import render


def start_task(request):
    return render(request, "index.html", {})
