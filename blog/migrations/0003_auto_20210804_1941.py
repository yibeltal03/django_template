# Generated by Django 3.2.5 on 2021-08-04 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210804_1920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='blogs',
            name='time',
            field=models.DateField(),
        ),
    ]
