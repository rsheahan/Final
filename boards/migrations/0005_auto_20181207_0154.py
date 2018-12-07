# Generated by Django 2.1.4 on 2018-12-07 01:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0004_remove_picture_picdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='localUsers',
        ),
    ]