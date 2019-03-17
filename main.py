import sys

from cidr_to_binary_subnet_mask import cidr_to_binary_subnet_mask
from convert_binary_address_to_decimal import convert_binary_address_to_decimal
from convert_decimal_address_to_binary import convert_decimal_address_to_binary
from decimal_to_binary import decimal_to_binary
from format_binary_number import format_binary_number
from get_broadcast_address import get_broadcast_address
from get_network_address import get_network_address
from get_network_class_from_ip import get_network_class_from_ip
from hosts import get_min_host_address, get_max_host_address, get_host_count, get_ip_address_with_cidr, get_cidr_from_ip_with_cidr, get_ip_from_ip_with_cidr, is_valid_ip
from write_to_json import write_to_json


def main():
    if len(sys.argv) > 1:
        ip_with_cidr = sys.argv[1]
        if not is_valid_ip(ip_with_cidr):
            print("Wrong ip address!")
            return
    else:
        ip_with_cidr = get_ip_address_with_cidr()

    cidr = get_cidr_from_ip_with_cidr(ip_with_cidr)
    ip = get_ip_from_ip_with_cidr(ip_with_cidr)

    mask_bin = cidr_to_binary_subnet_mask(cidr)
    mask_dec = convert_binary_address_to_decimal(mask_bin)

    network_address = get_network_address(ip, mask_dec)
    network_class = get_network_class_from_ip(ip)

    broadcast_address_dec = get_broadcast_address(network_address, mask_dec)
    broadcast_address_bin = convert_decimal_address_to_binary(broadcast_address_dec)

    min_host_address_dec = get_min_host_address(network_address)
    min_host_address_bin = convert_decimal_address_to_binary(min_host_address_dec)

    max_host_address_dec = get_max_host_address(broadcast_address_dec)
    max_host_address_bin = convert_decimal_address_to_binary(max_host_address_dec)

    host_count_dec = get_host_count(min_host_address_dec, max_host_address_bin)
    host_count_bin = decimal_to_binary(host_count_dec)

    data = {
        'ip': ip,
        'network_address': network_address,
        'network_class': network_class,
        'network_mask': [mask_dec, mask_bin],
        'broadcast_address': [broadcast_address_dec, broadcast_address_bin],
        'first_host': [min_host_address_dec, min_host_address_bin],
        'last_host': [max_host_address_dec, max_host_address_bin],
        'host_count': [host_count_dec, format_binary_number(host_count_bin)]
    }

    write_to_json("data.json", data)
    print(("ip:\t\t\t\t {0}\n" +
           "network_address:\t {1}\n" +
           "network_class:\t {2}\n" +
           "network_mask:\t {3}\n\t\t\t\t {4}\n" +
           "broadcast_address: {5}\n\t\t\t\t {6}\n" +
           "first_host:\t {7}\n\t\t\t\t {8}\n" +
           "last_host:\t {9}\n\t\t\t\t {10}\n" +
           "host_count:\t {11}\n\t\t\t\t {12}")
          .format(ip, network_address, network_class, mask_dec, mask_bin,
                  broadcast_address_dec, broadcast_address_bin,
                  min_host_address_dec, min_host_address_bin, max_host_address_dec, max_host_address_bin, host_count_dec,
                  format_binary_number(host_count_bin)))


if __name__ == "__main__":
    main()
