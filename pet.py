# The Threshold for Hunger and Boredom is set as 10

import random

user_pets = []
user_pets_name = []


class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = random.randint(1, 10)
        self.boredom = random.randint(1, 10)
        self.sounds = []
        self.boredom_decrement = 4
        self.hunger_decrement = 4

    def __str__(self):
        if self.boredom > 10 and self.hunger > 10:
            return "{} is Bored and Hungry".format(self.name.capitalize())
        elif self.boredom > 10:
            return "{} is Bored".format(self.name.capitalize())
        elif self.hunger > 10:
            return "{} is Hungry".format(self.name.capitalize())
        else:
            return "{} is Happy".format(self.name.capitalize())

    def clock_tick(self):
        self.hunger += 1
        self.boredom += 1

    def reduce_boredom(self):
        if self.boredom == 0:
            pass
        elif self.boredom == 1:
            self.boredom = self.boredom - 1
        elif self.boredom == 2:
            self.boredom = self.boredom - 2
        elif self.boredom == 3:
            self.boredom = self.boredom - 3
        else:
            self.boredom = self.boredom - self.boredom_decrement

    def reduce_hunger(self):
        if self.hunger == 0:
            pass
        elif self.hunger == 1:
            self.hunger = self.hunger - 1
        elif self.hunger == 2:
            self.hunger = self.hunger - 2
        elif self.hunger == 3:
            self.hunger = self.hunger - 3
        else:
            self.hunger = self.hunger - self.hunger_decrement

    def teach(self, word):
        self.sounds.append(word)
        print("Learned new word {}".format(word))
        self.reduce_boredom()

    def hi(self):
        if len(self.sounds) == 0:
            print("{} does not know any words!!!".format(self.name.capitalize()))
        else:
            print("{} says {}".format(self.name.capitalize(), self.sounds[random.randint(0, len(self.sounds) - 1)]))
            self.reduce_boredom()

    def feed(self):
        print("Feeding {}".format(self.name))
        self.reduce_hunger()


def update_clock():
    for item in user_pets:
        item.clock_tick()


def adopt_pet():
    print("**********************")
    name = input("Enter name for the new pet : ")
    new_pet = Pet(name)
    user_pets.append(new_pet)
    user_pets_name.append(name)
    print("New pet adopted\n**********************")


def show_pets():
    if len(user_pets) == 0:
        print("**********************\nYou do not have any pets yet!!!\n**********************")
    else:
        print("**********************\nMy Pets\n**********************")
        for item in user_pets:
            print(item)


def pet_interact(pet):
    while True:
        print("Current status : {}".format(pet))
        print("**********************\nPet Menu\n**********************")
        print(
            "1.Greet {p}\n2.Feed {p}\n3.Teach {p}\n4.Show the words that {p} knows\n5.Back to Main Menu\n**********************".format(
                p=pet.name.capitalize()))
        try:
            user_pet_choice = int(input("Enter your choice : "))
            if user_pet_choice == 1:
                pet.hi()
                update_clock()
            elif user_pet_choice == 2:
                pet.feed()
                update_clock()
            elif user_pet_choice == 3:
                word_to_be_taught = input("Enter the word to teach {} : ".format(pet.name.capitalize()))
                pet.teach(word_to_be_taught)
                update_clock()
            elif user_pet_choice == 4:
                if len(pet.sounds) == 0:
                    print("{} does not know any words!!!".format(pet.name.capitalize()))
                else:
                    print("Words {} Knows\n**********************".format(pet.name.capitalize()))
                    for i in pet.sounds:
                        print(i)
            elif user_pet_choice == 5:
                break
            else:
                print("Invalid Option!!!")
        except:
            print("Invalid Value!!!")


def main_menu():
    print("**********************\nMain Menu\n**********************")
    print("1.Adopt a Pet\n2.Show all of my Pets\n3.Connect with a Pet\n4.Exit\n**********************")
    try:
        user_choice = int(input("Enter your choice : "))
        if user_choice == 1:
            adopt_pet()
            update_clock()
        elif user_choice == 2:
            show_pets()
            update_clock()
        elif user_choice == 3:
            pet_name = input("Enter the pet you wish to interact with : ")
            if pet_name not in user_pets_name:
                print("You do not have a pet named {}".format(pet_name))
                update_clock()
            else:
                for i in user_pets:
                    if i.name == pet_name:
                        pet_interact(i)
        elif user_choice == 4:
            return False
        else:
            print("Invalid Option!!!")
    except:
        print("Invalid Value!!!")


print("Welcome")
while True:
    wish = main_menu()
    if wish is False:
        break
