# Generated by Django 4.0.3 on 2022-04-04 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default.ngg', upload_to='profile_pics'),
        ),
    ]