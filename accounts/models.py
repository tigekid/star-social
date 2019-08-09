# Copyright (c) 2019 Brian Ainsworth. All Rights Reserved.
from django.db import models
from django.contrib import auth
from django.utils import timezone

class User(auth.models.User,auth.models.PermissionsMixin):
    '''
    displaying username on all pages were visible
    '''
    def __str__(self):
        return "@{}".format(self.username)
