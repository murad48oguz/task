from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import FileUpload


def index(request):

    return render(request,'index.html')


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)

            return redirect('userPage')
        else:
            return render(request, 'login.html', {
            'error': 'Username or password is incorrect.'
        })
    else:
      return render(request, 'login.html')
    
    

@login_required(login_url="/login/")
def userPage(request):
    return render(request,'userPage.html')
  



@login_required(login_url="/login/")
def user_logout(request):
    logout(request)
    return redirect('loginPage')
  

   
@login_required(login_url="/login/")
def upload(request):

    if request.method == "POST":
        print('hfh')
        form = FileUpload(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('userPage')
        

    form = FileUpload()

    context = {
        "form": form,
    }

    
    return render(request, "upload.html", context)