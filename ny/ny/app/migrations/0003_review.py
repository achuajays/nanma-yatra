# Generated by Django 4.1.5 on 2023-04-30 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_a_price_s_dt'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reviewer_name', models.CharField(max_length=100)),
                ('review_date', models.DateField()),
                ('product_or_service', models.CharField(max_length=200)),
                ('rating', models.IntegerField()),
                ('review_content', models.TextField()),
            ],
        ),
    ]