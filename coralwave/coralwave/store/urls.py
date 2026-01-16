from django.urls import path, include
from .views import *

urlpatterns = [
    path('', info_view, name='home'),
    path('info/', info_view, name='info_view'),

    path('accounts/', account_list, name='account_list'),
    path('accounts/create/', account_create, name='account_create'),
    path('accounts/<int:pk>/update/', account_update, name='account_update'),
    path('accounts/<int:pk>/delete/', account_delete, name='account_delete'),

    path('certificates/', certificates_list, name='certificates_list'),
    path('certificates/create/', certificates_create, name='certificates_create'),
    path('certificates/<int:pk>/update/', certificates_update, name='certificates_update'),
    path('certificates/<int:pk>/delete/', certificates_delete, name='certificates_delete'),
    
    # Новые маршруты для покупки сертификатов
    path('purchase/<str:certificate_type>/', purchase_certificate, name='purchase_certificate'),
    path('certificate/success/<str:certificate_type>/', certificate_success, name='certificate_success'),
    
    # Маршрут для страницы всех сертификатов
    path('all-certificates/', all_certificates_view, name='all_certificates'),

    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile_view, name='profile'),
]
