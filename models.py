from django.db import models
from django.utils import timezone
from datetime import timedelta


class User(models.Model):
    mobile_number  = models.CharField(max_length=20)

    class Meta:
        db_table = "myapp_user"

    def __str__(self):
        x = '%s' % (self.mobile_number)
        return x
