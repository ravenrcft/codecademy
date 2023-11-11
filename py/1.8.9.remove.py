def remove_duplicates(alist):
    uniquelist = []
    for item in alist:
        if item  not in uniquelist:
            uniquelist.append(item)
    return uniquelist