# Generated by Django 2.2.4 on 2019-08-11 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20190811_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='upload',
            field=models.FileField(default='static/images/default_avatar.png', upload_to=''),
        ),
    ]
