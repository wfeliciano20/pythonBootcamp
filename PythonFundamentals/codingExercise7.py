import random

# This line creates a set with 6 random numbers
lottery_numbers = set(random.sample(range(22), 6))

# Here are your players; find out who has the most numbers matching lottery_numbers!
players = [
    {'name': 'Rolf', 'numbers': {1, 3, 5, 7, 9, 11}},
    {'name': 'Charlie', 'numbers': {2, 7, 9, 22, 10, 5}},
    {'name': 'Anna', 'numbers': {13, 14, 15, 16, 17, 18}},
    {'name': 'Jen', 'numbers': {19, 20, 12, 7, 3, 5}}
]

winner = players[0]
winner_matched_numbers = players[0]["numbers"].intersection(lottery_numbers)
for player in players:
    matched_numbers = player["numbers"].intersection(lottery_numbers)
    if matched_numbers > winner_matched_numbers:
        winner = player
winnings = 100 ** len(winner["numbers"].intersection(lottery_numbers))
print(f'{winner["name"]} won {winnings}')
# Then, print out a line such as "Jen won 1000.".
# The winnings are calculated with the formula:
# 100 ** len(numbers_matched)
