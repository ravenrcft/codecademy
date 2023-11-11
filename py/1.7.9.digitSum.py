def digit_sum(n):
    s = 0
    for d in str(n):
        s += int(d)
    return s