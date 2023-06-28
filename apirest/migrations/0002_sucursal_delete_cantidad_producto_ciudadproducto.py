# Generated by Django 4.2.1 on 2023-06-24 10:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apirest', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ciudad', models.CharField(max_length=40, unique=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Cantidad',
        ),
        migrations.AddField(
            model_name='producto',
            name='ciudadProducto',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='apirest.sucursal'),
            preserve_default=False,
        ),
    ]