import ipaddress

def calculate_network_size(netmask):
    # Convert netmask to binary string and count the number of '1's
    return 2 ** (32 - sum([bin(int(x)).count('1') for x in netmask.split('.')]))

def calculate_ip_range(subnet, netmask):
    network = ipaddress.IPv4Network(f"{subnet}/{netmask}", strict=False)
    return f"{network.network_address + 1} - {network.broadcast_address - 1}"
