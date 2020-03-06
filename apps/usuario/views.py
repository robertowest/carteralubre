from django.contrib.auth.decorators import login_required
from django.shortcuts import render


def signup(request):
    return render(request, 'users/signup.html')


@login_required(login_url='/login/')
def profile(request):
    return render(request, 'users/profile.html')
