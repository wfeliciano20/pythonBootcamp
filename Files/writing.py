
user_name = input("Enter your name: ")

my_file_writing = open('data.txt', 'w')
my_file_writing.write(user_name)
my_file_writing.close()
