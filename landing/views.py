from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

def home(request):
    data = {}
    return render (request, 'home.html', data)