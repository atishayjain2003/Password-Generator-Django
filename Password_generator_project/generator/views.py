from django.shortcuts import render
from django.http import HttpResponse
import random

def home(request):
    return render(request, 'home.html')
def password(request):
    thepassword='testing'

    characters=list('abcdefghijklmnopqrstuvwxyz')
    
    if(request.GET.get('uppercase')):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if(request.GET.get('special')):
        characters.extend(list('!@#$%^&*'))
    if(request.GET.get('numbers')):
        characters.extend(list('123456789'))


    
    
    length=int(request.GET.get('length'))

    
    thepassword=''
    
    for x in range(length):
        thepassword+=random.choice(characters)
    
    return render(request, 'password.html', {'password':thepassword})

# Create your views here.
