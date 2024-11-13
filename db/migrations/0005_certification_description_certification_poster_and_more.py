# Generated by Django 4.2.6 on 2024-11-11 22:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0004_moviedirector_collaboration_years_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='certification',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='certification',
            name='poster',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='director',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='director',
            name='poster',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='genre',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='genre',
            name='poster',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='directors',
            field=models.ManyToManyField(related_name='movies', through='db.MovieDirector', to='db.director'),
        ),
        migrations.AddField(
            model_name='movie',
            name='genres',
            field=models.ManyToManyField(related_name='movies', through='db.MovieGenre', to='db.genre'),
        ),
        migrations.AddField(
            model_name='movie',
            name='stars',
            field=models.ManyToManyField(related_name='movies', through='db.MovieStar', to='db.star'),
        ),
        migrations.AddField(
            model_name='star',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='star',
            name='poster',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='moviedirector',
            name='director',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.director'),
        ),
        migrations.AlterField(
            model_name='moviedirector',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.movie'),
        ),
        migrations.AlterField(
            model_name='moviegenre',
            name='genre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.genre'),
        ),
        migrations.AlterField(
            model_name='moviegenre',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.movie'),
        ),
        migrations.AlterField(
            model_name='moviestar',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.movie'),
        ),
        migrations.AlterField(
            model_name='moviestar',
            name='star',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.star'),
        ),
    ]
