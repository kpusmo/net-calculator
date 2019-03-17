def get_network_class_from_ip(ip):
    ip_parts = ip.split(".")
    if int(ip_parts[0]) < 127:
        return "A"
    elif int(ip_parts[0]) < 192:
        return "B"
    elif int(ip_parts[0]) < 224:
        return "C"
    elif int(ip_parts[0]) < 240:
        return "D"
    elif int(ip_parts[0]) <= 255:
        return "E"
