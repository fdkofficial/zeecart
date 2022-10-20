# Generated by Django 4.0.3 on 2022-04-30 07:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('images', models.ImageField(upload_to='photos/product')),
                ('description', models.TextField(max_length=200)),
                ('slug', models.SlugField(max_length=100)),
                ('price', models.IntegerField()),
                ('stock', models.IntegerField()),
                ('is_available', models.BooleanField(default=True)),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.category')),
            ],
        ),
    ]