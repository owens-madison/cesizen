from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('postInformation/', views.postInformation, name='postInformation'),
    path('edit/<uuid:post_id>/', views.edit_post, name='edit_post'),
    path('delete/<uuid:post_id>/', views.delete_post, name='delete_post'),
    path('account/', views.account, name='account'),
    path('logout/', views.custom_logout, name='logout'),
    path('administration/users/', views.admin_user_list, name='admin_user_list'),
    path('administration/users/create/', views.admin_user_create, name='admin_user_create'),
    path('administration/users/<int:user_id>/edit/', views.admin_user_edit, name='admin_user_edit'),
    path('administration/users/<int:user_id>/delete/', views.admin_user_delete, name='admin_user_delete'),
]