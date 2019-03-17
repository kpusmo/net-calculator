def get_broadcast_address(network_address, mask):
    network_parts = network_address.split('.')
    mask_parts = mask.split('.')
    broadcast_address = ''
    for i in range(len(network_parts)):
        broadcast_address += str(0xff - (int(mask_parts[i]) ^ int(network_parts[i]))) + '.'  # XNOR
    return broadcast_address[:-1]
