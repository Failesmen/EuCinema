# Generated by Django 4.0.1 on 2022-01-25 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contato',
            name='subject',
            field=models.TextField(default=2),
            preserve_default=False,
        ),
    ]
