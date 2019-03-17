def cidr_to_binary_subnet_mask(cidr):
    mask = []
    dotted_mask = ""
    cidr = int(cidr)
    for i in range(cidr):
        mask.append(1)
    for i in range(cidr, 32):
        mask.append(0)
    j = 0
    for i in mask:
        j += 1
        if j > 8:
            dotted_mask = dotted_mask + "."
            j = 1
        dotted_mask = dotted_mask + str(i)
    return dotted_mask
