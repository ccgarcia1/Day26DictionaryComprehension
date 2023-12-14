import random
# here we have a list of names
names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freedie']

print(names)

                 #{new_key:new_value for new_key in names}
student_scores = {student:random.randint(1,100) for student in names}

print(student_scores)