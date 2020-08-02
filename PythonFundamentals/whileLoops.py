is_learning = True

while is_learning:
    print("You're learning!")
    is_learning = False


user_input = input("Do you wish to run the program? (yes/no): ")

while user_input == "yes":
    print("We're running!")
    user_input = input("Do you wish to run the program? (yes/no): ")
print("We stopped running.")
