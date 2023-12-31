# Generated by Django 4.2.7 on 2023-11-10 19:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cities_light', '0011_alter_city_country_alter_city_region_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CountryTaxesConcept',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('rate_percentage', models.DecimalField(decimal_places=8, max_digits=20)),
                ('rate_fixed', models.DecimalField(decimal_places=8, max_digits=20)),
                ('rate_formula', models.CharField(max_length=100)),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cities_light.country')),
            ],
        ),
    ]
