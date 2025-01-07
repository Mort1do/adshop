from django.shortcuts import render
from .models import product

#test text views
#!!!!delete later!!!!

from django.http import HttpResponse
from pathlib import Path

def index(request):
    outputTest = product.objects.all()

    #for i in range(len(outputTest)):
    #    currentObject = outputTest[i]
    #    currentObject.name

    context = {
        'products': outputTest
    }

    print(Path(__file__).resolve().parent.parent)

    return render(request, "catalog/catalog.html", context=context)



