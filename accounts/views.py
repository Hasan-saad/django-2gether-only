from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import *
from .models import Profile

def signup(request):
    if request.method == 'POST':
        form = Signup(request.POST)
        formUser = SignupUser(request.POST)
        
        if form.is_valid() and formUser.is_valid():
            user = form.save()
            user.profile.city = formUser.cleaned_data.get('city')
            user.profile.phoneNumber = formUser.cleaned_data.get('phoneNumber')
            user.profile.save()

            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            userLogin = authenticate(username=username, password=password)
            login(request, userLogin)
            return redirect('/accounts/profile')
    else:
        form = Signup()
        formUser = SignupUser()
    return render(request, 'registration/singup.html', {'form': form, 'formUser':formUser})


def profile(request):
    profile = Profile.objects.get(user=request.user.id)
    return render(request, 'accounts/profile.html', {'profile': profile})

def profile_edit(request):
    profile = Profile.objects.get(user=request.user)

    if request.method == 'POST':
        userform = UserForm(request.POST, instance=request.user)
        profileform = ProfileForm(request.POST, request.FILES, instance=profile)
        if userform.is_valid() and profileform.is_valid():
            userform.save()
            profileform.save(commit=False)
            profileform.user = request.user
            profileform.save()
            return redirect(reverse('accounts:profile'))
    else:
        userform = UserForm(instance=request.user)
        profileform = ProfileForm(instance=profile)

    return render(request, 'accounts/profile_edit.html', {'userform': userform, 'profileform': profileform})




