# Generated by Django 4.1.7 on 2023-03-30 02:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proxy_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='keytoken',
            name='hostdomain',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proxy_api.hostdomain', to_field='name'),
        ),
    ]
