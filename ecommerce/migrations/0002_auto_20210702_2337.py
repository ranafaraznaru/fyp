# Generated by Django 3.2.4 on 2021-07-03 06:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='color',
        ),
        migrations.RemoveField(
            model_name='product',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='product',
            name='size',
        ),
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='count_in_stock',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='/placeholder.png', null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='product',
            name='num_reviews',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='rating',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True),
        ),
    ]
