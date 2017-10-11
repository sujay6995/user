from django.shortcuts import render
from register.forms import UserForm,UserProfileInfoForm,UserProfileInfo
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate,login,logout
# Create your views here.

def index(request):
    return render(request,'register/index.html')

def register(request):
    registered = False

    if request.method=="POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'pictures' in request.FILES:
                profile.picture = request.FILES['profile_pic']

            profile.save()
            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request,'register/register.html',{'user_form':user_form,'profile_form':profile_form})

def user_login(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('user is not active')
        else:
            print('user does not exist')
            return HttpResponse("invalid login credentials")
    else:
        return render(request,'register/login.html')
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def view(request):
     UserProfileInfo = request.user.get_profile()
     profile_url = UserProfileInfo.url
     return HttpResponseRedirect(reverse('userpage'))

def user_page(request):
    return render(request,'register/userpage.html',{'form':url})










