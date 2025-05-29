# artist = ["Motorhead", "Metallica", "Guns & Roses", "Accept", "Bonjovi"]

# print(artist)

# print(f"You can listen to {artist[0]}")
# print(f"You can listen to {artist[1]}")
# print(f"You can listen to {artist[2]}")
# print(f"You can listen to {artist[3]}")
# print(f"You can listen to {artist[4]} \n")

# print(f"{artist[0]} - Aces of Spades")
# print(f"{artist[1]} - Hit the Lighrs")
# print(f"{artist[2]} - Paradise City")
# print(f"{artist[3]} - Balls to the Walls")
# print(f"{artist[4]} - Living on a Prayer \n")

# favourite_game = ["Red Dead Redemption 2", "Far Cry 3", "Final Fantasy VII Remake", "Resident Evil 2 Remake"]
# print("\n")
# authors = ["Capcom", "Rockstar Games", "Ubisoft", "Square Enix"]

# print("Favourite game:")
# print(favourite_game)

# print("Author of game:") 
# print(authors)

# print(f"\nI liked the game {favourite_game[0]} which was directed by {authors[1]} because of it's story \n")

# ###########################################################################################################

# The Dinner Problem

print("\nwho would I invite for dinner? \n")

family = ["Dad", "Mum", "Noshi",]

print(f"I would invite {family[0]}, {family[1]} and {family[2]} \n")

# I just found out that my sister will be unable to come.

print(f"I just found out that {family[2]} will be unable to come for dinner." )
print("Luckily I was able to save a seat for another family member.\n")

del family[2]
family.insert(2, 'Ali')

print(family, "\n")
print("Now 3 seats excluding myself are full.\n")

# Send out new invites

print(f"my invite to {family[0]} has been sent.")
print(f"my invite to {family[1]} has been sent.")
print(f"my invite to {family[2]} has been sent. \n")

# A bigger table for more people has been found

print("I went to the restaurant to arrange seatings and discovered a bigger table with even more")
print("seating availabe. Now I can invite more people for the dinner. \n")

family.append('Cuddles') 
family.insert(3, 'Gurya')
family.insert(0, 'Zain')

print(family, "\n")

print(f"New invite to {family[0]} has been sent")
print(f"New invite to {family[1]} has been sent")
print(f"New invite to {family[2]} has been sent")
print(f"New invite to {family[3]} has been sent")
print(f"New invite to {family[4]} has been sent")
print(f"New invite to {family[5]} has been sent \n")

for family_member in family:
    print(f"This is {family_member}")

print("So thats my one big happy family")

## BONUS - USING THE SORTED AND REVERSE FUNCTION ==================

print("The restaruant manager said he required a list of people")
print("to make the invites but requested them in order\n") 

print("The list of family members in order... \n")
print(sorted(family))

print("\nThe restaruant manager now said his printer is jumbling the order formation of invites and asks")
print("me to provide a new list but in reverse. Not sure how it will fix the printer problem.\n")

print("The list of family members but in reverse...\n")
family.reverse
print(family)

# ## END OF BONUS ====================================================

# Bigger table will not be ready for the dinner event. Only 2 spaces are currently available

print("\nA Bigger table will not be ready for the dinner event.")
print("They only have tables with 3 seats available.\n")

print(f"I will invite {family[1]} and {family[2]} for dinner. I will have to let")
print(f"{family[0]}, {family[3]}, {family[4]} and {family[5]} know of the shortage")
print("of seats available and will plan another day. \n")

family.pop(3)      
family.pop(4)

print(f"I've informed {family[1]} and {family[2]} they are still invited for dinner. \n")

del family[0]

del family[2]

print(f"{family[0]} and {family[1]} have their invites and are ready to come for dinner.") 
print("Excluding myself, the total people coming below is... \n") 

print(len(family))
print("\nThe others have been notified of the change of plans. ")
print("Hopefully this 'Dinner Problem' wont happen the next time! \n")
