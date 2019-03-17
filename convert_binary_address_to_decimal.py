from binary_to_decimal import binary_to_decimal


def convert_binary_address_to_decimal(binary_address):
    binary_address_chunks = binary_address.split('.')
    decimal_address = ''
    for address in binary_address_chunks:
        decimal_address += str(binary_to_decimal(address)) + '.'
    return decimal_address[:-1]
