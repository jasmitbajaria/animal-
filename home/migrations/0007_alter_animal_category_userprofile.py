# Generated by Django 5.0.2 on 2025-03-15 05:40

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_animal_category_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='category',
            field=models.CharField(choices=[('air', 'Air'), ('water', 'Water'), ('land', 'Land'), ('aerial', 'Aerial'), ('terrestrial', 'Terrestrial'), ('aquatic', 'Aquatic')], max_length=20),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.PositiveIntegerField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
