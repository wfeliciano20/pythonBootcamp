def avg(seq): return sum(seq)/len(seq)


def total(seq): return sum(seq)


def top(seq): return max(seq)


operations = {
    "average": avg,
    "total": total,
    "top": top
}

students = [
    {"name": "Rolf", "grades": (67, 90, 95, 100)},
    {"name": "Bob", "grades": (56, 78, 80, 90)},
    {"name": "Jen", "grades": (98, 90, 95, 99)},
    {"name": "Anne", "grades": (100, 100, 95, 100)},
]

for student in students:
    name = student["name"]
    grades = student["grades"]

    print(f"Student: {name}")
    operation = input("Enter 'average','total','top': ")

    operation_function = operations[operation]
    print(operation_function(grades))
