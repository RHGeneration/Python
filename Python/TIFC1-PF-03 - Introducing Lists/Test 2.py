# A list of foods. Lists starts with Square brackets. []

foods = ['tuna', 'beef', 'rabbit', 'chicken', 'salmon']
print(foods)

print(input(f"Would you like to have {foods [2]}? "))
foods[4] = "lamb"
print(f"I want {foods [4]}.")

# In order of numbers, the first always starts with a zero and not a one.
# When you dont add a zero, the print function will ignore the zero but notice
# it does not count the 5 as there is no 5th or 6th index made as Python indicates)

# print(f"You can eat {foods[0]} for dinner")
# print(f"You can eat {foods[1]} for dinner")
# print(f"You can eat {foods[2]} for dinner")
# print(f"You can eat {foods[3]} for dinner")
# print(f"You can eat {foods[4]} for dinner")

# # You can modify the above list by adding your own variables by changing the value and number
# # in the list.

# foods[0] = 'lamb'
# print(foods)

# # Appending a syntax with an input gives the user to type something in the command box

# # foods.append(input("Add another food item "))
# # print(foods)

# # # Adding insert adds another variable in your syntax

# # foods.insert(1, 'trout')
# # print(foods)

# # This will delete one of the syntaxes on your print list

# # foods = ['tuna', 'beef', 'rabbit', 'chicken', 'salmon']
# # print(foods)

# # using del command will delete the numbered variable used

# del foods[1]
# print(foods)

# # using the pop command will remove the last item or from a 
# # position if you know the index of the number. You can use
# # the pop command also shows which item was removed from the list

# popped_food = foods.pop(2)
# print(foods)
# print(popped_food)

# print(f"I regret to inform that we ran out of {popped_food}.")

# removed_food = "lamb"
# foods.remove(removed_food)

# print(removed_food)

# print(f"Looks like we do not have {removed_food} either. Sorry...")

# print(foods)
# foods.sort
# print(sorted(foods))
# foods.reverse()
# print(foods)
# print(len(foods))
