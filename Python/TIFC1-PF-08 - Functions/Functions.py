# Exercise 1 - print a function to display a message

# def display_message():
#     print("Today in Python, I am learning another exercise called functions.")

# display_message()

#===================================================================================================

# Exercise 2 - print a function to accept a parameter

# def favourite_game(game_name, company_name):
#     print("\nMy favourite game is called " + game_name + " which was developed by " + company_name + ".")


# favourite_game('Red Dead Redemption 2', 'Rockstars Games')

#===================================================================================================

# Exercise 3 - print a function to show shirt size and message

# def make_shirt():
#     while True:
#         print("\nWelcome to Shirt Designer! In order to help us create your perfect shirt, please follow the instructions to create your one of a kind shirt!")
    
#         shirt_size = input("Let's start with the size of the shirt. Please type below of what size shirt you would like from small to extra large:")
#         if shirt_size.lower() == {'small', 'medium', 'large', 'extra large':
#             print("Size selected. Next is to choose your shirt colour.")
#         else:
#             shirt_size = input("Please input the size you would like. Sizes include small, medium, large and extra large.")

#         shirt_colour = input("Choose one of the following colours. We have; Red, Orange, Yellow, Green, Blue, Purple, Violet, Black and white.")
#         if shirt_colour:
#             print("Colour selected. Next is to choose the text you would like printed on your shirt.")
#         else:
#             shirt_size = input("This colour is not available at the moment. Colours available are Red, Orange, Yellow, Green, Blue, Purple, Violet, Black and white. ")

#         print("Thank you for choosing shirt designer. Please proceed to the counter to collect your shirt")
#         break

#         shirt_message = input("Finally, type the text you would want your shirt to display.")
#         if shirt_message:
#             input("Your message has been printed on the shirt. If you are happy with your choices, type " + shirt_message_done + "to confirm. Otherwise type again to update your new message. ")
#         elif:
#             shirt_size = input("This colour is not available at the moment. Colours available are Red, Orange, Yellow, Green, Blue, Purple, Violet, Black and white. ")

# prompt = "\nWelcome to Shirt Designer! In order to help us create your perfect shirt, please follow the instructions to create your one of a kind shirt!"
# prompt += "\nLet's start with the size of the shirt. Please type below of what size shirt you would like from small to extra large:"
# prompt1 = "\nChoose one of the following colours. We have; Red, Orange, Yellow, Green, Blue, Purple, Violet, Black and white."
# prompt2 = "\nFinally please enter the text you would like to have printed on your shirt. Just this last step and you're done!"



# while True:
#     answer = input(prompt)
#     if answer.lower() == 'small', 'medium', 'large', 'extra large':
#         print("Size selected. Next is to choose your shirt colour.")
#     else:
#         print("We do not have size at the moment, our available sizes are small, medium, large and extra large. Please type again one of the following sizes you like.")

#     answer = input(prompt1)
#     if answer.lower() == 'red', 'orange', 'yellow', 'green', 'blue', 'purple', 'violet', 'Black', 'white':
#         print("Colour selected. Next is to choose the text you would like printed on your shirt.")
#     else:
#         input("We do not have this colour at the moment. We have colours from Red, Orange, Yellow, Green, Blue, Purple, Violet, Black and white. Please type again the colour you would like from the list: ")
    
#         answer = input(prompt2)
#         print("Your choices are finalised and your shirt is made. Please collect from the counter. Thank you for choosing Shirt Designer!")
        
# make_shirt()


# shirt_colour = make_shirt.lower('red', 'orange', 'yellow', 'green', 'blue', 'purple', 'violet', 'black', 'white')

# shirt_message = make_shirt.input("Finally, Type what message you would like written on your shirt: \n")

# shirt_message_done = make_shirt.input('yes')

# shirt_message_again = 

def make_shirt(size, message):
    """Prints a summary of the shirt size and the message on it."""
    print(f"\nThe shirt will be size {size.upper()} with the message: '{message}'.")

# Call the function using positional arguments
make_shirt('medium', 'Python is fun!')

# Call the function using keyword arguments
make_shirt(size='large', message='Keep coding!')

#===================================================================================================

# Exercise 4 - print a function to show and accepts a city and country

# def describe_city(country, city='Paris'):
#     print("\nThere is a city which is known as the city of lights which is in " + city + ".")
#     print("This city is located in a country called " + country + ".")

# describe_city(country='France')

#===================================================================================================

# Exercise 5 - 5.	Write a function called make_album() that builds a dictionary describing a music album

# def make_album(song, artist):
#     make_album = {'Metallica': 'Hit the lights', 'Accept': 'Balls to the Walls', 'Guns and Roses': 'Paradise City'}
#     make_album = {'Artist': artist, 'Song': song}
#     return make_album

# heavy_metal_1 = make_album('Metallica', 'Hit the lights')
# print(heavy_metal_1)
# heavy_metal_2 = make_album('Accept', 'Balls to the Walls')
# print(heavy_metal_2)
# heavy_metal_3 = make_album('Guns and Roses', 'Paradise City')
# print(heavy_metal_3)

# print("\n")
# for x, y in heavy_metal_1.items():
#     print(y)
#     print("\n")
# for x, y in heavy_metal_2.items():
#     print(y)
#     print("\n")
# for x, y in heavy_metal_3.items():
#     print(y)

#--------------------------------------------------------------------------------

# def make_album():
#     while True:
#         print("\nEnter the album details:")
 
#         artist = input("Enter the artist (or type 'done' to exit): ")
#         if artist.lower() == 'done':
#             break
 
#         title = input("Enter the album title: ")
 
#         tracks_no = input("Enter the number of tracks (press Enter to skip): ")
#         if tracks_no:
#             tracks = int(tracks_no)
#         else:
#             tracks = "Not specified"
 
#         album = {
#             "artist": artist,
#             "title": title
#         }
#         if tracks is not None:
#             album["tracks"] = tracks
       
#         print("\nAlbum created:")
#         print(album)
#         print(f"{artist.title()} - {title.title()} ({tracks})")
#         break
 
# make_album()

# #=======================================================================================================




