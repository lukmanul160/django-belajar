# Generated by Django 3.1.4 on 2021-01-02 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='alamat',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
