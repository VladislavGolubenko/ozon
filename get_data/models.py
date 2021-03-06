from django.db import models
from django.core import validators
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)
from django.contrib.auth.models import User


class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):

        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, **extra_fields):

        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        extra_fields.setdefault("role", User.USER)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):

        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("role", User.ADMIN)
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)

    def update_ozon_user(self, ozon_id, api_key):

        ozon_user = self.update(ozon_id=ozon_id, api_key=api_key)
        return ozon_user


class User(AbstractBaseUser, PermissionsMixin):

    USER = "user"
    ADMIN = "admin"
    ROLE = [
        (USER, "user"),
        (ADMIN, "admin"),
    ]

    email = models.EmailField(
        db_index=True,
        validators=[validators.validate_email],
        unique=True,
        blank=False,
    )
    first_name = models.CharField(
        max_length=100, blank=True, null=True, verbose_name="Имя"
    )
    last_name = models.CharField(
        max_length=100, blank=True, null=True, verbose_name="Фамилия"
    )
    patronymic = models.CharField(
        max_length=100, blank=True, null=True, verbose_name="Отчество"
    )

    role = models.CharField(
        choices=ROLE,
        default="user",
        max_length=20,
        blank=False,
        null=False,
        verbose_name="Роль",
    )

    date_create = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name="Дата регистрации")
    is_staff = models.BooleanField(default=False, verbose_name="Персонал")
    is_active = models.BooleanField(default=True, verbose_name='Активный пользователь')
    is_superuser = models.BooleanField(default=False, verbose_name="Администратор")
    post_agreement = models.BooleanField(default=True, verbose_name="Согласие на отправку писем")
    card = models.CharField(max_length=16, null=True, blank=True, verbose_name="Карта")
    card_year = models.CharField(max_length=5, null=True, blank=True, verbose_name="Срок действия карты", default="Null")
    card_ovner = models.CharField(max_length=250, null=True, blank=True, verbose_name="Данные владельца карты", default="Null")

    ozon_id = models.IntegerField(verbose_name="ID пользователя OZON", default=0, blank=True, null=True)
    api_key = models.CharField(max_length=500, verbose_name="API ключ OZON", default='Null', blank=True, null=True)

    name_org = models.CharField(max_length=256, null=True, blank=True, verbose_name="Название организации")
    inn = models.CharField(max_length=12, null=True, blank=True, verbose_name="ИНН")
    orgn = models.CharField(max_length=12, null=True, blank=True, verbose_name="ОРГН")
    kpp = models.CharField(max_length=9, null=True, blank=True, verbose_name="КПП")
    bank_account = models.CharField(max_length=20, null=True, blank=True, verbose_name="Номер счёта")
    bank = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Название банка")
    correspondent_bank_account = models.CharField(max_length=20, null=True, blank=True,
                                                  verbose_name="Кореспондентский счёт")
    bik = models.CharField(max_length=8, null=True, blank=True, verbose_name="БИК")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["password"]
    objects = UserManager()

    @classmethod
    def transaction_data(obj):
        user_transaction_query = Transaction.objects.filter(id_user=1)
        return_transaction = ''

        for user_transaction in user_transaction_query:
            return_transaction = return_transaction + f'Номер транзакции:  {user_transaction.transaction_number}, ' \
                                                      f'\n Дата транзакции:  {user_transaction.date_issued}, \n ' \
                                                      f'Тип оплаты:  {user_transaction.type}, \n Тариф: ' \
                                                      f'  {user_transaction.rate}, \n Сумма:  {user_transaction.summ} \n \n \n'

        return return_transaction

    class Meta:
        verbose_name = "пользователя"
        verbose_name_plural = "пользователи"
        ordering = ("id",)

    def __str__(self):
        return self.email

class PaymentType(models.Model):

    type = models.CharField(max_length=100, default='card', verbose_name="Способ оплаты")
    description = models.CharField(max_length=1000, verbose_name="Описание способа оплаты")

    def __str__(self):
        return str(self.type)

    class Meta:
        verbose_name = 'способ оплаты'
        verbose_name_plural = 'способы оплаты'
        ordering = ['type']

class Transaction(models.Model):

    id_user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="user_transaction", verbose_name='Пользователь')
    transaction_number = models.CharField(max_length=200, default='000000000000000', verbose_name="Номер транзакции")
    date_issued = models.DateTimeField(auto_now_add=True, verbose_name="Дата выполнения")
    type = models.ForeignKey(PaymentType, on_delete=models.CASCADE, blank=True, null=True, related_name="payment_transaction", verbose_name='Способ оплаты')
    rate = models.CharField(max_length=100, default='base', verbose_name="Тариф")
    summ = models.IntegerField(default=0, verbose_name='Сумма списания')
    status = models.CharField(max_length=100, default='wait', verbose_name='Статус')


    def __str__(self):
        return str(self.transaction_number)

    class Meta:
        verbose_name = 'транзакцию'
        verbose_name_plural = 'транзакции'
        ordering = ['id']
    