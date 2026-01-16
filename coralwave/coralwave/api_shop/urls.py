from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CountriesViewSet, SeasViewSet, ReefsViewSet, CategoriesViewSet, CoralsViewSet,
    OrderStatusesViewSet, AccountsViewSet, RolesViewSet, UsersViewSet, OrdersViewSet,
    OrderItemsViewSet, CertificateStatusesViewSet, CertificateTypesViewSet,
    CertificatesViewSet, ReviewsViewSet
)

router = DefaultRouter()
router.register(r'countries', CountriesViewSet)
router.register(r'seas', SeasViewSet)
router.register(r'reefs', ReefsViewSet)
router.register(r'categories', CategoriesViewSet)
router.register(r'corals', CoralsViewSet)
router.register(r'orderstatuses', OrderStatusesViewSet)
router.register(r'accounts', AccountsViewSet)
router.register(r'roles', RolesViewSet)
router.register(r'users', UsersViewSet)
router.register(r'orders', OrdersViewSet)
router.register(r'orderitems', OrderItemsViewSet)
router.register(r'certificatestatuses', CertificateStatusesViewSet)
router.register(r'certificatetypes', CertificateTypesViewSet)
router.register(r'certificates', CertificatesViewSet)
router.register(r'reviews', ReviewsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
