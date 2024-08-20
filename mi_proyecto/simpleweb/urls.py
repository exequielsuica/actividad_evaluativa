
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home,name='home'),
    
    path('category/', views.categorylisting, name="categorylisting"),
    path('category/create/', views.categorycreate, name="categorycreate"),
    path('category/inserted/', views.categoryaddprocess, name="categoryaddprocess"),
    path('category/delete/<int:id>', views.categorydelete, name="categorydelete"),
    path('category/edit/<int:id>', views.categoryedit, name="categoryedit"),
    path('category/update/', views.categoryupdate, name="categoryupdate"),
    
    path('alumnos/', views.alumnos_listing, name='alumnoslisting'),
    path('alumnos/create/', views.alumnos_create, name="alumnoscreate"),
    path('alumnos/inserted/', views.alumnos_addprocess, name="alumnosaddprocess"),
    path('alumnos/delete/<int:id>', views.alumnos_delete, name="alumnosdelete"),
    path('alumnos/edit/<int:id>', views.alumnos_edit, name="alumnosedit"),
    path('alumnos/update/', views.alumnos_update, name="alumnosupdate"),
]