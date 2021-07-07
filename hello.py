# variables
Age = 21
Message = "Hello world, I am " + str(Age) + " years old."

# list
Colors = ['Black', 'White', 'Yellow']

# printing
print(Message)

# looping
for Color in Colors:
    print(Color)

for Num in range(1, 11):
    print(Num)

# tuple, immutable list
Even_Numbers = (2, 4, 6, 8, 10)
print(Even_Numbers[1:3])

# Dictionary
Person = {}
Person["name"] = "Jacky Depp"
Person["age"] = 45
Person["gender"] = "Male"

del Person["age"]

# Iterate dictionary
for key, values in Person.items():
    print(str(key).capitalize() + ": " + str(values).capitalize())

# Taking inputs
Hungryinput = input("Are you hungry?")

if str(Hungryinput).capitalize() == "No":
    print("You can go to sleep")
else:
    print("Hope you get good food!")

# while loop
I = 0
while True:
    if I > 2:
        break
    I += 1
    print("I am not sad")


# function
def Sing_A_Song(Song_Name):
    print("Singing " + str(Song_Name) + "...")


Sing_A_Song(Song_Name="Mune no kemuri")

