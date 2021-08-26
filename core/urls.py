from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('getAllCategories', views.getAllCategories, name='getAllCategories'),
    path('getAllSubCategories', views.getAllSubCategories, name='getAllSubCategories'),
    path('getAllProductsForCategory', views.getAllProductsForCategory, name='getAllProductsForCategory'),
    path('getAllProductsForSubCategory', views.getAllProductsForSubCategory, name='getAllProductsForSubCategory'),
    path('postProduct', views.postProduct, name='postProduct'),
]
