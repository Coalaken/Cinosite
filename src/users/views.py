import logging

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth.models import User
from django.views.generic import View


from .forms import RegisterForm
from .service import register_form_checker


# logger name from settings 
logger = logging.getLogger('django')

    
def profile_page(request, pk):
    return render(request, 'users/accout_page.html')


class RegistrationUser(View):

    def get(self, request):
        """get request on register page"""
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('home'))
        form = RegisterForm()
        return render(request, 'registration/sign-up.html', 
                      {'form': form})
        
    def post(self, request):
        """post request on user form"""
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('home'))
        form = RegisterForm(request.POST)
        try:
            register_form_checker(form) 
        except Exception as e:
            logger.exception(e)
        else:
            form = RegisterForm()
            return render(request, 'registration/sign-up.html', 
                        {'form': form})
            
               