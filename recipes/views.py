from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# def home(request):
#     return HttpResponse("Home")

def home(request):
    # return render(request,'recipes/home.html')
    # return render(request,'recipes/home.html', status=404)
    # return render(request,'recipes/home.html', status=201)
    return render(request,'recipes/home.html', context={
        'name': "José Osvaldo"
    })


def about(request):
    return HttpResponse("About")
    


def contact(request):
    # return HttpResponse("Contact")
    return render(request, 'temp.html')