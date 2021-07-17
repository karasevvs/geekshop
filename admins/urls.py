from django.urls import path
from admins.views import index, admin_users, admin_users_create, admin_users_update, admin_users_remove, admin_category, \
    admin_category_update, admin_category_remove, admin_category_create, admin_product, admin_products_create

app_name = 'admins'

urlpatterns = [
    path('', index, name='index'),

    path('users/', admin_users, name='admin_users'),
    path('users/create/', admin_users_create, name='admin_users_create'),
    path('users/update/<int:pk>/', admin_users_update, name='admin_users_update'),
    path('users/remove/<int:pk>/', admin_users_remove, name='admin_users_remove'),

    path('category/', admin_category, name='admin_category'),
    path('category/update/<int:pk>/', admin_category_update, name='admin_category_update'),
    path('category/remove/<int:pk>/', admin_category_remove, name='admin_category_remove'),
    path('category/create/', admin_category_create, name='admin_category_create'),

    path('products/', admin_product, name='admin_product'),
    path('products/create/', admin_products_create, name='admin_products_create'),
]
