# Generated by Django 3.1 on 2020-09-05 13:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('poker_games', '0001_initial'),
        ('polls', '0002_create_model_vote'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='poker_game',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='poker_games.pokergame'),
        ),
    ]
