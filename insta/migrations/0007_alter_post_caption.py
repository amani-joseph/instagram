# Generated by Django 4.0.3 on 2022-04-04 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0006_remove_post_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='caption',
            field=models.CharField(blank=True, default='caption', max_length=200, unique=True),
            preserve_default=False,
        ),
    ]