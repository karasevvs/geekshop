from django.shortcuts import render, HttpResponseRedirect
from users.models import User
from products.models import ProductCategory, Product
from admins.forms import UserAdminRegistrationForm, UserAdminProfileForm, ProductCategoryAdminProfileForm, \
    ProductAdminProfileForm
from django.urls import reverse
from django.contrib.auth.decorators import user_passes_test


@user_passes_test(lambda u: u.is_staff)
def index(request):
    context = {'title': 'Админ-панель'}
    return render(request, 'admins/index.html', context)


@user_passes_test(lambda u: u.is_staff)
def admin_users(request):
    context = {
        'title': 'Админ-панель - Пользователи',
        'users': User.objects.all()}
    return render(request, 'admins/admin-users-read.html', context)


@user_passes_test(lambda u: u.is_staff)
def admin_users_create(request):
    if request.method == 'POST':
        form = UserAdminRegistrationForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_users'))
        else:
            print(form.errors)
    else:
        form = UserAdminRegistrationForm()
    context = {'title': 'Админ-панель - Создание пользователя',
               'form': form}
    return render(request, 'admins/admin-users-create.html', context)


@user_passes_test(lambda u: u.is_staff)
def admin_users_update(request, pk):
    selected_user = User.objects.get(id=pk)
    if request.method == 'POST':
        form = UserAdminProfileForm(instance=selected_user, files=request.FILES, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_users'))
    form = UserAdminProfileForm(instance=selected_user)
    context = {'title': 'Админ-панель - Редактирование пользователя',
               'form': form,
               'selected_user': selected_user,
               }
    return render(request, 'admins/admin-users-update-delete.html', context)


@user_passes_test(lambda u: u.is_staff)
def admin_users_remove(request, pk):
    user = User.objects.get(id=pk)
    # user.delete()
    user.is_active = False
    user.save()
    return HttpResponseRedirect(reverse('admins:admin_users'))


# Работа с категориями

@user_passes_test(lambda u: u.is_staff)
def admin_category(request):
    context = {
        'title': 'Админ-панель - Категории',
        'categories': ProductCategory.objects.all()}
    return render(request, 'admins/admin-category-read.html', context)


@user_passes_test(lambda u: u.is_staff)
def admin_category_update(request, pk):
    selected_category = ProductCategory.objects.get(id=pk)
    if request.method == 'POST':
        form = ProductCategoryAdminProfileForm(instance=selected_category, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_category'))
    form = ProductCategoryAdminProfileForm(instance=selected_category)
    context = {'title': 'Админ-панель - Редактирование категории',
               'form': form,
               'selected_category': selected_category,
               }
    return render(request, 'admins/admin-category-update-delete.html', context)


@user_passes_test(lambda u: u.is_staff)
def admin_category_remove(request, pk):
    name = ProductCategory.objects.get(id=pk)
    name.delete()
    return HttpResponseRedirect(reverse('admins:admin_category'))


@user_passes_test(lambda u: u.is_staff)
def admin_category_create(request):
    if request.method == 'POST':
        form = ProductCategoryAdminProfileForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_category'))
        else:
            print(form.errors)
    else:
        form = ProductCategoryAdminProfileForm()
    context = {'title': 'Админ-панель - Создание категории',
               'form': form}
    return render(request, 'admins/admin-category-create.html', context)


# Работа с продуктами


@user_passes_test(lambda u: u.is_staff)
def admin_product(request):
    context = {
        'title': 'Админ-панель - Продукты',
        'products': Product.objects.all()}
    return render(request, 'admins/admin-products-read.html', context)


@user_passes_test(lambda u: u.is_staff)
def admin_products_create(request):
    if request.method == 'POST':
        form = ProductAdminProfileForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_product'))
        else:
            print(form.errors)
    else:
        form = ProductAdminProfileForm()

    context = {'title': 'Админ-панель - Создание продукта',
               'form': form,
               }
    return render(request, 'admins/admin-products-create.html', context)


@user_passes_test(lambda u: u.is_staff)
def admin_products_update(request, pk):
    selected_product = Product.objects.get(id=pk)
    if request.method == 'POST':
        form = ProductAdminProfileForm(instance=selected_product, files=request.FILES, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_product'))
    form = ProductAdminProfileForm(instance=selected_product)
    context = {'title': 'Админ-панель - Редактирование продукта',
               'form': form,
               'selected_product': selected_product,
               }
    return render(request, 'admins/admin-products-update-delete.html', context)


@user_passes_test(lambda u: u.is_staff)
def admin_products_remove(request, pk):
    product = Product.objects.get(id=pk)
    product.delete()
    return HttpResponseRedirect(reverse('admins:admin_product'))