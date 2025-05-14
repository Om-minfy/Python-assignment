# Easy Questions
# 1. Function Basics
def calculate_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

print("Testing calculate_average:")
print(calculate_average([5, 10, 15, 20]))
print(calculate_average([]))


# 2. Default Parameters
def greet_user(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print("\nTesting greet_user:")
print(greet_user("Alice"))
print(greet_user("Bob", "Hi"))


# Medium Questions
# 1. Variable Arguments
def calculate_total(*prices, discount=0):
    total = sum(prices)
    if discount:
        total -= total * (discount / 100)
    return total

print("\nTesting calculate_total:")
print(calculate_total(10, 20, 30))
print(calculate_total(10, 20, 30, discount=10))


# 2. Closures
def create_multiplier(factor):
    def multiplier(x):
        return x * factor
    return multiplier

print("\nTesting create_multiplier:")
double = create_multiplier(2)
triple = create_multiplier(3)
print(double(5))
print(triple(5))