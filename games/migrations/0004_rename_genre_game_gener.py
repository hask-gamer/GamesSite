# Generated by Django 5.0.1 on 2024-02-15 11:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0003_rename_gener_game_genre_gamereviews'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='genre',
            new_name='gener',
        ),
    ]
