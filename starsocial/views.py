# Copyright (c) 2019 Brian Ainsworth. All Rights Reserved.
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView

class TestPage(TemplateView):
    '''
    redirected to this page once logged in.
    '''
    template_name = 'test.html'

class ThanksPage(TemplateView):
    '''
    redirected to this page once logged out.
    '''
    template_name = 'thanks.html'

class HomePage(TemplateView):
    '''
    main page either logged in as user or not
    '''
    template_name = 'index.html'

    def get(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('test'))
        return super().get(request,*args,**kwargs)