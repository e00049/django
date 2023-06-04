from django.contrib import admin
from apptrainersportal.models import Product

# Register your models here.

class apptrainersportal(admin.ModelAdmin):
    list = [ 'name', 'price' ]

admin.site.register(Product, apptrainersportal)
admin.site.register(Product)
