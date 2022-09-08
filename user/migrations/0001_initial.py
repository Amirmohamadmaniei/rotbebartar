# Generated by Django 4.1 on 2022-09-07 15:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('phone', models.CharField(max_length=11, unique=True, verbose_name='شماره تلفن')),
                ('first_name', models.CharField(blank=True, max_length=150, null=True, verbose_name='نام')),
                ('last_name', models.CharField(blank=True, max_length=180, null=True, verbose_name='نام خانوادگی')),
                ('age', models.IntegerField(blank=True, null=True, verbose_name='سن')),
                ('ostan', models.CharField(blank=True, max_length=100, null=True, verbose_name='استان محل سکونت')),
                ('city', models.CharField(blank=True, max_length=100, null=True, verbose_name='شهر محل سکونت')),
                ('sex', models.CharField(choices=[('None', 'نامشخص'), ('male', 'مرد'), ('female', 'زن')], default=0, max_length=10, verbose_name='جنسیت')),
                ('major_high_school', models.CharField(blank=True, choices=[('riazi', 'ریاضی'), ('tajrobi', 'تجربی'), ('ensani', 'انسانی'), ('fani', 'فنی و حرفه ای'), ('tarbiat_badani', 'تربیت بدنی')], max_length=180, null=True, verbose_name='رشته تحصیلی دبیرستان')),
                ('type', models.CharField(choices=[('student', 'دانش اموز'), ('consultant', 'مشاور')], default='student', max_length=10, verbose_name='نوع کاربر')),
                ('is_admin', models.BooleanField(default=False, verbose_name='اذمین')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال')),
                ('slug', models.SlugField(allow_unicode=True, blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'verbose_name': 'کاربر',
                'verbose_name_plural': 'کاربران',
            },
        ),
        migrations.CreateModel(
            name='ConsultantProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capacity', models.IntegerField(default=0, verbose_name='ظرفیت قبولی دانش اموزان')),
                ('status', models.BooleanField(default=False, verbose_name='وضعبت فعالیت')),
                ('university', models.CharField(blank=True, max_length=150, null=True)),
                ('major_university', models.CharField(max_length=100, verbose_name='رشته دانشگاهی')),
                ('image', models.ImageField(upload_to='img/consultant', verbose_name='عکس پروفایل')),
                ('description', models.TextField(verbose_name='سوابق تحصیلی')),
                ('price', models.CharField(blank=True, max_length=15, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='ایمیل')),
                ('tel', models.CharField(blank=True, max_length=180, null=True, verbose_name='شماره تماس')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'اطلاعات مشاور',
            },
        ),
        migrations.CreateModel(
            name='StudentProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.CharField(blank=True, choices=[('12', 'پایه دوازدهم'), ('11', 'پایه یازدهم'), ('10', 'پایه دهم'), ('posht_konkoor', 'پشت کنکوری')], max_length=50, null=True, verbose_name='پایه تحصیلی')),
                ('time_consultation', models.CharField(blank=True, choices=[('30', 'یک ماهه'), ('60', 'دو ماهه'), ('90', 'سه ماهه'), ('180', 'شش ماهه'), ('360', 'یک شاله')], max_length=20, null=True)),
                ('time_end', models.DateTimeField(blank=True, null=True)),
                ('consultant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='students', to='user.consultantprofile', verbose_name='مشاور')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'اطلاعات دانش آموز',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='متن پیام')),
                ('status', models.BooleanField(default=False, verbose_name='انتشار')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('consultant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='user.consultantprofile', verbose_name='مشاور')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='user.studentprofile', verbose_name='کاربر')),
            ],
            options={
                'verbose_name': 'نظر',
                'verbose_name_plural': 'نظر ها',
            },
        ),
    ]
