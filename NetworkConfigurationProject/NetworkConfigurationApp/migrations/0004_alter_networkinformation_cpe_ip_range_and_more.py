# Generated by Django 5.0.7 on 2024-07-12 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NetworkConfigurationApp', '0003_alter_networkinformation_config_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='networkinformation',
            name='cpe_ip_range',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='networkinformation',
            name='cpe_netmask',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='networkinformation',
            name='cpe_size',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='networkinformation',
            name='date_assigned',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='networkinformation',
            name='mgmt_ip_range',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='networkinformation',
            name='mgmt_netmask',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='networkinformation',
            name='mgmt_size',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
