# Generated by Django 5.0.7 on 2024-07-12 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NetworkInformation',
            fields=[
                ('config_number', models.IntegerField(primary_key=True, serialize=False)),
                ('date_recorded', models.DateField()),
                ('status_bcc', models.CharField(choices=[('DONE', 'DONE'), ('PENDING', 'PENDING'), ('VOID', 'VOID')], default='PENDING', max_length=20)),
                ('status_route', models.CharField(choices=[('DONE', 'DONE'), ('PENDING', 'PENDING'), ('VOID', 'VOID')], default='PENDING', max_length=20)),
                ('device_group', models.CharField(max_length=255)),
                ('dhcp_cluster', models.CharField(max_length=255)),
                ('olt_name', models.CharField(max_length=255)),
                ('site', models.CharField(blank=True, max_length=255, null=True)),
                ('p2p_primary', models.CharField(max_length=255)),
                ('p2p_secondary', models.CharField(max_length=255)),
                ('mgmt_vlan100', models.CharField(max_length=255)),
                ('mgmt_subnet', models.IntegerField()),
                ('mgmt_ip_range', models.CharField(max_length=255)),
                ('mgmt_netmask', models.CharField(max_length=255)),
                ('mgmt_size', models.IntegerField()),
                ('cpe_vlan10', models.CharField(max_length=255)),
                ('cpe_subnet', models.CharField(max_length=255)),
                ('cpe_ip_range', models.CharField(max_length=255)),
                ('cpe_netmask', models.CharField(max_length=255)),
                ('cpe_size', models.IntegerField()),
            ],
        ),
    ]
