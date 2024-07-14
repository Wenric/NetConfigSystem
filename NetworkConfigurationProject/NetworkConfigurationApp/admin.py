from django.contrib import admin
from .models import NetworkInformation, DeviceGroup, DHCPCluster

@admin.register(NetworkInformation)
class NetworkInformationAdmin(admin.ModelAdmin):
    list_display = ['config_number', 'date_recorded', 'date_assigned', 'approval_status', 'status_bcc', 'status_route', 'device_group', 'dhcp_cluster', 'olt_name']
    search_fields = ['config_number', 'olt_name']
    list_filter = ['approval_status', 'status_bcc', 'status_route', 'device_group', 'dhcp_cluster']

@admin.register(DeviceGroup)
class DeviceGroupAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(DHCPCluster)
class DHCPClusterAdmin(admin.ModelAdmin):
    list_display = ['name']
