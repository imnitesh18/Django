# Generated by Django 5.0.1 on 2024-04-09 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_blogpost'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cookie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('value', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
