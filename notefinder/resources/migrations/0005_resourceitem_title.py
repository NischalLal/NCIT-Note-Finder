# Generated by Django 2.0.5 on 2018-05-25 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0004_resourceurl_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='resourceitem',
            name='title',
            field=models.CharField(default='Nischal', max_length=100),
            preserve_default=False,
        ),
    ]
