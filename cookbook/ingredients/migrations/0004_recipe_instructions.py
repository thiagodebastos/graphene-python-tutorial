# Generated by Django 2.2.4 on 2019-09-01 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ingredients', '0003_auto_20190901_1036'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='instructions',
            field=models.TextField(default=''),
        ),
    ]
