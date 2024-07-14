from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import NetworkInformation, DeviceGroup, DHCPCluster
from django.contrib import messages
from datetime import date
from django.contrib.auth import authenticate, login, logout
from .decorators import role_required
from .forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.http import HttpResponseForbidden

@login_required
def home_page(request):
    configs = NetworkInformation.objects.all()
    device_groups = DeviceGroup.objects.all()
    dhcp_clusters = DHCPCluster.objects.all()

    pending_approvals_count = configs.filter(approval_status='PENDING').count()
    status_bcc_done_count = configs.filter(status_bcc='DONE').count()
    status_bcc_pending_count = configs.filter(status_bcc='PENDING').count()
    status_bcc_void_count = configs.filter(status_bcc='VOID').count()
    status_route_done_count = configs.filter(status_route='DONE').count()
    status_route_pending_count = configs.filter(status_route='PENDING').count()
    status_route_void_count = configs.filter(status_route='VOID').count()

    is_admin = request.user.groups.filter(name='admin').exists()

    return render(request, 'NetworkConfigurationApp/home_page.html', {
        'configs': configs,
        'device_groups': device_groups,
        'dhcp_clusters': dhcp_clusters,
        'pending_approvals_count': pending_approvals_count,
        'status_bcc_done_count': status_bcc_done_count,
        'status_bcc_pending_count': status_bcc_pending_count,
        'status_bcc_void_count': status_bcc_void_count,
        'status_route_done_count': status_route_done_count,
        'status_route_pending_count': status_route_pending_count,
        'status_route_void_count': status_route_void_count,
        'is_admin': is_admin,
    })

@login_required
def add_network_config(request):
    if request.method == 'POST':
        new_config = NetworkInformation(
            device_group=DeviceGroup.objects.get(id=request.POST.get('device_group')),
            dhcp_cluster=DHCPCluster.objects.get(id=request.POST.get('dhcp_cluster')),
            olt_name=request.POST.get('olt_name'),
            site=request.POST.get('site'),
            mgmt_vlan100=request.POST.get('mgmt_vlan100'),
            mgmt_netmask=request.POST.get('mgmt_netmask'),
            mgmt_subnet=int(request.POST.get('mgmt_subnet')),
            cpe_vlan10=request.POST.get('cpe_vlan10'),
            cpe_netmask=request.POST.get('cpe_netmask'),
            cpe_subnet=int(request.POST.get('cpe_subnet')),
            p2p_primary=request.POST.get('p2p_primary'),
            p2p_secondary=request.POST.get('p2p_secondary'),
            status_route=request.POST.get('status_route'),
            status_bcc=request.POST.get('status_bcc'),
            date_assigned=request.POST.get('date_assigned'),
            date_recorded=date.today(),
            submitted_by = request.user
        )
        
        new_config.save()
        return redirect(reverse('home_page'))
    else:
        return render(request, 'NetworkConfigurationApp/home_page.html')
    
@login_required
def edit_network_config(request, config_number):
    config = get_object_or_404(NetworkInformation, config_number=config_number)
    if request.method == 'POST':
        config.device_group = DeviceGroup.objects.get(id=request.POST.get('device_group'))
        config.dhcp_cluster = DHCPCluster.objects.get(id=request.POST.get('dhcp_cluster'))
        config.olt_name = request.POST.get('olt_name')
        config.site = request.POST.get('site')
        config.mgmt_vlan100 = request.POST.get('mgmt_vlan100')
        config.mgmt_netmask = request.POST.get('mgmt_netmask')
        config.mgmt_subnet = int(request.POST.get('mgmt_subnet'))
        config.cpe_vlan10 = request.POST.get('cpe_vlan10')
        config.cpe_netmask = request.POST.get('cpe_netmask')
        config.cpe_subnet = int(request.POST.get('cpe_subnet'))
        config.p2p_primary = request.POST.get('p2p_primary')
        config.p2p_secondary = request.POST.get('p2p_secondary')
        config.status_route = request.POST.get('status_route')
        config.status_bcc = request.POST.get('status_bcc')
        config.date_assigned = request.POST.get('date_assigned')
        config.date_recorded = date.today()
        
        config.save()
        return redirect(reverse('home_page'))
    else:
        return render(request, 'NetworkConfigurationApp/home_page.html')
    

def custom_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home_page')  # Redirect to your desired page after login
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'NetworkConfigurationApp/login.html')


@login_required
@role_required(allowed_roles=['admin'])
def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            group = Group.objects.get(id=form.cleaned_data['role'].id)
            user.groups.add(group)
            messages.success(request, 'User registered successfully.')
            return redirect('home_page')  # Redirect to a success page
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = UserRegistrationForm()

    groups = Group.objects.all()
    return render(request, 'NetworkConfigurationApp/register.html', {'form': form, 'groups': groups})


def custom_logout(request):
    logout(request)
    return redirect('custom_login')


@login_required
def change_approval_status(request, config_number, status):
    if request.user.groups.filter(name='admin').exists():
        config = get_object_or_404(NetworkInformation, config_number=config_number)
        config.approval_status = status
        config.save()
        return redirect('home_page')
    return HttpResponseForbidden("You are not allowed to access this page")