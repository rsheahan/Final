# Generated by Django 2.1.3 on 2018-11-30 20:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='picture',
            old_name='pic_descrip',
            new_name='pic_description',
        ),
    ]
