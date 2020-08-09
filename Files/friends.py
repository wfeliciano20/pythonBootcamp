friends = []
for i in range(3):
    friend = input("Enter the name of your friend ")
    friends.append(friend)

people = open('people.txt', 'r')
people_nearby = [line.strip() for line in people.readlines()]
people.close()

friends_set = set(friends)
people_nearby_set = set(people_nearby)

friends_nearby_set = friends_set.intersection(people_nearby_set)

nearby_friend_file = open('nearby_friends.txt', 'w')

for friend in friends_nearby_set:
    print(f'{friend} is nearby! Meet up with them.')
    nearby_friend_file.write(f'{friend}\n')
nearby_friend_file.close()
