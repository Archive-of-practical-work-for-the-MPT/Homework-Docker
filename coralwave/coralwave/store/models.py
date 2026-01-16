from django.db import models


class Countries(models.Model):
    id_country = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False, blank=False)
    code = models.CharField(max_length=3, null=True, blank=True)

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'

    def __str__(self):
        return self.name


class Seas(models.Model):
    id_sea = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = 'Море'
        verbose_name_plural = 'Моря'

    def __str__(self):
        return self.name


class Reefs(models.Model):
    id_reef = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    coordinate = models.TextField(null=True, blank=True)
    id_country = models.ForeignKey(Countries, on_delete=models.PROTECT, db_column='id_country')
    id_sea = models.ForeignKey(Seas, on_delete=models.PROTECT, db_column='id_sea')

    class Meta:
        verbose_name = 'Риф'
        verbose_name_plural = 'Рифы'

    def __str__(self):
        return self.name


class Categories(models.Model):
    id_category = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Категория кораллов'
        verbose_name_plural = 'Категории кораллов'

    def __str__(self):
        return self.name


class Corals(models.Model):
    id_coral = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False, blank=False)
    scientific_name = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    id_reef = models.ForeignKey(Reefs, on_delete=models.PROTECT, db_column='id_reef')
    id_category = models.ForeignKey(Categories, on_delete=models.PROTECT, db_column='id_category')

    class Meta:
        verbose_name = 'Коралл'
        verbose_name_plural = 'Кораллы'

    def __str__(self):
        return self.name


class OrderStatuses(models.Model):
    id_status = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        verbose_name = 'Статус заказа'
        verbose_name_plural = 'Статусы заказов'

    def __str__(self):
        return self.name


class Accounts(models.Model):
    id_account = models.AutoField(primary_key=True)
    login = models.CharField(max_length=50, unique=True, null=False, blank=False)
    password = models.CharField(max_length=50, null=False, blank=False)

    class Meta:
        verbose_name = 'Аккаунт'
        verbose_name_plural = 'Аккаунты'

    def __str__(self):
        return self.login


class Roles(models.Model):
    id_role = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, unique=True, null=False, blank=False)

    class Meta:
        verbose_name = 'Роль'
        verbose_name_plural = 'Роли'

    def __str__(self):
        return self.name


class Users(models.Model):
    id_user = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, null=False, blank=False)
    lastname = models.CharField(max_length=50, null=False, blank=False)
    email = models.CharField(max_length=100, unique=True, null=False, blank=False)
    phone = models.CharField(max_length=20, null=True, blank=True)
    id_role = models.ForeignKey(Roles, on_delete=models.PROTECT, db_column='id_role')
    id_account = models.ForeignKey(Accounts, on_delete=models.PROTECT, db_column='id_account')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f"{self.name} {self.lastname}"


class Orders(models.Model):
    id_order = models.AutoField(primary_key=True)
    id_user = models.ForeignKey(Users, on_delete=models.PROTECT, db_column='id_user')
    order_date = models.DateTimeField(null=True, blank=True)
    id_status = models.ForeignKey(OrderStatuses, on_delete=models.PROTECT, db_column='id_status')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f"Заказ №{self.id_order}"


class OrderItems(models.Model):
    id_item = models.AutoField(primary_key=True)
    id_order = models.ForeignKey(Orders, on_delete=models.PROTECT, db_column='id_order')
    id_coral = models.ForeignKey(Corals, on_delete=models.PROTECT, db_column='id_coral')
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)

    class Meta:
        verbose_name = 'Элемент заказа'
        verbose_name_plural = 'Элементы заказа'

    def __str__(self):
        return f"Элемент заказа №{self.id_item}"


class CertificateStatuses(models.Model):
    id_status = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        verbose_name = 'Статус сертификата'
        verbose_name_plural = 'Статусы сертификатов'

    def __str__(self):
        return self.name


class CertificateTypes(models.Model):
    id_type = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    class Meta:
        verbose_name = 'Тип сертификата'
        verbose_name_plural = 'Типы сертификатов'

    def __str__(self):
        return self.name


class Certificates(models.Model):
    id_certificate = models.AutoField(primary_key=True)
    id_order = models.ForeignKey(Orders, on_delete=models.PROTECT, db_column='id_order')
    id_coral = models.ForeignKey(Corals, on_delete=models.PROTECT, db_column='id_coral')
    certificate_number = models.CharField(max_length=50, null=True, blank=True)
    issue_date = models.DateField(null=True, blank=True)
    id_status = models.ForeignKey(CertificateStatuses, on_delete=models.PROTECT, db_column='id_status')
    id_type = models.ForeignKey(CertificateTypes, on_delete=models.PROTECT, db_column='id_type')

    class Meta:
        verbose_name = 'Сертификат'
        verbose_name_plural = 'Сертификаты'

    def __str__(self):
        return self.certificate_number if self.certificate_number else f"Сертификат №{self.id_certificate}"


class Reviews(models.Model):
    id_review = models.AutoField(primary_key=True)
    id_user = models.ForeignKey(Users, on_delete=models.PROTECT, db_column='id_user')
    id_coral = models.ForeignKey(Corals, on_delete=models.PROTECT, db_column='id_coral')
    rating = models.IntegerField(null=False, blank=False)
    review_text = models.TextField(null=True, blank=True)
    review_date = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return f"Отзыв от {self.id_user} на {self.id_coral}"
