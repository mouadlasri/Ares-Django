# Generated by Django 2.0.1 on 2019-08-26 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20190819_2112'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='link',
            field=models.CharField(default='no link', max_length=120),
            preserve_default=False,
        ),
    ]
