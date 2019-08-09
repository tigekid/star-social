# Copyright (c) 2019 Brian Ainsworth. All Rights Reserved.
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.views.generic import CreateView
from . import forms

class SignUp(CreateView):
    '''
    form used to sign up to blog and redirect to login
    '''
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'