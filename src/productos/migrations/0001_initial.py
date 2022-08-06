# Generated by Django 4.0.6 on 2022-08-06 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductosDetailing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
                ('marca', models.CharField(max_length=150)),
                ('precio', models.FloatField()),
                ('tipo', models.DateField(max_length=10)),
                ('stock', models.IntegerField(default=50)),
            ],
        ),
    ]
