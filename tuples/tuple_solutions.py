# Import namedtuple
from collections import namedtuple

# Easy Questions
# 1. Swap adjacent elements in a tuple
def swap_pairs(t):
    new_list = []
    i = 0
    while i < len(t):
        if i + 1 < len(t):
            new_list.append(t[i + 1])
            new_list.append(t[i])
            i += 2
        else:
            new_list.append(t[i])
            i += 1
    return tuple(new_list)

print("Testing swap_pairs:")
print(swap_pairs((1, 2, 3, 4)))
print(swap_pairs((1, 2, 3)))


# 2. Get stats from a list of numbers
def get_stats(numbers):
    if len(numbers) == 0:
        return (None, None, 0, 0)
    minimum = min(numbers)
    maximum = max(numbers)
    total = sum(numbers)
    average = total / len(numbers)
    return (minimum, maximum, total, average)

print("\nTesting get_stats:")
print(get_stats([1, 2, 3, 4, 5]))


# Medium Questions
# 1. Named Tuple: Student and Top Student
Student = namedtuple("Student", ["name", "age", "grades"])

def top_student(students):
    top = None
    highest_avg = 0
    for student in students:
        avg = sum(student.grades) / len(student.grades)
        if avg > highest_avg:
            highest_avg = avg
            top = student
    return top

print("\nTesting top_student:")
alice = Student("Alice", 20, (85, 90, 95))
bob = Student("Bob", 19, (70, 80, 90))
charlie = Student("Charlie", 21, (90, 92, 93))
print(top_student([alice, bob, charlie]))


# 2. Count coordinate occurrences
def count_coordinate_occurrences(coords):
    count_dict = {}
    for point in coords:
        if point in count_dict:
            count_dict[point] += 1
        else:
            count_dict[point] = 1
    return count_dict

print("\nTesting count_coordinate_occurrences:")
coords = [(1, 2), (3, 4), (1, 2), (5, 6), (3, 4), (1, 2)]
print(count_coordinate_occurrences(coords))