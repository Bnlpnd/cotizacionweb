# Generated by Django 3.1.7 on 2021-10-24 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Modelo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('descripcion', models.CharField(max_length=500, null=True)),
                ('diaselaboracion', models.IntegerField(default=8)),
            ],
        ),
    ]