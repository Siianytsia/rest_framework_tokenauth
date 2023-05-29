from django.contrib import admin
from django.urls import path
from myapp.views import UserRegister, UserLogIn, UserLogOut

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/register/', UserRegister.as_view(), name='register'),
    path('api/login/', UserLogIn.as_view(), name='login'),
    path('api/logout/', UserLogOut.as_view(), name='logout')
]
