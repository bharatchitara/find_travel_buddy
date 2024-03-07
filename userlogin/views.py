from django.shortcuts import render


# Create your views here.

def index(request, *args, **kargs):
    '''application landing page'''
    return render(request, 'userlogin/home.html')

def find_buddy(request, *args, **kargs):
    '''find buddy page, this page will contain the map design'''
    return render(request, 'userlogin/find_buddy.html')
