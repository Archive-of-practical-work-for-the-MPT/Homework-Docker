from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth import logout as django_logout
from .forms import RegisterForm, LoginForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


def info_view(request):
    return render(request, 'info.html')


class CountriesListView(ListView):
    model = Countries
    template_name = 'countries/countries_list.html'
    context_object_name = 'countries'


class CountriesDetailView(DetailView):
    model = Countries
    template_name = 'countries/countries_detail.html'
    context_object_name = 'country'


class CountriesCreateView(CreateView):
    model = Countries
    form_class = CountriesForm
    template_name = 'countries/countries_form.html'
    success_url = reverse_lazy('countries_list')


class CountriesUpdateView(UpdateView):
    model = Countries
    form_class = CountriesForm
    template_name = 'countries/countries_form.html'
    success_url = reverse_lazy('countries_list')


class CountriesDeleteView(DeleteView):
    model = Countries
    template_name = 'countries/countries_confirm_delete.html'
    success_url = reverse_lazy('countries_list')


class SeasListView(ListView):
    model = Seas
    template_name = 'seas/seas_list.html'
    context_object_name = 'seas'


class SeasDetailView(DetailView):
    model = Seas
    template_name = 'seas/seas_detail.html'
    context_object_name = 'sea'


class SeasCreateView(CreateView):
    model = Seas
    form_class = SeasForm
    template_name = 'seas/seas_form.html'
    success_url = reverse_lazy('seas_list')


class SeasUpdateView(UpdateView):
    model = Seas
    form_class = SeasForm
    template_name = 'seas/seas_form.html'
    success_url = reverse_lazy('seas_list')


class SeasDeleteView(DeleteView):
    model = Seas
    template_name = 'seas/seas_confirm_delete.html'
    success_url = reverse_lazy('seas_list')


class ReefsListView(ListView):
    model = Reefs
    template_name = 'reefs/reefs_list.html'
    context_object_name = 'reefs'


class ReefsDetailView(DetailView):
    model = Reefs
    template_name = 'reefs/reefs_detail.html'
    context_object_name = 'reef'


class ReefsCreateView(CreateView):
    model = Reefs
    form_class = ReefsForm
    template_name = 'reefs/reefs_form.html'
    success_url = reverse_lazy('reefs_list')


class ReefsUpdateView(UpdateView):
    model = Reefs
    form_class = ReefsForm
    template_name = 'reefs/reefs_form.html'
    success_url = reverse_lazy('reefs_list')


class ReefsDeleteView(DeleteView):
    model = Reefs
    template_name = 'reefs/reefs_confirm_delete.html'
    success_url = reverse_lazy('reefs_list')


class CategoriesListView(ListView):
    model = Categories
    template_name = 'categories/categories_list.html'
    context_object_name = 'categories'


class CategoriesDetailView(DetailView):
    model = Categories
    template_name = 'categories/categories_detail.html'
    context_object_name = 'category'


class CategoriesCreateView(CreateView):
    model = Categories
    form_class = CategoriesForm
    template_name = 'categories/categories_form.html'
    success_url = reverse_lazy('categories_list')


class CategoriesUpdateView(UpdateView):
    model = Categories
    form_class = CategoriesForm
    template_name = 'categories/categories_form.html'
    success_url = reverse_lazy('categories_list')


class CategoriesDeleteView(DeleteView):
    model = Categories
    template_name = 'categories/categories_confirm_delete.html'
    success_url = reverse_lazy('categories_list')


class CoralsListView(ListView):
    model = Corals
    template_name = 'corals/corals_list.html'
    context_object_name = 'corals'


class CoralsDetailView(DetailView):
    model = Corals
    template_name = 'corals/corals_detail.html'
    context_object_name = 'coral'


class CoralsCreateView(CreateView):
    model = Corals
    form_class = CoralsForm
    template_name = 'corals/corals_form.html'
    success_url = reverse_lazy('corals_list')


class CoralsUpdateView(UpdateView):
    model = Corals
    form_class = CoralsForm
    template_name = 'corals/corals_form.html'
    success_url = reverse_lazy('corals_list')


class CoralsDeleteView(DeleteView):
    model = Corals
    template_name = 'corals/corals_confirm_delete.html'
    success_url = reverse_lazy('corals_list')


class OrderStatusesListView(ListView):
    model = OrderStatuses
    template_name = 'orderstatuses/orderstatuses_list.html'
    context_object_name = 'orderstatuses'


class OrderStatusesDetailView(DetailView):
    model = OrderStatuses
    template_name = 'orderstatuses/orderstatuses_detail.html'
    context_object_name = 'orderstatus'


class OrderStatusesCreateView(CreateView):
    model = OrderStatuses
    form_class = OrderStatusesForm
    template_name = 'orderstatuses/orderstatuses_form.html'
    success_url = reverse_lazy('orderstatuses_list')


class OrderStatusesUpdateView(UpdateView):
    model = OrderStatuses
    form_class = OrderStatusesForm
    template_name = 'orderstatuses/orderstatuses_form.html'
    success_url = reverse_lazy('orderstatuses_list')


class OrderStatusesDeleteView(DeleteView):
    model = OrderStatuses
    template_name = 'orderstatuses/orderstatuses_confirm_delete.html'
    success_url = reverse_lazy('orderstatuses_list')


class AccountsListView(ListView):
    model = Accounts
    template_name = 'accounts/accounts_list.html'
    context_object_name = 'accounts'


class AccountsDetailView(DetailView):
    model = Accounts
    template_name = 'accounts/accounts_detail.html'
    context_object_name = 'account'


class AccountsCreateView(CreateView):
    model = Accounts
    form_class = AccountsForm
    template_name = 'accounts/accounts_form.html'
    success_url = reverse_lazy('accounts_list')


class AccountsUpdateView(UpdateView):
    model = Accounts
    form_class = AccountsForm
    template_name = 'accounts/accounts_form.html'
    success_url = reverse_lazy('accounts_list')


class AccountsDeleteView(DeleteView):
    model = Accounts
    template_name = 'accounts/accounts_confirm_delete.html'
    success_url = reverse_lazy('accounts_list')


class RolesListView(ListView):
    model = Roles
    template_name = 'roles/roles_list.html'
    context_object_name = 'roles'


class RolesDetailView(DetailView):
    model = Roles
    template_name = 'roles/roles_detail.html'
    context_object_name = 'role'


class RolesCreateView(CreateView):
    model = Roles
    form_class = RolesForm
    template_name = 'roles/roles_form.html'
    success_url = reverse_lazy('roles_list')


class RolesUpdateView(UpdateView):
    model = Roles
    form_class = RolesForm
    template_name = 'roles/roles_form.html'
    success_url = reverse_lazy('roles_list')


class RolesDeleteView(DeleteView):
    model = Roles
    template_name = 'roles/roles_confirm_delete.html'
    success_url = reverse_lazy('roles_list')


class UsersListView(ListView):
    model = Users
    template_name = 'users/users_list.html'
    context_object_name = 'users'


class UsersDetailView(DetailView):
    model = Users
    template_name = 'users/users_detail.html'
    context_object_name = 'user'


class UsersCreateView(CreateView):
    model = Users
    form_class = UsersForm
    template_name = 'users/users_form.html'
    success_url = reverse_lazy('users_list')


class UsersUpdateView(UpdateView):
    model = Users
    form_class = UsersForm
    template_name = 'users/users_form.html'
    success_url = reverse_lazy('users_list')


class UsersDeleteView(DeleteView):
    model = Users
    template_name = 'users/users_confirm_delete.html'
    success_url = reverse_lazy('users_list')


class OrdersListView(ListView):
    model = Orders
    template_name = 'orders/orders_list.html'
    context_object_name = 'orders'


class OrdersDetailView(DetailView):
    model = Orders
    template_name = 'orders/orders_detail.html'
    context_object_name = 'order'


class OrdersCreateView(CreateView):
    model = Orders
    form_class = OrdersForm
    template_name = 'orders/orders_form.html'
    success_url = reverse_lazy('orders_list')


class OrdersUpdateView(UpdateView):
    model = Orders
    form_class = OrdersForm
    template_name = 'orders/orders_form.html'
    success_url = reverse_lazy('orders_list')


class OrdersDeleteView(DeleteView):
    model = Orders
    template_name = 'orders/orders_confirm_delete.html'
    success_url = reverse_lazy('orders_list')


class OrderItemsListView(ListView):
    model = OrderItems
    template_name = 'orderitems/orderitems_list.html'
    context_object_name = 'orderitems'


class OrderItemsDetailView(DetailView):
    model = OrderItems
    template_name = 'orderitems/orderitems_detail.html'
    context_object_name = 'orderitem'


class OrderItemsCreateView(CreateView):
    model = OrderItems
    form_class = OrderItemsForm
    template_name = 'orderitems/orderitems_form.html'
    success_url = reverse_lazy('orderitems_list')


class OrderItemsUpdateView(UpdateView):
    model = OrderItems
    form_class = OrderItemsForm
    template_name = 'orderitems/orderitems_form.html'
    success_url = reverse_lazy('orderitems_list')


class OrderItemsDeleteView(DeleteView):
    model = OrderItems
    template_name = 'orderitems/orderitems_confirm_delete.html'
    success_url = reverse_lazy('orderitems_list')


class CertificateStatusesListView(ListView):
    model = CertificateStatuses
    template_name = 'certificatestatuses/certificatestatuses_list.html'
    context_object_name = 'certificatestatuses'


class CertificateStatusesDetailView(DetailView):
    model = CertificateStatuses
    template_name = 'certificatestatuses/certificatestatuses_detail.html'
    context_object_name = 'certificatestatus'


class CertificateStatusesCreateView(CreateView):
    model = CertificateStatuses
    form_class = CertificateStatusesForm
    template_name = 'certificatestatuses/certificatestatuses_form.html'
    success_url = reverse_lazy('certificatestatuses_list')


class CertificateStatusesUpdateView(UpdateView):
    model = CertificateStatuses
    form_class = CertificateStatusesForm
    template_name = 'certificatestatuses/certificatestatuses_form.html'
    success_url = reverse_lazy('certificatestatuses_list')


class CertificateStatusesDeleteView(DeleteView):
    model = CertificateStatuses
    template_name = 'certificatestatuses/certificatestatuses_confirm_delete.html'
    success_url = reverse_lazy('certificatestatuses_list')


class CertificateTypesListView(ListView):
    model = CertificateTypes
    template_name = 'certificatetypes/certificatetypes_list.html'
    context_object_name = 'certificatetypes'


class CertificateTypesDetailView(DetailView):
    model = CertificateTypes
    template_name = 'certificatetypes/certificatetypes_detail.html'
    context_object_name = 'certificatetype'


class CertificateTypesCreateView(CreateView):
    model = CertificateTypes
    form_class = CertificateTypesForm
    template_name = 'certificatetypes/certificatetypes_form.html'
    success_url = reverse_lazy('certificatetypes_list')


class CertificateTypesUpdateView(UpdateView):
    model = CertificateTypes
    form_class = CertificateTypesForm
    template_name = 'certificatetypes/certificatetypes_form.html'
    success_url = reverse_lazy('certificatetypes_list')


class CertificateTypesDeleteView(DeleteView):
    model = CertificateTypes
    template_name = 'certificatetypes/certificatetypes_confirm_delete.html'
    success_url = reverse_lazy('certificatetypes_list')


class CertificatesListView(ListView):
    model = Certificates
    template_name = 'certificates/certificates_list.html'
    context_object_name = 'certificates'


class CertificatesDetailView(DetailView):
    model = Certificates
    template_name = 'certificates/certificates_detail.html'
    context_object_name = 'certificate'


class CertificatesCreateView(CreateView):
    model = Certificates
    form_class = CertificatesForm
    template_name = 'certificates/certificates_form.html'
    success_url = reverse_lazy('certificates_list')


class CertificatesUpdateView(UpdateView):
    model = Certificates
    form_class = CertificatesForm
    template_name = 'certificates/certificates_form.html'
    success_url = reverse_lazy('certificates_list')


class CertificatesDeleteView(DeleteView):
    model = Certificates
    template_name = 'certificates/certificates_confirm_delete.html'
    success_url = reverse_lazy('certificates_list')


class ReviewsListView(ListView):
    model = Reviews
    template_name = 'reviews/reviews_list.html'
    context_object_name = 'reviews'


class ReviewsDetailView(DetailView):
    model = Reviews
    template_name = 'reviews/reviews_detail.html'
    context_object_name = 'review'


class ReviewsCreateView(CreateView):
    model = Reviews
    form_class = ReviewsForm
    template_name = 'reviews/reviews_form.html'
    success_url = reverse_lazy('reviews_list')


class ReviewsUpdateView(UpdateView):
    model = Reviews
    form_class = ReviewsForm
    template_name = 'reviews/reviews_form.html'
    success_url = reverse_lazy('reviews_list')


class ReviewsDeleteView(DeleteView):
    model = Reviews
    template_name = 'reviews/reviews_confirm_delete.html'
    success_url = reverse_lazy('reviews_list')


def account_list(request):
    accounts = Accounts.objects.all()
    return render(request, 'accounts/account_list.html', {'accounts': accounts})


def account_create(request):
    if request.method == 'POST':
        form = AccountsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('account_list')
    else:
        form = AccountsForm()
    return render(request, 'accounts/account_form.html', {'form': form})


def account_update(request, pk):
    account = get_object_or_404(Accounts, pk=pk)
    if request.method == 'POST':
        form = AccountsForm(request.POST, instance=account)
        if form.is_valid():
            form.save()
            return redirect('account_list')
    else:
        form = AccountsForm(instance=account)
    return render(request, 'accounts/account_form.html', {'form': form})


def account_delete(request, pk):
    account = get_object_or_404(Accounts, pk=pk)
    if request.method == 'POST':
        account.delete()
        return redirect('account_list')
    return render(request, 'accounts/account_confirm_delete.html', {'object': account})


def certificates_list(request):
    certificates = Certificates.objects.all()
    return render(request, 'certificates/certificates_list.html', {'certificates': certificates})


def certificates_create(request):
    if request.method == 'POST':
        form = CertificatesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('certificates_list')
    else:
        form = CertificatesForm()
    return render(request, 'certificates/certificates_form.html', {'form': form})


def certificates_update(request, pk):
    certificate = get_object_or_404(Certificates, pk=pk)
    if request.method == 'POST':
        form = CertificatesForm(request.POST, instance=certificate)
        if form.is_valid():
            form.save()
            return redirect('certificates_list')
    else:
        form = CertificatesForm(instance=certificate)
    return render(request, 'certificates/certificates_form.html', {'form': form})


def certificates_delete(request, pk):
    certificate = get_object_or_404(Certificates, pk=pk)
    if request.method == 'POST':
        certificate.delete()
        return redirect('certificates_list')
    return render(request, 'certificates/certificates_confirm_delete.html', {'object': certificate})


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            account = form.save()
            user_role = Roles.objects.filter(
                name__iexact='Пользователь').first()
            if not user_role:
                user_role = Roles.objects.create(name='Пользователь')
            Users.objects.create(
                name='', lastname='', email='', id_role=user_role, id_account=account
            )
            messages.success(
                request, 'Регистрация прошла успешно. Теперь войдите.')
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})

# --- Логин ---


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            login = form.cleaned_data['login']
            password = form.cleaned_data['password']
            try:
                account = Accounts.objects.get(login=login, password=password)
                request.session['account_id'] = account.id_account
                user = Users.objects.get(id_account=account)
                request.session['user_id'] = user.id_user
                request.session['role'] = user.id_role.name
                messages.success(
                    request, f'Добро пожаловать, {account.login}!')
                return redirect('profile')
            except Accounts.DoesNotExist:
                form.add_error(None, 'Неверный логин или пароль')
            except Users.DoesNotExist:
                form.add_error(None, 'Пользователь не найден')
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})


def logout_view(request):
    request.session.flush()
    django_logout(request)
    messages.info(request, 'Вы вышли из системы.')
    return redirect('login')


def profile_view(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')
    user = Users.objects.select_related(
        'id_role', 'id_account').get(id_user=user_id)
    return render(request, 'users/profile.html', {'user': user})


def forbidden_view(request):
    return render(request, 'users/forbidden.html')


def admin_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        role = request.session.get('role')
        if role != 'Администратор':
            return forbidden_view(request)
        return view_func(request, *args, **kwargs)
    return _wrapped_view


account_list = admin_required(account_list)
account_create = admin_required(account_create)
account_update = admin_required(account_update)
account_delete = admin_required(account_delete)


def purchase_certificate(request, certificate_type):
    """Представление для страницы покупки сертификата"""
    # Данные о сертификатах (в реальном проекте это было бы в БД)
    certificate_data = {
        'pink': {
            'name': 'Розовый ветвистый коралл',
            'id': 'AUS-GBR-2023-P001',
            'price': 5000,
            'description': 'Сертификат на коралл розового цвета в северной части Большого Барьерного рифа. Включает именной сертификат и ежемесячные обновления о состоянии вашего коралла.',
            'image': 'https://images.unsplash.com/photo-1560275619-4cc5fa59d3ae?ixlib=rb-4.0.3'
        },
        'blue': {
            'name': 'Голубой мозговой коралл',
            'id': 'AUS-GBR-2023-B042',
            'price': 7500,
            'description': 'Сертификат на редкий голубой мозговой коралл в центральной части Большого Барьерного рифа. Включает именной сертификат, фото вашего коралла и GPS-координаты.',
            'image': 'https://images.unsplash.com/photo-1551244072-5d12893278ab?ixlib=rb-4.0.3'
        },
        'orange': {
            'name': 'Оранжевый веерный коралл',
            'id': 'AUS-GBR-2023-O118',
            'price': 6200,
            'description': 'Сертификат на яркий оранжевый веерный коралл в южной части Большого Барьерного рифа. Включает именной сертификат и видео вашего коралла в естественной среде.',
            'image': 'https://images.unsplash.com/photo-1513039235271-5937eefe2959?ixlib=rb-4.0.3'
        }
    }
    
    # Если это custom тип, берем первый сертификат из базы данных
    if certificate_type == 'custom':
        try:
            certificate_type_obj = CertificateTypes.objects.first()
            if certificate_type_obj:
                certificate = {
                    'name': certificate_type_obj.name,
                    'id': f'CERT-{certificate_type_obj.id_type:04d}',
                    'price': certificate_type_obj.price or 5000,
                    'description': certificate_type_obj.description or 'Сертификат на коралл в Большом Барьерном рифе. Включает именной сертификат и регулярные обновления о состоянии вашего коралла.',
                    'image': 'https://images.unsplash.com/photo-1560275619-4cc5fa59d3ae?ixlib=rb-4.0.3'
                }
            else:
                return redirect('all_certificates')
        except:
            return redirect('all_certificates')
    elif certificate_type not in certificate_data:
        return redirect('home')
    else:
        certificate = certificate_data[certificate_type]
    
    if request.method == 'POST':
        # Обработка нажатия кнопки "Перевел"
        return redirect('certificate_success', certificate_type=certificate_type)
    
    context = {
        'certificate': certificate,
        'certificate_type': certificate_type
    }
    return render(request, 'certificates/purchase.html', context)


def certificate_success(request, certificate_type):
    """Представление для страницы успешной покупки сертификата"""
    certificate_data = {
        'pink': {
            'name': 'Розовый ветвистый коралл',
            'id': 'AUS-GBR-2023-P001',
            'price': 5000,
            'image': 'https://images.unsplash.com/photo-1560275619-4cc5fa59d3ae?ixlib=rb-4.0.3'
        },
        'blue': {
            'name': 'Голубой мозговой коралл',
            'id': 'AUS-GBR-2023-B042',
            'price': 7500,
            'image': 'https://images.unsplash.com/photo-1551244072-5d12893278ab?ixlib=rb-4.0.3'
        },
        'orange': {
            'name': 'Оранжевый веерный коралл',
            'id': 'AUS-GBR-2023-O118',
            'price': 6200,
            'image': 'https://images.unsplash.com/photo-1513039235271-5937eefe2959?ixlib=rb-4.0.3'
        }
    }
    
    # Если это custom тип, берем первый сертификат из базы данных
    if certificate_type == 'custom':
        try:
            certificate_type_obj = CertificateTypes.objects.first()
            if certificate_type_obj:
                certificate = {
                    'name': certificate_type_obj.name,
                    'id': f'CERT-{certificate_type_obj.id_type:04d}',
                    'price': certificate_type_obj.price or 5000,
                    'image': 'https://images.unsplash.com/photo-1560275619-4cc5fa59d3ae?ixlib=rb-4.0.3'
                }
            else:
                return redirect('all_certificates')
        except:
            return redirect('all_certificates')
    elif certificate_type not in certificate_data:
        return redirect('home')
    else:
        certificate = certificate_data[certificate_type]
    
    context = {
        'certificate': certificate,
        'certificate_type': certificate_type
    }
    return render(request, 'certificates/success.html', context)


def all_certificates_view(request):
    """Представление для отображения всех сертификатов из базы данных"""
    # Получаем параметр поиска
    search_query = request.GET.get('search', '')
    
    # Получаем все типы сертификатов из базы данных
    certificate_types = CertificateTypes.objects.all()
    
    # Применяем фильтр поиска если есть запрос
    if search_query:
        certificate_types = certificate_types.filter(name__icontains=search_query)
    
    # Если сертификатов нет, передаем пустой список
    if not certificate_types.exists():
        certificate_types = []
    
    context = {
        'certificate_types': certificate_types,
        'search_query': search_query
    }
    return render(request, 'certificates/all_certificates.html', context)
