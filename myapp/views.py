from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
# Create your views here.

def home(request):
    return render(request,'myapp/home.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        myuser = User.objects.create_user(username=username,password=password)
        if myuser:
            return HttpResponse('Login Success')
        else:
            return HttpResponse('Login Failed')
        
        myuser.save()

        return redirect('home')

    

    return render(request,'myapp/login.html')