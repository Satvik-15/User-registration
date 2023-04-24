from django.shortcuts import render
from first_app.forms import UserForm
from first_app.forms import UserProfileInfoForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout


# Create your views here.


def base(request):
    const_dict = {"name": "satvik jalan", "number": 100}
    return render(request, 'first_app/base.html', const_dict)


def yoyo(request):
    return render(request, 'first_app/yoyo.html')


def index(request):

    if request.method == "POST":
        user_form = UserForm(request.POST)
        profile_form = UserProfileInfoForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            # Setting up the encyption for password

            user = user_form.save()
            # setting the user passcode algorithm
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            # check if there is picture uploaded before we save it
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            return render(request, 'first_app/yoyo.html')

        else:
            # print error statements
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request, 'first_app/index.html', {
        'user_form': user_form,
        'profile_form': profile_form})


def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # django authenticates user and password WoW..
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/index/')

            else:
                return HttpResponse("Account not active ")

        else:
            print("Tried login and failed!")
            print("Username: {} and password {}".format(username, password))
            return HttpResponse("invalid login details supplied")

    else:
        return render(request, 'first_app/login.html')


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/index/')
