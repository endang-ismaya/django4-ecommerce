# Generated by Django 4.1a1 on 2022-06-16 15:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("app_ecommerce", "0002_product_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="seller_name",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
