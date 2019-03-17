def get_network_address(ip, mask):
    ip_parts = ip.split('.')
    mask_parts = mask.split('.')
    network_address = ''
    for i in range(len(ip_parts)):
        network_address += str(int(ip_parts[i]) & int(mask_parts[i])) + '.'
    return network_address[:-1]
