from datetime import datetime, timedelta
from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from .managers import CustomUserManager
from home import information


class CustomUser(AbstractBaseUser):
    phone = models.CharField(max_length=11, unique=True, verbose_name='شماره تلفن')

    first_name = models.CharField(max_length=150, null=True, blank=True, verbose_name='نام')
    last_name = models.CharField(max_length=180, null=True, blank=True, verbose_name='نام خانوادگی')
    age = models.IntegerField(null=True, blank=True, verbose_name='سن')
    ostan = models.CharField(max_length=100, null=True, blank=True, verbose_name='استان محل سکونت')
    city = models.CharField(max_length=100, null=True, blank=True, verbose_name='شهر محل سکونت')

    sex = models.CharField(max_length=10, choices=information.sex_type, default=0, verbose_name='جنسیت')

    major_high_school = models.CharField(max_length=180, choices=information.major_high_schools, null=True, blank=True,
                                         verbose_name='رشته تحصیلی دبیرستان')

    type = models.CharField(max_length=10, choices=information.type_user, default='student', verbose_name='نوع کاربر')

    is_admin = models.BooleanField(default=False, verbose_name='اذمین')
    is_active = models.BooleanField(default=True, verbose_name='فعال')

    slug = models.SlugField(allow_unicode=True, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True)

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
        if self.first_name is None and self.last_name is None:
            return 'نامشخص'
        elif self.first_name is None and self.last_name is not None:
            return self.last_name
        elif self.first_name is not None and self.last_name is None:
            return self.first_name
        return f'{self.first_name} {self.last_name}'

    def get_absolute_url(self):
        return reverse('consultant:consultant_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.get_full_name(), allow_unicode=True)
        return super(CustomUser, self).save(*args, **kwargs)


class ConsultantProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    capacity = models.IntegerField(default=0, verbose_name='ظرفیت قبولی دانش اموزان')
    status = models.BooleanField(default=False, verbose_name='وضعبت فعالیت')
    university = models.CharField(max_length=150)
    major_university = models.CharField(max_length=100, verbose_name='رشته دانشگاهی')
    image = models.ImageField(upload_to='img/consultant', null=True, blank=True, verbose_name='عکس پروفایل')
    description = models.TextField(verbose_name='سوابق تحصیلی')
    price = models.CharField(max_length=15)
    email = models.EmailField(verbose_name='ایمیل')
    tel = models.CharField(max_length=180, verbose_name='شماره تماس')

    class Meta:
        verbose_name = 'اطلاعات مشاور'

    def __str__(self):
        return self.user.get_full_name()

    def get_capacity(self):
        return self.capacity - self.students.all().count()


class StudentProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    grade = models.CharField(max_length=50, null=True, blank=True, choices=information.grades,
                             verbose_name='پایه تحصیلی')
    consultant = models.ForeignKey(ConsultantProfile, on_delete=models.SET_NULL, null=True, blank=True,
                                   related_name='students', verbose_name='مشاور')
    time_consultation = models.CharField(max_length=20, null=True, blank=True, choices=information.time_consultation)
    time_end = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = 'اطلاعات دانش آموز'

    def __str__(self):
        return self.user.get_full_name()

    def is_subscriber(self):
        if self.time_end is not None:
            if self.time_end.date() >= datetime.today().date():
                return True
            return False

    def end_subscribe(self):
        self.consultant = None
        self.time_consultation = None
        self.time_end = None
        self.save()

    def subscriber_to_end(self):
        time = self.time_end.date() - datetime.today().date()
        if time.days == 0:
            return f'{datetime.now().time().hour - self.time_end.time().hour} ساعت'
        return f'{time.days} روز'


class Comment(models.Model):
    user = models.ForeignKey(StudentProfile, on_delete=models.CASCADE,
                             related_name='comments', verbose_name='کاربر')
    consultant = models.ForeignKey(ConsultantProfile, on_delete=models.CASCADE,
                                   related_name='comments', verbose_name='مشاور')
    text = models.TextField(verbose_name='متن پیام')
    status = models.BooleanField(default=False, verbose_name='انتشار')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'نظر'
        verbose_name_plural = 'نظر ها'

    def __str__(self):
        return f'{self.user} - {self.text[:20]}'
