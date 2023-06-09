""" 
Django Models with creation normal and superuser
"""

from django.db import models
from django.utils import timezone
from rest_framework_simplejwt.tokens import RefreshToken
from datetime import timedelta


class User(models.Model):
    mobile_number  = models.CharField(max_length=20)

    class Meta:
        db_table = "myapp_user"

    def __str__(self):
        x = '%s' % (self.mobile_number)
        return x

    # Creating tokens manually
    def token(user):
        refresh = RefreshToken.for_user(user)
    
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }


class MyModel(models.Model):	
	user             = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True, editable=False)
    tf_location      = models.CharField(max_length=5000, null=True, blank=True)
    created_at       = models.DateTimeField(auto_now_add=True)
    updated_at       = models.DateTimeField(auto_now=True)

