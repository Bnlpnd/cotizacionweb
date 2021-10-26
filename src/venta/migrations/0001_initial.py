# Generated by Django 3.1.7 on 2021-10-25 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codventa', models.CharField(default='00000', max_length=5)),
                ('fechaventa', models.DateTimeField(auto_now_add=True)),
                ('preciototal', models.DecimalField(decimal_places=2, default=0.0, max_digits=1000)),
                ('montocancelado', models.DecimalField(decimal_places=2, default=0.0, max_digits=1000)),
                ('saldo', models.DecimalField(decimal_places=2, default=0.0, max_digits=1000)),
                ('estado', models.CharField(default='PEN', max_length=3)),
            ],
        ),
    ]
