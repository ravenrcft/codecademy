def check_bit4(x):
    mask = 0b1000
    if x & mask > 0:
        return "on"
    else:
        return "off"