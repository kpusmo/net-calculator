import socket
import re


def get_min_host_address(network_address):
    network_address_parts = network_address.split('.')
    network_address_parts[3] = str(int(network_address_parts[3]) + 1)
    return '.'.join(network_address_parts)


def get_max_host_address(broadcast_address):
    broadcast_address_parts = broadcast_address.split('.')
    broadcast_address_parts[3] = str(int(broadcast_address_parts[3]) - 1)
    return '.'.join(broadcast_address_parts)


def get_host_count(min_host_address, max_host_address):
    min_host_address_parts = min_host_address.split(".")
    max_host_address_parts = max_host_address.split(".")

    if max_host_address_parts[2] == min_host_address_parts[2] and max_host_address_parts[1] == min_host_address_parts[1] and \
            max_host_address_parts[0] == min_host_address_parts[0]:
        host_count = (int(max_host_address_parts[3]) - int(min_host_address_parts[3])) + 1
        return host_count

    host_count = 256 - int(min_host_address_parts[3])
    for i in [2, 1, 0]:
        net_count = int(max_host_address_parts[i]) - int(min_host_address_parts[i])
        host_count += net_count * pow(256, 3 - i)
    host_count -= 255 - int(max_host_address_parts[3])
    return host_count


def get_ip_address_with_cidr():
    return socket.gethostbyname(socket.gethostname()) + '/24'


def get_cidr_from_ip_with_cidr(ip):
    return (ip.split('/'))[1]


def get_ip_from_ip_with_cidr(ip):
    return (ip.split('/'))[0]


def is_valid_ip(ip):
    ip_parts = ip.split("/")
    regex = re.compile("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")
    parts = ip_parts[0].split('.')
    return is_cidr_valid(ip_parts[1]) and re.match(regex, ip_parts[0]) and len(parts) == 4 and all(
        0 <= int(part) < 256 for part in parts)


def is_cidr_valid(cidr):
    return 0 <= int(cidr) < 33
