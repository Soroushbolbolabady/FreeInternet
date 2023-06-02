# Generated by Django 4.2.1 on 2023-05-31 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('uuid', models.CharField(max_length=40)),
                ('is_active', models.BooleanField(default=False)),
            ],
        ),
    ]