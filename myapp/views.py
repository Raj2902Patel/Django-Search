from django.shortcuts import render
from .models import *

# Create your views here.

def addproduct(request):
    if request.method == 'POST':
        pname = request.POST.get('pname')
        pbrand = request.POST.get('pbrand')
        pprice = request.POST.get('pprice')
        pstock = request.POST.get('pstock')

        query_set = data(pname=pname,pbrand=pbrand,pprice=pprice,pstock=pstock)
        query_set.save()

    return render(request,'data.html')


def display(request):
    fetch = data.objects.all()
    return render(request,'display.html',{'data':fetch})


def search(request):
    if request.method == "POST":
        query_name = request.POST.get('name',None)
        if query_name:
            results = data.objects.filter(pname__contains=query_name)
            return render(request, 'search.html', {"results":results})

    return render(request, 'search.html')