import random
names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freedie']

print(names)

student_scores = {student:random.randint(1,100) for student in names}

print(student_scores)