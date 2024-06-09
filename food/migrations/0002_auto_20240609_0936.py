# Generated by Django 3.1.2 on 2024-06-09 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='data_alpha_carotene',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='data_beta_carotene',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='data_beta_cryptoxanthin',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='data_cholesterol',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='data_lutein_and_zeaxanthin',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='data_lycopene',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='data_major_minerals_calcium',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='data_major_minerals_magnesium',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='data_major_minerals_phosphorus',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='data_major_minerals_potassium',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='data_major_minerals_sodium',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='data_retinol',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='data_vitamins_vitamin_a_rae',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
