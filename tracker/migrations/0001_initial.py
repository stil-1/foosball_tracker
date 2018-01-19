# Generated by Django 2.0.1 on 2018-01-19 08:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('mu', models.FloatField()),
                ('sigma', models.FloatField()),
                ('wins', models.IntegerField()),
                ('losses', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('players', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team', to='tracker.Player')),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='loser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='games_lost', to='tracker.Team'),
        ),
        migrations.AddField(
            model_name='game',
            name='winner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='games_won', to='tracker.Team'),
        ),
    ]
