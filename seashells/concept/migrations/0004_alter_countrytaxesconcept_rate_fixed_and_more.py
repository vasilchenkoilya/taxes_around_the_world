# Generated by Django 4.2.7 on 2023-11-11 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('concept', '0003_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='countrytaxesconcept',
            name='rate_fixed',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='countrytaxesconcept',
            name='rate_formula',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='countrytaxesconcept',
            name='rate_percentage',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=20, null=True),
        ),
    ]