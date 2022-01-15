# Generated by Django 3.2 on 2021-12-20 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_learning_prerequisite_tag_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='slug',
            field=models.CharField(max_length=50, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='learning',
            name='description',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='prerequisite',
            name='description',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='tag',
            name='description',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='video',
            name='video_id',
            field=models.CharField(max_length=100),
        ),
    ]