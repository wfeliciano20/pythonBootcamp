friend_ages = {"Rolf": 24, "Adam": 30, "Anne": 27}
print(friend_ages["Rolf"])

friend_ages["Bob"] = 20
print(friend_ages)

friends = [("Rolf", 24), ("Adam", 30), ("Anne", 27)]

friends_ages2 = dict(friends)

print(friends_ages2)
