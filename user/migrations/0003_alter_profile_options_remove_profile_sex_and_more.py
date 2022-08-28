# Generated by Django 4.1 on 2022-08-26 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_customuser_type'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name': 'اطلاعات مشاور'},
        ),
        migrations.RemoveField(
            model_name='profile',
            name='sex',
        ),
        migrations.AddField(
            model_name='customuser',
            name='sex',
            field=models.CharField(blank=True, choices=[('male', 'مرد'), ('female', 'زن')], max_length=10, null=True),
        ),
    ]