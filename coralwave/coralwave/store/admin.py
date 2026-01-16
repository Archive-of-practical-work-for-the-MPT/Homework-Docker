from django.contrib import admin

from .models import *

@admin.register(Countries)
class CountriesAdmin(admin.ModelAdmin):
    pass

@admin.register(Seas)
class SeasAdmin(admin.ModelAdmin):
    pass

@admin.register(Reefs)
class ReefsAdmin(admin.ModelAdmin):
    pass

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    pass

@admin.register(Corals)
class CoralsAdmin(admin.ModelAdmin):
    pass

@admin.register(OrderStatuses)
class OrderStatusesAdmin(admin.ModelAdmin):
    pass

@admin.register(Accounts)
class AccountsAdmin(admin.ModelAdmin):
    pass

@admin.register(Roles)
class RolesAdmin(admin.ModelAdmin):
    pass

@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    pass

@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    pass

@admin.register(OrderItems)
class OrderItemsAdmin(admin.ModelAdmin):
    pass

@admin.register(CertificateStatuses)
class CertificateStatusesAdmin(admin.ModelAdmin):
    pass

@admin.register(CertificateTypes)
class CertificateTypesAdmin(admin.ModelAdmin):
    pass

@admin.register(Certificates)
class CertificatesAdmin(admin.ModelAdmin):
    pass

@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    pass
