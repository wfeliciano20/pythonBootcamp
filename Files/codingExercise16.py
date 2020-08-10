import json

csv_file = open('csv_file.txt', 'r')
file_contents = csv_file.readlines()
csv_file.close()
json_list = []
lines = [line.strip() for line in file_contents]
for line in lines:
    club, country, city = line.split(',')
    data = {
        'club': club,
        'country': country,
        'city': city
    }
    json_list.append(data)
json_obj = json.dumps(json_list)
json_file = open('json_file.txt', 'w')
json_file.write(json_obj)
json_file.close()
