from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from .managers import CustomUserManager


class CustomUser(AbstractBaseUser):
    phone = models.CharField(max_length=11, unique=True, verbose_name='شماره تلفن')

    first_name = models.CharField(max_length=150, null=True, blank=True, verbose_name='نام')
    last_name = models.CharField(max_length=180, null=True, blank=True, verbose_name='نام خانوادگی')
    age = models.IntegerField(null=True, blank=True, verbose_name='سن')
    sex_type = (
        ('None', 'نامشخص'),
        ('male', 'مرد'),
        ('female', 'زن'),
    )
    sex = models.CharField(max_length=10, choices=sex_type, default=0, verbose_name='جنسیت')
    major = models.CharField(max_length=180, null=True, blank=True, verbose_name='رشته تحصیلی')

    type_user = (
        ('student', 'دانش اموز'),
        ('consultant', 'مشاور'),
    )
    type = models.CharField(max_length=10, choices=type_user, default=0, verbose_name='نوع کاربر')

    consultant = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='students',
                                   verbose_name='مشاور')

    is_admin = models.BooleanField(default=False, verbose_name='اذمین')
    is_active = models.BooleanField(default=True, verbose_name='فعال')

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ()

    objects = CustomUserManager()

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

    def __str__(self):
        return self.phone

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='img/consultant', verbose_name='عکس پروفایل')
    records = models.CharField(max_length=180, null=True, blank=True, verbose_name='سوابق تحصیلی')
    telegram = models.CharField(max_length=180, null=True, blank=True, verbose_name='تلگرام')
    whatsapp = models.CharField(max_length=180, null=True, blank=True, verbose_name='واتس اپ')
    instagram = models.CharField(max_length=180, null=True, blank=True, verbose_name='اینستاگرام')
    tel = models.CharField(max_length=180, null=True, blank=True, verbose_name='شماره تماس')

    class Meta:
        verbose_name = 'اطلاعات مشاور'
