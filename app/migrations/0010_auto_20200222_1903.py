# Generated by Django 3.0.3 on 2020-02-22 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20200222_1838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lawandeconomics',
            name='lectureName',
            field=models.CharField(default='법과경제학', max_length=200),
        ),
        migrations.AlterField(
            model_name='physicsexperiment',
            name='lectureName',
            field=models.CharField(default='물리학실험', max_length=200),
        ),
        migrations.AlterField(
            model_name='physicsexperiment',
            name='professorName',
            field=models.CharField(default='태원이', max_length=50),
        ),
        migrations.AlterField(
            model_name='webprogramming',
            name='lectureName',
            field=models.CharField(default='웹프로그래밍', max_length=200),
        ),
        migrations.AlterField(
            model_name='webprogramming',
            name='professorName',
            field=models.CharField(default='혜선이', max_length=50),
        ),
    ]
