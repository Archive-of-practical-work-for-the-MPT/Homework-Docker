from django.shortcuts import render
from rest_framework import viewsets
from store.models import (
    Countries, Seas, Reefs, Categories, Corals, OrderStatuses, Accounts, Roles,
    Users, Orders, OrderItems, CertificateStatuses, CertificateTypes,
    Certificates, Reviews
)
from .serializers import (
    CountriesSerializer, SeasSerializer, ReefsSerializer, CategoriesSerializer,
    CoralsSerializer, OrderStatusesSerializer, AccountsSerializer, RolesSerializer,
    UsersSerializer, OrdersSerializer, OrderItemsSerializer,
    CertificateStatusesSerializer, CertificateTypesSerializer,
    CertificatesSerializer, ReviewsSerializer
)

class CountriesViewSet(viewsets.ModelViewSet):
    queryset = Countries.objects.all()
    serializer_class = CountriesSerializer


class SeasViewSet(viewsets.ModelViewSet):
    queryset = Seas.objects.all()
    serializer_class = SeasSerializer


class ReefsViewSet(viewsets.ModelViewSet):
    queryset = Reefs.objects.all()
    serializer_class = ReefsSerializer


class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer


class CoralsViewSet(viewsets.ModelViewSet):
    queryset = Corals.objects.all()
    serializer_class = CoralsSerializer


class OrderStatusesViewSet(viewsets.ModelViewSet):
    queryset = OrderStatuses.objects.all()
    serializer_class = OrderStatusesSerializer


class AccountsViewSet(viewsets.ModelViewSet):
    queryset = Accounts.objects.all()
    serializer_class = AccountsSerializer


class RolesViewSet(viewsets.ModelViewSet):
    queryset = Roles.objects.all()
    serializer_class = RolesSerializer


class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer


class OrdersViewSet(viewsets.ModelViewSet):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer


class OrderItemsViewSet(viewsets.ModelViewSet):
    queryset = OrderItems.objects.all()
    serializer_class = OrderItemsSerializer


class CertificateStatusesViewSet(viewsets.ModelViewSet):
    queryset = CertificateStatuses.objects.all()
    serializer_class = CertificateStatusesSerializer


class CertificateTypesViewSet(viewsets.ModelViewSet):
    queryset = CertificateTypes.objects.all()
    serializer_class = CertificateTypesSerializer


class CertificatesViewSet(viewsets.ModelViewSet):
    queryset = Certificates.objects.all()
    serializer_class = CertificatesSerializer


class ReviewsViewSet(viewsets.ModelViewSet):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer

