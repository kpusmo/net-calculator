def format_binary_number(binary_number):
    if isinstance(binary_number, int):
        binary_number = str(binary_number)
    result = ''
    while len(binary_number) % 4 != 0:
        binary_number = '0' + binary_number
    binary_number_string_length = len(binary_number)
    for i in range(binary_number_string_length):
        if ((binary_number_string_length - i) % 4) == 0 and i != 0:
            result += ' '
        result += binary_number[i]
    return result
