grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def grades_sum(scores):
    total = 0
    for n in scores:
        total += n
    return total

print grades_sum(grades)

def grades_average(grades):
    average = (grades_sum(grades) / float(len(grades)))
    return average

print grades_average(grades)