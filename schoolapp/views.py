from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.

def index(request):
    return render(request,"index.html")



def middle(request):
    return render(request,"middlepage.html")
#
#
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if not username or not password :
            messages.error(request, "Please fill in all the fields.")
            return render(request, 'login.html')

        if user is not None:
            auth.login(request,user)
            return render(request,"middlepage.html")
        else:
            messages.info(request,'Invalid credentials')
            return redirect('/login')
    return render(request,"login.html")


def register(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        cpassword=request.POST['password1']


        if not username or not password or not cpassword:
            messages.error(request, "Please fill in all the fields.")
            return render(request, 'register.html')

        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username exists")
                return redirect('/register')
            else:
                user = User.objects.create_user(username=username, password=password)

                user.save();
                print("check1")
                return redirect('/login')
            # print('user created')
        else:
            messages.info(request,"Password not matching")
            return redirect('/register')
        return redirect('/')
    return render(request,'register.html')


def form(request):
    return render(request,"form.html")

def final(request):
    return render(request,"final.html")


def logout(request):
    auth.logout(request)
    return redirect('/')

def home(request):
    return render(request,"home.html")





