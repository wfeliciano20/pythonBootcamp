# Ask the user to choose one of two option
user_input = input(
    "Do you want to print(p) or do you want to exit without printing(q)?")
# if they type 'p', our program should print "Hello" and then ask the user again. Keep repeating this until...
while user_input != "q":
    if user_input == "p":
        print("Hello")
    user_input = input(
        "Do you want to print(p) or do you want to exit without printing(q)?")
# if they type 'q', our program should terminate.
