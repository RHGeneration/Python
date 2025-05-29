weasley = { 
    'fur': 'white and ginger',
    'eyes': 'yellow',
    'toes': 'pink'
    }
noche = {}

#Add to an existing dictionary
weasley['age'] = 1

#Copy an existing dictionary and modify the new one
bigglesworth = dict(weasley)
bigglesworth['fur'] = 'none'
bigglesworth['age'] = 666

#Populate an empty dictionary
noche['fur'] = 'black'
noche['eyes'] = 'green'
noche['toes'] = 'black'
noche['age'] = 2

print("Weasley's attributes are:")
print(weasley)
print("Noche's attributes are:")
print(noche)
print("Bigglesworth's attributes are:")
print(bigglesworth)

#Creating a dictionary

Rafi = {
    'First Name': 'Rafi',
    'Last Name': 'Haq',
    'City': 'Birmingham'
    }

#Copying a dictionary

Garry = dict(Rafi)
Garry['Last Name'] = 'Mason'
Garry['City'] = 'Manchester'
Garry['County'] = 'Greater Manchester'

#Modifying / adding extra to an existing dictionary

Rafi['County'] = 'West Midlands'

#Adding Key-Value Pairs

Harry = {}
#       /\
#       ||
#Adding data to an empty dictionary
 #      ||
#       \/
Harry['First Name'] = 'Harry'
Harry['Last Name'] = 'Mason'
Harry['City'] = 'Luton'
Harry['County'] = 'Bedfordshire'

# deleting data

del Garry['City']

print("This is Rafi's details")
print(Rafi)

print("This is Garry's details")
print(Garry)

print("This is Harry's details")
print(Harry)


