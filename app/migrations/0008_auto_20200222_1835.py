# Generated by Django 3.0.3 on 2020-02-22 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20200222_0118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lawandeconomics',
            name='professorName',
            field=models.CharField(default='김용규', max_length=50),
        ),
    ]
