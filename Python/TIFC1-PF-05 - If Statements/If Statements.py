# # Exercise 1

# fruit = 'orange'
# sweet = 'orange'
# print("Is the fruit an == 'orange'? I predict True.")
# print(fruit == 'orange')
# print("\nIs an orange == 'squared'? I predict False.")
# print(fruit == 'round')
# print("Is an orange == 'sweet'? I think it's true.")
# print(sweet == 'orange')

# print("\n")

# Exercise 2

# age = int(input("How old is this person? "))

# if age <= 2:
#     print("He is a baby.\n")
# elif 2 <= age < 4:
#     print("He is a toddler.\n")
# elif 4 <= age < 13:
#     print("He is a kid.\n")
# elif 13 <= age < 20:
#     print("He is a teenager.\n")
# elif 21 <= age < 64:
#     print("He is an adult.\n")
# else:
#     print("He is a senior.\n")

# Exercise 3

# print("\n")

# favourite_fruits = ["bananas", "oranges", "blackcurrants", "strawberries"]

# answer = input(f"What is your favourite fruit? ")

# if answer.lower() == 'bananas':
#     print(f"Ah so you like {favourite_fruits[0]}?! Interesting...")
# elif answer.lower() == 'oranges':
#     print(f"Ah so you like {favourite_fruits[1]}?! Interesting...")
# elif answer.lower() == 'blackcurrants':
#     print(f"Ah so you like {favourite_fruits[2]}?! Interesting...")
# elif answer.lower() == 'strawberries':
#     print(f"Ah so you like {favourite_fruits[3]}?! Interesting...")
# else:
#     print("Its not on your favourite list.")

# Exercise 4

# username = ["admin", "shrek", "fiona", "donkey", "puss"]
# login_attempt = input("Welcome back. Please login to access your desktop \n")

# if login_attempt in username:
#         if login_attempt == 'admin':
#             print(f"welcome {login_attempt.title()}. Would you like to see a status report?")
#         else: 
#             print(f"Welcome back {login_attempt.title()} to your far far away desktop.")
# else:
#      print("This user is currently not registered on the system.")


# Exercise 5

# current_users = ["admin", "shrek", "fiona", "donkey", "puss"]
# new_users = ["dragon", "wolf", "pinocchio", "farquod", "charming"]

# login_attempt = input("Welcome to the Far Far away experience. We are preparing to setting up your first desktop experience. \nEnter your name to create your account. Names are case insensitive. \n")
# create_new_user = input("Welcome to the Far Far away experience. We are preparing to setting up your first desktop experience. \nEnter your name to create your account. Names are case insensitive. \n")

# if login_attempt in current_users:
#         if login_attempt == 'admin':
#             print(f"There can only be one {login_attempt.title()}. Please contact your administrator \nif you wish to have another {login_attempt.title()} account created.")
#         else: 
#             print(f"The name {login_attempt.title()} has already been taken.")
# else:
#      print("This name is available to use.")

#==============================================================================================================================================================================================

# Stretch and exercise

numbers = list(range(1, 11))

for num in numbers:
    if num == 1:
        print(f"{num}st")
    elif num == 2:
        print(f"{num}nd")
    elif num == 3:
        print(f"{num}rd")
    else:
        print(f"{num}th")



# # print("\n")

# # flower = "Sunflowers"

# # answer = input(f"Do {flower} produce seeds? Type yes or no: ")

# # if answer.lower() == 'yes':
# #     print(f"That's right! {flower} do indeed produce seeds.")
# # else:
# #     print(f"No is not the correct answer. {flower} do infact produce seeds.\n")


