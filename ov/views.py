from django.shortcuts import render

# from django.http import HttpResponse


def index(request):
    context_dict = {'boldmessage': "I am bold font from the context"}
    return render(request, 'ov/index.html', context_dict)


def about(request):
    context_dict = {'boldmessage': "About page you most welcome"}
    return render(request, 'ov/about.html', context_dict)
