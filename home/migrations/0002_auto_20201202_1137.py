# Generated by Django 3.0 on 2020-12-02 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='date_published',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
