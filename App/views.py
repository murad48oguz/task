from django.shortcuts import render,redirect
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import FileUpload
from .models import UserProfile
from .models import File
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from .models import File
from django.contrib import messages

def index(request):
    if request.user.is_authenticated:
        return redirect('userPage')
    else:
        return render(request,'index.html')

   


def loginPage(request):

    if request.user.is_authenticated:
        return redirect('userPage')

    elif request.method == 'POST':
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
      
        return render(request, 'userPage.html')
    
    
  

@login_required(login_url="/login/")
def user_files(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
        # print(user_profile)
        user_files = File.objects.filter(user=request.user)
        # print(user_files)
        return render(request, 'userFiles.html', {'user_files': user_files})
    except UserProfile.DoesNotExist:
        UserProfile.objects.create(user=request.user)
        return redirect('userPage')
    

@login_required(login_url="/login/")
def user_logout(request):
    logout(request)
    return redirect('loginPage')
  

   
@login_required(login_url="/login/")
def upload(request):

    if request.method == "POST":
        form = FileUpload(request.POST, request.FILES)
        if form.is_valid():
            file=form.save(commit=False)
            file.user=request.user
            file.save()
            return redirect('userPage')
        

    form = FileUpload()

    context = {
        "form": form,
    }

    
    return render(request, "upload.html", context)



@login_required(login_url="/login/")
def share_file(request, file_id):
    file_instance = get_object_or_404(File, id=file_id)
    print(file_instance)

    if request.method == 'POST':
        username = request.POST.get('username')
        user_to_share = User.objects.get(username=username)
        print(user_to_share)
        if user_to_share:
            
            shared_files = File.objects.filter(filename=file_instance.filename)
            print(shared_files)

            context = {
                'user_files': shared_files,
            }
            print(context)
            return render(request, 'userFiles.html', context)
            
        else:
            messages.error(request, 'User with username "{}" not found.'.format(username))
            return redirect('userFiles')
            
