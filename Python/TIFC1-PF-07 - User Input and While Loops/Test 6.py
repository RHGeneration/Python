# age = input("How old are you? ")

# if int(age) <= 18:
#     print("You are too young to play!")
# else:
#     print("You are allowed to play, you are old.")

# # print("\n")

# # prompt = "Hello Weasley and Noche! What would you like to eat today?"
# # prompt += "\nThis is what we have: tuna, chicken, salmon, and clams. Type 'done' when you are finished! \n"

# # while True:
# #     answer = input(prompt)
# #     if answer.lower() == 'tuna':
# #         print("That sounds great! I will make tuna for you now.")
# #     elif answer.lower() == 'chicken':
# #         print("I am surprised you chose chicken!")
# #     elif answer.lower() == 'salmon':
# #         print("Salmon is so special, yum!")
# #     elif answer.lower() == 'clams':
# #         print("Wow! Fancy clams!")
# #     elif answer.lower() == 'done':
# #         break
# #     else:
# #         print("Sorry! We do not have that.")


# current_number = 1

# while current_number <= 5:
#     print(current_number)
#     current_number += 1


# #     prompt = "\nTell me something, and I will repeat it back to you:"
# # prompt += "\nEnter 'quit' to end the program. "
# # message = ""

# # while message != 'quit':
# #     message = input(prompt)
# #     print(message)

# #     #This is an example of using continue in a for loop
# # for letter in 'Noche':     
# #    if letter == 'h':
# #       continue
# #    print('Current Letter :', letter)

prompt = "What rental car would you like? "
prompt += "\nWe have a great selection available: subaru, toyota, honda, and ford. Type 'quit' if our selection does not suit you."
 
while True:
    answer = input(prompt)
    if answer == 'subaru':
        print("Let me see if I can find you a Subaru.")
    elif answer == 'toyota':
        print("Sorry, our last Toyota was rented out.")
    elif answer == 'honda':
        print("Sure, we have a Honda available.")
    elif answer == 'ford':
        print("We have grey, black and a red Ford available.")
    elif answer == 'quit':
        break
    else:
        print("Sorry, we do not have that car available.")