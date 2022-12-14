# Generated by Django 4.1 on 2022-09-08 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=150, verbose_name='نام کامل')),
                ('email', models.EmailField(max_length=254, verbose_name='ایمیل')),
                ('phone', models.CharField(max_length=11, verbose_name='تلفن')),
                ('subject', models.CharField(max_length=80, verbose_name='موضوع')),
                ('body', models.TextField(verbose_name='متن پیام')),
            ],
            options={
                'verbose_name': 'پیام ارسالی',
                'verbose_name_plural': 'پیام های ارسالی ',
            },
        ),
    ]
