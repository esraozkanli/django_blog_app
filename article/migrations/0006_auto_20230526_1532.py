# Generated by Django 3.2.10 on 2023-05-26 12:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_auto_20230525_1822'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-created_date']},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-comment_created_date']},
        ),
    ]
