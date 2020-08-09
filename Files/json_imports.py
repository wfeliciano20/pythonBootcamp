import json

json_file = open('friends_json.txt', 'r')
file_contents = json.load(json_file)
json_file.close()

print(file_contents['friends'][0])

cars = [
    {'make': 'Ford', 'model': 'Fiesta'},
    {'make': 'Ford', 'model': 'Focus'}
]

file_ptr = open('cars_json.txt', 'w')
json.dump(cars, file_ptr)
file_ptr.close()
