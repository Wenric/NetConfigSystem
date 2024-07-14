from django.db import models
import ipaddress
from django.contrib.auth.models import User

class DeviceGroup(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class DHCPCluster(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class NetworkInformation(models.Model):
    device_group = models.ForeignKey(DeviceGroup, on_delete=models.CASCADE)
    dhcp_cluster = models.ForeignKey(DHCPCluster, on_delete=models.CASCADE)
    config_number = models.AutoField(primary_key=True)
    date_recorded = models.DateField(auto_now_add=True)
    date_assigned = models.DateField()
    approval_status = models.CharField(max_length=20, choices=[
        ('APPROVED', 'APPROVED'),
        ('PENDING', 'PENDING'),
        ('DENIED', 'DENIED'),
    ], default='PENDING')
    status_bcc = models.CharField(max_length=20, choices=[
        ('DONE', 'DONE'),
        ('PENDING', 'PENDING'),
        ('VOID', 'VOID'),
    ], default='PENDING')
    status_route = models.CharField(max_length=20, choices=[
        ('DONE', 'DONE'),
        ('PENDING', 'PENDING'),
        ('VOID', 'VOID'),
    ], default='PENDING')
    olt_name = models.CharField(max_length=255)
    site = models.CharField(max_length=255, blank=True, null=True)
    p2p_primary = models.CharField(max_length=255)
    p2p_secondary = models.CharField(max_length=255, blank=True, null=True)
    mgmt_vlan100 = models.CharField(max_length=255)
    mgmt_netmask = models.CharField(max_length=255)
    mgmt_subnet = models.IntegerField()
    cpe_vlan10 = models.CharField(max_length=255)
    cpe_netmask = models.CharField(max_length=255)
    cpe_subnet = models.IntegerField()
    mgmt_ip_range = models.CharField(max_length=255, blank=True, null=True)
    mgmt_size = models.IntegerField(blank=True, null=True)
    cpe_ip_range = models.CharField(max_length=255, blank=True, null=True)
    cpe_size = models.IntegerField(blank=True, null=True)
    submitted_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.mgmt_ip_range = self.calculate_ip_range(self.mgmt_vlan100, self.mgmt_subnet)
        self.mgmt_size = self.calculate_network_size(self.mgmt_subnet)
        self.cpe_ip_range = self.calculate_ip_range(self.cpe_vlan10, self.cpe_subnet)
        self.cpe_size = self.calculate_network_size(self.cpe_subnet)
        super().save(*args, **kwargs)

    def calculate_network_size(self, prefix_length):
        # Calculate the number of hosts in the subnet (excluding network and broadcast addresses)
        return 2 ** (32 - prefix_length) - 2

    def calculate_ip_range(self, vlan_ip, prefix_length):
        network = ipaddress.IPv4Network(f"{vlan_ip}/{prefix_length}", strict=False)
        # Calculate first and last usable IP addresses
        first_usable_ip = network.network_address + 1
        last_usable_ip = network.broadcast_address - 1
        return f"{first_usable_ip} - {last_usable_ip}"

    def __str__(self):
        return f"Network Information - {self.config_number}"
