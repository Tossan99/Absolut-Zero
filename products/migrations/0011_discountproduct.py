# Generated by Django 4.2.11 on 2024-04-28 15:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_alter_productrating_rating_productreview'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiscountProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discount_price', models.DecimalField(decimal_places=2, help_text='The discounted price of the product', max_digits=7)),
                ('discount_percentage', models.DecimalField(decimal_places=2, help_text='The percentage of the discount applied to the product', max_digits=4)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='discounts', to='products.product')),
            ],
        ),
    ]