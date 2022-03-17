from django.contrib import admin
from django.urls import path
from deardiaryapp import views
from .views import *

urlpatterns = [
    path('',views.index,name = 'home'),
    path('update_entry/<int:pk>',views.update_entry,name = 'Update_entry'),
    path('Delete_entry/<int:pk>',views.Delete_entry,name = 'Delete_entry'),
    path('register',views.register, name = 'register'),
    path('accounts/profile/',views.login_user,name = 'login'),
    path('accounts/logout/',views.logoutuser,name = 'logout')
]
