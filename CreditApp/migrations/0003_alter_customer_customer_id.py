# Generated by Django 4.2.8 on 2023-12-16 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CreditApp', '0002_alter_customer_customer_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customer_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]