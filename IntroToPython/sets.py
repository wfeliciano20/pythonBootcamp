# sets don't have duplicates you can add or remove items
# is easy to compare with other sets
art_friends = {"Rolf", "Anne", "Jen"}
science_friends = {"Jen", "Charlie"}

art_but_not_science = art_friends.difference(science_friends)
print(art_but_not_science)
not_in_both = art_friends.symmetric_difference(science_friends)
print(not_in_both)
