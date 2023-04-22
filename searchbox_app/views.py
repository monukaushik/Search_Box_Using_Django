import contextlib
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import *
from django.db.models import Q



def index(request):
    data = student.objects.all()
    if request.method=='GET':
        data1=request.GET.get('search')
        with contextlib.suppress(Exception):
            lookupvalue=Q(name__icontains=data1)|Q(username__icontains=data1)|Q(email__icontains=data1)
            status=student.objects.filter(lookupvalue)
            return render(request, 'index.html', {"data": status})
    return render(request, 'index.html', {"data": data})
