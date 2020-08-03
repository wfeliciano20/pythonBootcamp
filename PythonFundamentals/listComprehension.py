numbers[0, 1, 2, 3, 4]

doubled_numbers = []

for number in numbers:
    doubled_numbers.append(number * 2)


# is the same as doing this
doubled_numbers2 = [number * 2 for number in range(5)]
print(doubled_numbers2)

friend_ages = [22, 31, 35, 37]
age_strings = [f'My friend is {age} years old' for age in friend_ages]
print(age_strings)
