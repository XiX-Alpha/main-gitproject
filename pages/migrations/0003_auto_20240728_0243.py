# Generated by Django 3.0.7 on 2024-07-28 02:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20240727_1341'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='facebok_link',
            new_name='facebook_link',
        ),
    ]
