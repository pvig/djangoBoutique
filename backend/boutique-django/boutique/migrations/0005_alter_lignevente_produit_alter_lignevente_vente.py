# Generated by Django 5.0.2 on 2024-02-21 18:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boutique', '0004_remove_client_datecommande1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lignevente',
            name='produit',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='boutique.produit'),
        ),
        migrations.AlterField(
            model_name='lignevente',
            name='vente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lignesVente', to='boutique.vente'),
        ),
    ]
