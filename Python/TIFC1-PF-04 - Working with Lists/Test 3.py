# This syntax creates lists

foods = ["tuna", "salmon", "mackerel", "trout"]

print("Okay Weasley, you can eat any of the following for dinner:")

# This syntax creates loops

for food in foods:
    print(f"You can have {food} for dinner. ")
    print("or....")
   
print("Nothing!")

# End of loop syntax

# Test

print("These are my dogs...")

dogs = ["Larry", "Harry", "Henry", "Bill", "Author"]

for doggy in dogs:
    print("This dog is " + doggy + ".")

questions = ["1 * 2", "2 * 2", "3 * 2", "4 * 2", "5 * 2"]
answers = [2, 4, 6, 8, 10]

for question in questions:
    print("What is the answer for " + question + "?")   
print("\n")
for answer in answers:
    print(f"The answer is... {answer}.")

# Ranges - range(start, stop, step)

for value in range(2,21,2):
    print(value)

for value in range(4,20,4):
    print(value)

# Ranges - END

# List ()

numbers = list(range(1,15))
print(numbers)

my_list = list('This is a test')

print(my_list)

numbers = list(range(0,11))
print(numbers)

digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(min(digits))
print(max(digits))
print(sum(digits))

# Slicing a list

cats = ["tabby", "tuxedo", "calico", "bengal"]

# semi colon alters this code. if SC is placed before the digit, the first string appears only.
# If the SC is placed after the digit, the other strings appear except the first string
# Using different numbers alters the print statement but rules will play the same.
print(cats[:1])

foods = ["tuna", "salmon", "mackerel", "trout"]

print("Alright Weasley and Noche, this is what we can have for dinner: ")
for food in foods[0:4]:
    print(food.title())

plants = ['hawthoria', 'palm', 'pothos', 'barrel cactus', 'prayer plant']
print("Here are my favorite plants out of my list:")
for plant in plants[0:4]:
    print(plant.title())

# List with looping slices with append commands.

weasley_foods = ["tuna", "salmon", "mackerel", "trout"]
noche_foods = weasley_foods[:]

weasley_foods.append('chicken')
noche_foods.append('cheese')

print("The foods Weasley likes to eat is: ")
print(weasley_foods)

print("The foods Noche likes to eat is: ")
print(noche_foods)

# Tuples - Like a list but its immovable. starts with parentheses instead of square brackets

foods = ("tuna", "trout", "salmon", "mackerel")
print(foods)
print(foods[3])

plants = ('cacti', 'pothos', 'eucalyptus')
for plant in plants:
    print(plant)

plants = ('palm', 'tree', 'lily pad')
for plant in plants:
    print(plant)
   
print(plants)