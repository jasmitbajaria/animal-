# Generated by Django 5.0.2 on 2025-03-08 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='category',
            field=models.CharField(choices=[('Air', 'Air'), ('Water', 'Water'), ('Land', 'Land')], max_length=10),
        ),
        migrations.AlterField(
            model_name='animal',
            name='image1',
            field=models.ImageField(blank=True, null=True, upload_to='animals/'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='animals/'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to='animals/'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='section',
            field=models.CharField(choices=[('Kids', 'Kids'), ('Adults', 'Adults')], max_length=10),
        ),
    ]
