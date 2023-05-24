from django.shortcuts import render


def swagger_ui(request):
    return render(request, 'swagger_ui.html')
