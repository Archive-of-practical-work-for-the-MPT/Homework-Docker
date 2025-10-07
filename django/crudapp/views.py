from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Product
from .forms import ProductForm

# Create your views here.


def product_list(request):
    products = Product.objects.all()
    return render(request, 'crudapp/product_list.html', {'products': products})


def product_create(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Продукт успешно создан!')
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'crudapp/product_form.html', {'form': form, 'title': 'Создать продукт'})


def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Продукт успешно обновлен!')
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'crudapp/product_form.html', {'form': form, 'title': 'Редактировать продукт'})


def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        product.delete()
        messages.success(request, 'Продукт успешно удален!')
        return redirect('product_list')
    return render(request, 'crudapp/product_confirm_delete.html', {'product': product})
