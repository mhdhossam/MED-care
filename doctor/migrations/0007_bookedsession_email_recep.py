# Generated by Django 4.1.1 on 2022-12-29 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0006_bookedsession'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookedsession',
            name='email_recep',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
