from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('myapp.urls')),
]

----------------------------

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
