from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

from .forms import RegisterForm



def sign_up(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse_lazy('home'))
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.added_by = request.user
            form.save(commit=True)
            return HttpResponseRedirect(reverse_lazy('home'))
        else:
            form = RegisterForm()
            return render(request, 'users/sign-up.html', {'form': form})
    elif request.method == 'GET':
        form = RegisterForm()
        return render(request, 'users/sign-up.html', {'form': form})