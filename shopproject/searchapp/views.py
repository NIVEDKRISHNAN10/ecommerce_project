from django.shortcuts import render
from shopapp.models import product
from django.db.models import Q

def searchrslt(request):
    products=None
    query=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        products=product.objects.all().filter(Q(name__contains= query ) |Q(desc__contains=query)  )
    return render (request,'search.html',{'query':query , 'products':products})

