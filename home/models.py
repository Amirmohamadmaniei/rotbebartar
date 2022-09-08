from django.db import models


class ContactUs(models.Model):
    full_name = models.CharField(max_length=150, verbose_name='نام کامل')
    email = models.EmailField(verbose_name='ایمیل')
    phone = models.CharField(max_length=11, verbose_name='تلفن')
    subject = models.CharField(max_length=80, verbose_name='موضوع')
    body = models.TextField(verbose_name='متن پیام')

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = 'پیام ارسالی'
        verbose_name_plural = 'پیام های ارسالی '
