# Easy Questions
# 1. Filter Even Numbers
def filter_even_numbers(numbers):
    even_numbers = []
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers

print("Testing filter_even_numbers:")
print(filter_even_numbers([1, 2, 3, 4, 5, 6]))
print(filter_even_numbers([1, 3, 5]))


# 2. Merge Sorted Lists
def merge_sorted_lists(list1, list2):
    combined = list1 + list2
    combined.sort()
    return combined

print("\nTesting merge_sorted_lists:")
print(merge_sorted_lists([1, 3, 5], [2, 4, 6]))
print(merge_sorted_lists([1, 2, 3], [4, 5, 6]))


# Medium Questions
# 1. Generate Matrix
def generate_matrix(n, m):
    matrix = []
    for i in range(n):
        row = []
        for j in range(m):
            row.append(i * j)
        matrix.append(row)
    return matrix

print("\nTesting generate_matrix:")
print(generate_matrix(3, 3))


# 2. Transpose Matrix
def transpose_matrix(matrix):
    result = []
    for j in range(len(matrix[0])):
        row = []
        for i in range(len(matrix)):
            row.append(matrix[i][j])
        result.append(row)
    return result

print("\nTesting transpose_matrix:")
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print(transpose_matrix(matrix))