# Generated by Django 3.2 on 2021-05-10 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0003_alter_inv_db_auto_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inv_db',
            name='Asset_Name',
            field=models.CharField(max_length=70),
        ),
    ]
