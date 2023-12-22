from django.urls import path
from . import views

urlpatterns = [
    path('', views.rastenie_index, name='index'),
    path('all', views.rastenie_all, name='all'),
    path('<int:pk>/', views.rastenie_show, name='show'),
    path('admin/all', views.rastenie_adm_all, name='adm_all'),
    path('admin/new/', views.rastenie_new, name='new'),
    path('admin/<int:pk>/edit', views.rastenie_edit, name='edit'),
    path('admin/<int:pk>/delete', views.rastenie_delete, name='delete'),
]