def cube(number):
    '''returns cube value of a number'''
    return number**3

def by_three(number):
    if number % 3 == 0:
        return cube(number)
    else:
        return False