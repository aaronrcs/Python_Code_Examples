mayra = {
    "name": "Mayra",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
aaron = {
    "name": "Aaron",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
pablo = {
    "name": "Pablo",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}


# fucntion that takes an average
def average(numbers):
    total = sum(numbers)
    total = float(total)
    result = total / len(numbers)
    return result

# fucntion that gets the average of all the students score for homework, quizzes, and tests
def get_average(student):
    homework = average(student["homework"])
    quizzes = average(student["quizzes"])
    tests = average(student["tests"])
    return 0.1 * homework + 0.3 * quizzes + 0.6 * tests

# fucntion that will determine the letter grade
def get_letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


print("This is the average letter grade of Pablo (student): ")
print (get_letter_grade(get_average(pablo)))
print()


def get_class_average(students):
    results = []

    for student in students:
        results.append(get_average(student))

    return average(results)


students = [mayra, aaron, pablo]

print("Total class average: ")
print (get_class_average(students))
print()

print("Letter grade of the class average: ")
print (get_letter_grade(get_class_average(students)))
