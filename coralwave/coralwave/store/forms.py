from django import forms
from .models import *

class CountriesForm(forms.ModelForm):
    class Meta:
        model = Countries
        fields = '__all__'

class SeasForm(forms.ModelForm):
    class Meta:
        model = Seas
        fields = '__all__'

class ReefsForm(forms.ModelForm):
    class Meta:
        model = Reefs
        fields = '__all__'

class CategoriesForm(forms.ModelForm):
    class Meta:
        model = Categories
        fields = '__all__'

class CoralsForm(forms.ModelForm):
    class Meta:
        model = Corals
        fields = '__all__'

class OrderStatusesForm(forms.ModelForm):
    class Meta:
        model = OrderStatuses
        fields = '__all__'

class AccountsForm(forms.ModelForm):
    class Meta:
        model = Accounts
        fields = '__all__'

class RolesForm(forms.ModelForm):
    class Meta:
        model = Roles
        fields = '__all__'

class UsersForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = '__all__'

class OrdersForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = '__all__'

class OrderItemsForm(forms.ModelForm):
    class Meta:
        model = OrderItems
        fields = '__all__'

class CertificateStatusesForm(forms.ModelForm):
    class Meta:
        model = CertificateStatuses
        fields = '__all__'

class CertificateTypesForm(forms.ModelForm):
    class Meta:
        model = CertificateTypes
        fields = '__all__'

class CertificatesForm(forms.ModelForm):
    class Meta:
        model = Certificates
        fields = '__all__'

class ReviewsForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = '__all__'

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Accounts
        fields = ['login', 'password']

class LoginForm(forms.Form):
    login = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)