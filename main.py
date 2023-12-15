import random

# here we have a list of names
names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freedie']

print(names)

     #sintax: {new_key:new_value for new_key in names}
student_scores = {student: random.randint(1, 100) for student in names}

print(student_scores)

# syntax: passed_students = {new_key: new_value for (key, value) in dictionary.items()}
passed_students = {student: score for (student, score) in student_scores.items() if score >= 60}

print(passed_students)


# Exercise 1 (31) for List Comprehension
# Example Input "What is the Airspeed Velocity of an Unladen Swallow?"
# Example Output
# {
# 'What': 4,
# 'is': 2,
# 'the': 3,
# 'Airspeed': 8,
# 'Velocity': 8,
# 'of': 2,
# 'an': 2,
# 'Unladen': 7,
# 'Swallow?': 8
# }

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# 🚨 Don't change code above 👆 # Write your code below 👇
sentence_list = sentence.split()
# print(sentence_list)
result = {word: len(word) for word in sentence_list}
print(result)


# Exercise 2 (32) for List Comprehension
# You are going to use Dictionary Comprehension to create a dictionary called weather_f that takes each temperature in degrees Celsius and converts it into degrees Fahrenheit.
# To convert temp_c into temp_f use this formula:
# (temp_c * 9/5) + 32 = temp_f

# Example Output
{'Monday': 53.6, 'Tuesday': 57.2, 'Wednesday': 59.0, 'Thursday': 57.2, 'Friday': 69.8, 'Saturday': 71.6, 'Sunday': 75.2}

weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
# 🚨 Don't change code above 👆 # Write your code 👇 below:

weather_f = {day_of_week: (temp_c * 9/5) + 32 for (day_of_week, temp_c) in weather_c.items()}

print(weather_f)




