# Generated by Django 4.1.2 on 2022-10-19 18:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_rename_cat_id_channel_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channel',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='channels', to='core.category'),
        ),
    ]
