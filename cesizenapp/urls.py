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
    path('stress-quiz/', views.stress_quiz, name='stress_quiz'),
    path('administration/stress-events/', views.stress_event_list, name='stress_event_list'),
    path('administration/stress-events/create/', views.stress_event_edit, name='stress_event_create'),
    path('administration/stress-events/<int:event_id>/edit/', views.stress_event_edit, name='stress_event_edit'),
    path('administration/stress-events/<int:event_id>/delete/', views.stress_event_delete, name='stress_event_delete'),
    path('administration/results/', views.results_list, name='results_list'),
    path('administration/results/create/', views.results_edit, name='results_create'),
    path('administration/results/<int:result_id>/edit/', views.results_edit, name='results_edit'),
    path('administration/results/<int:result_id>/delete/', views.results_delete, name='results_delete'),
    path('administration/stress-events/create/', views.stress_event_create, name='stress_event_create'),
]