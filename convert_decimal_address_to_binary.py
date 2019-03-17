from decimal_to_binary import decimal_to_binary


def convert_decimal_address_to_binary(decimal_address):
    decimal_address_chunks = decimal_address.split('.')
    binary_address = ''
    for address in decimal_address_chunks:
        binary_address += str(decimal_to_binary(address)) + '.'
    return binary_address[:-1]
