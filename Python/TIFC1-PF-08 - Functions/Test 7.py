def greet_sausage(dog):
    print(f"Hi {dog.title()}")

greet_sausage('Scout')
greet_sausage('Frankie')

#-----------------------------------

def describe_pet(animal_type, pet_name):
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('dachshund', 'scout')
describe_pet('scout', 'dachshund')

def describe_pet(animal_type, pet_name='dachshund'):
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet(pet_name='scout')

#----------------------------------------------------


def describe_pet(pet_name, animal_type, pet_last_name=' '):
    if pet_last_name:
        pet_info = pet_name + ', ' + pet_last_name + ', ' + animal_type
    else:
        pet_info = pet_name + ', ' + animal_type
    return pet_info

my_pet = describe_pet('Frankie', 'dachshund')
print(my_pet)

my_pet = describe_pet('Frankie', 'dachshund', 'Furter')
print(my_pet)

#-------------------------------------------------------

def describe_pet(pet_first_name, pet_last_name):
    my_pet = {'first': pet_first_name, 'last': pet_last_name}
    return my_pet

dog = describe_pet('Frankie', 'Furter')
print(dog)

for x, y in dog.items():
    print(y)
