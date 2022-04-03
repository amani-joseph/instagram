# Generated by Django 4.0.3 on 2022-04-03 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0002_alter_post_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='hashtags',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='caption',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='comments',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]