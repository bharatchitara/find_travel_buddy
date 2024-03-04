from django.shortcuts import render


# Create your views here.

def index(request, *args, **kargs):
    '''application landing page'''
    return render(request, 'userlogin/home.html')
