# Generated by Django 3.2 on 2021-05-10 09:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerDetails',
            fields=[
                ('C_ID', models.CharField(max_length=10, primary_key=True, serialize=False, unique=True)),
                ('Customer_Name', models.CharField(max_length=50)),
                ('PAN', models.CharField(blank=True, max_length=10, unique=True)),
                ('Adhaar', models.CharField(blank=True, max_length=50, unique=True)),
                ('Passport', models.CharField(blank=True, max_length=50, unique=True)),
                ('Residential_Address', models.TextField(blank=True, max_length=500)),
                ('Phone', models.IntegerField(blank=True, unique=True)),
                ('Email', models.CharField(blank=True, max_length=100, unique=True)),
                ('Birth_Date', models.DateField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='INV_DB',
            fields=[
                ('Asset_Name', models.CharField(max_length=70, primary_key=True, serialize=False, unique=True)),
                ('Qty', models.FloatField()),
                ('CP', models.FloatField(blank=True, default=0)),
                ('SP', models.FloatField(blank=True, default=0)),
            ],
        ),
        migrations.CreateModel(
            name='TRX_CENTRAL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TRX_ID', models.CharField(max_length=70, unique=True)),
                ('Name', models.CharField(blank=True, max_length=50)),
                ('Amount_USD', models.FloatField()),
                ('IN_OUT', models.CharField(max_length=7)),
                ('Date_Time_Stamp', models.DateTimeField(auto_now_add=True)),
                ('customer_ID', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='CID', to='application.customerdetails')),
            ],
        ),
    ]