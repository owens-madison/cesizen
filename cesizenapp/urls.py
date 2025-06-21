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
    path('diagnostic/', views.diagnostic, name='diagnostic'),
    path('submit-diagnostic/', views.submit_diagnostic, name='submit_diagnostic'),
    path('diagnostic/save/', views.save_diagnostic, name='save_diagnostic'),
    path('account/', views.account, name='account'),
    path('logout/', views.custom_logout, name='logout'),

]