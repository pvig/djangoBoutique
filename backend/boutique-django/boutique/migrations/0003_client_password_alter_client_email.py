# Generated by Django 5.0.2 on 2024-02-14 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boutique', '0002_alter_client_datecommande1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='password',
            field=models.CharField(default='a', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='client',
            name='email',
            field=models.CharField(blank=True, default='a', max_length=100),
            preserve_default=False,
        ),
    ]
