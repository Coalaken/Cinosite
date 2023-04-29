from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from django.contrib.auth.models import User
from django.views.generic import View


from .forms import RegisterForm, ChangeUserSettings



def sign_up(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse_lazy('home'))    
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect(reverse_lazy('home'))
        else:
            form = RegisterForm()
            return render(request, 'users/sign-up.html', {'form': form})
    elif request.method == 'GET':
        form = RegisterForm()
        return render(request, 'users/sign-up.html', {'form': form})
    
    
def profile_page(request, pk):
    return render(request, 'users/accout_page.html')
