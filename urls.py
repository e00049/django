from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('myapp.urls')),
]

# -------------------------------------------------

from django.urls import path
from myapp.views import *

# urlpatterns = [
#     path('userslistview/',            userslistview.as_view(), name='userslistview'),
#     # path('userdetailsview/<int:pk>/', userdetailsview,   name='userdetails'),
# ]

urlpatterns = [
    path('users/',           UserView.as_view(),       name='user-list'),
    path('users/<int:uid>/', UserDetailView.as_view(), name='user-detail'),
]

#-------------------------------------------------
    # Django REST Swagger
from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from myapp.views import *
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView, TokenVerifyView)

schema_view = get_schema_view(
    openapi.Info(
        title="Endpoints APIs",
        default_version="v1",
        description="Trainers Portal Endpoints APIs",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="e00049@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),

   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),    

# URL - https://django-rest-swagger.readthedocs.io/en/latest/
    
        path('register/', RegisterAPIView.as_view(), name="register"),
        path('send-otp/', SendOTPView.as_view(), name='send-otp'),

    

    
