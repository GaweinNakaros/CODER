# Generated by Django 4.0.4 on 2022-06-09 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0003_delete_clientes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('edad', models.IntegerField()),
            ],
        ),
    ]
