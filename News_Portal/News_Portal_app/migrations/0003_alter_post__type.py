# Generated by Django 4.1.5 on 2023-01-31 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('News_Portal_app', '0002_alter_post__type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='_type',
            field=models.CharField(choices=[('AR', 'статья'), ('NE', 'новость')], max_length=2),
        ),
    ]