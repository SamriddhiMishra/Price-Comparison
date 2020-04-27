from django.shortcuts import render,redirect,reverse
from .models import amfp
from .sel_code import compare

def enterprod(request):
    f = amfp.objects.all()
    f.delete()
    return render(request,'index.html')

def createtable(request):
    product=request.POST['product']
    compare(product)
    f = amfp.objects.all()
    return render(request, 'show.html',{'f':f})
