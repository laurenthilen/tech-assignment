# Generated by Django 4.0 on 2021-03-19 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('headcount', '0007_alter_company_company_alter_user_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='month',
            field=models.DateField(),
        ),
    ]