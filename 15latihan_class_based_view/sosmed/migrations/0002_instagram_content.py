# Generated by Django 3.1.4 on 2021-01-14 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sosmed', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='instagram',
            name='content',
            field=models.CharField(default='programming', max_length=50),
            preserve_default=False,
        ),
    ]