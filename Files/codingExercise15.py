import json

json_list = []
csv_file = open('csv_file.txt', 'r')
csv_content = csv_file.readlines()

for line in csv_content:
    club, city, country = line.strip().split(',')
    data = {
        'club': club,
        'city': city,
        'country': country
    }
    json_list.append(data)

    json_file = open('json_file.txt', 'w')
    json.dump(json_list, json_file)
    json_file.close()
