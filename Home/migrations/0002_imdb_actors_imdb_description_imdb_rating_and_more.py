# Generated by Django 4.2.14 on 2024-08-01 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='imdb',
            name='actors',
            field=models.CharField(default='Unknown', max_length=500),
        ),
        migrations.AddField(
            model_name='imdb',
            name='description',
            field=models.TextField(default='Unknown'),
        ),
        migrations.AddField(
            model_name='imdb',
            name='rating',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='imdb',
            name='revenue',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='imdb',
            name='runtime',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='imdb',
            name='votes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='imdb',
            name='director',
            field=models.CharField(default='Unknown', max_length=200),
        ),
        migrations.AlterField(
            model_name='imdb',
            name='genre',
            field=models.CharField(default='Unknown', max_length=200),
        ),
        migrations.AlterField(
            model_name='imdb',
            name='rank',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='imdb',
            name='title',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='imdb',
            name='year',
            field=models.IntegerField(default=0),
        ),
    ]
