# Print out numbers from 1 to 100 (including 100).
# But, instead of printing multiples of 3, print "Fizz"
# Instead of printing multiples of 5, print "Buzz"
# Instead of printing multiples of both 3 and 5, print "FizzBuzz".

for index in range(1, 101):
    if index % 3 == 0 and index % 5 == 0:
        print("FizzBuzz")
    elif index % 3 == 0:
        print("Fizz")
    elif index % 5 == 0:
        print("Buzz")
    else:
        print(index)
