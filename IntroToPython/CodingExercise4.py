lottery_numbers = {13, 21, 22, 5, 8}


"""
A player looks like this:

{
    'name': 'PLAYER_NAME',
    'numbers': {1, 2, 3, 4, 5}
}

Define a list with two players (you can come up with their names and numbers).
"""

players = []

player1 = {'name': 'Will', 'numbers': {21, 3, 5, 14, 11}}

player2 = {'name': 'Sonia', 'numbers': {13, 11, 22, 5, 8}}

players.append(player1)
players.append(player2)

"""
For each of the two players, print out a string like this: "Player PLAYER_NAME got 3 numbers right.".
Of course, replace PLAYER_NAME by their name, and the 3 by the amount of numbers they matched with lottery_numbers.
You'll have to access each player's name and numbers, and calculate the intersection of their numbers with lottery_numbers.
Then construct a string and print it out.

Remember: the string must contain the player's name and the amount of numbers they got right!
"""

players1_right_answers = len(
    players[0]["numbers"].intersection(lottery_numbers))
players2_right_answers = len(
    players[1]["numbers"].intersection(lottery_numbers))

print(f"Player {player1['name']} got {players1_right_answers} numbers right.")
print(f"Player {player2['name']} got {players2_right_answers} numbers right.")
