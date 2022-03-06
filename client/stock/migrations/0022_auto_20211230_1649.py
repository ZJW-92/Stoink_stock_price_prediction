# Generated by Django 3.2.9 on 2021-12-30 15:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0021_auto_20211230_1510'),
    ]

    operations = [
        migrations.AddField(
            model_name='aimodel',
            name='evaluation_dataset',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='evaluation_dataset', to='stock.dataset'),
        ),
        migrations.AlterField(
            model_name='aimodel',
            name='dataset',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='dataset', to='stock.dataset'),
        ),
    ]