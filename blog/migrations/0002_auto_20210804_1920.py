# Generated by Django 3.2.5 on 2021-08-04 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='description',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='blogs',
            name='time',
            field=models.DateField(auto_now=True),
        ),
    ]