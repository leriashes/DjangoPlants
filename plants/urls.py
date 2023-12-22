from django.urls import path
from . import views

urlpatterns = [
    path('', views.rastenie_index, name='index'),
    path('all', views.rastenie_all, name='all'),
    path('favourites', views.rastenie_fav, name='fav'),
    path('rastlist', views.rastenie_list, name='rastlist'),
    path('favourites/<int:pk>', views.rastenie_fav_add, name='fav_add'),
    path('favourites/add/', views.rastenie_fav_add, name='fav_add'),
    #path('favourites/remove/', views.rastenie_fav_rem, name='fav_rem'),
    path('<int:pk>/', views.rastenie_show, name='show'),
    path('admin/all', views.rastenie_adm_all, name='adm_all'),
    path('admin/new/', views.rastenie_new, name='new'),
    path('admin/<int:pk>/edit', views.rastenie_edit, name='edit'),
    path('admin/<int:pk>/delete', views.rastenie_delete, name='delete'),
]