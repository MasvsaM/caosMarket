# Generated by Django 4.2.1 on 2023-06-24 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apirest', '0002_sucursal_delete_cantidad_producto_ciudadproducto'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='stock',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]