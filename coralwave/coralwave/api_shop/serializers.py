from rest_framework import serializers
from store.models import (
    Countries, Seas, Reefs, Categories, Corals, OrderStatuses, Accounts, Roles,
    Users, Orders, OrderItems, CertificateStatuses, CertificateTypes,
    Certificates, Reviews
)


class CountriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Countries
        fields = '__all__'


class SeasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seas
        fields = '__all__'


class ReefsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reefs
        fields = '__all__'


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'


class CoralsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Corals
        fields = '__all__'


class OrderStatusesSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderStatuses
        fields = '__all__'


class AccountsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accounts
        fields = '__all__'


class RolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roles
        fields = '__all__'


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'


class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = '__all__'


class OrderItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItems
        fields = '__all__'


class CertificateStatusesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CertificateStatuses
        fields = '__all__'


class CertificateTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CertificateTypes
        fields = '__all__'


class CertificatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificates
        fields = '__all__'


class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = '__all__'
