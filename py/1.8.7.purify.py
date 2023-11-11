def purify(number_list):
    listt =[]
    for n in number_list:
        if int(n)%2 == 0:
            listt.append(n)
    return listt