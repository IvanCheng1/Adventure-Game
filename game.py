import time
import words
import random

# ==============================================================


def print_pause(message):
    print(message)
    time.sleep(1)


def intro(hallway_adj, colour_one, colour_two):
    print_pause(f"\nYou find yourself trapped in a {hallway_adj} hallway.\n")
    print_pause(f"In front of you are two rooms; a {colour_one} room, and "
                f"a {colour_two} room.\n")

# ==============================================================


def room_one(lights, items, hallway_adj, colour_one, colour_two,
             chest_key_adj, table_adj):
    print_pause(f"You are in the {colour_one} room.\n")

    if "light_one" not in lights:
        print_pause("It's a little bit dark.\n")
        print_pause("You go and turn the light on.\n")
        lights.append("light_one")

    print_pause("There is a door straight ahead, and in the middle of the room"
                ", there is a treasure chest.\n")

    room_one_action(lights, items, hallway_adj, colour_one, colour_two,
                    chest_key_adj, table_adj)

# ==============================================================


def room_one_action(lights, items, hallway_adj, colour_one, colour_two,
                    chest_key_adj, table_adj):
    action = input("\nWould you like to:\n\n"
                   "1. Open the door\n"
                   "2. Open the treasure chest\n"
                   f"3. Go to the {colour_two} room\n\n"
                   "(Please choose 1, 2 or 3.)\n\n")
    if action == "1":
        print_pause("You walk towards the door, and try to open it.")
        if "door_key" not in items:
            print_pause("The door seems locked.")
            room_one_action(lights, items, hallway_adj, colour_one, colour_two,
                            chest_key_adj, table_adj)
        else:
            print_pause("You use your door key to unlock the door.")
            print_pause("The door opens up and takes you to the outside world"
                        "!")
            print_pause("\n\nYOU HAVE WON!\n\n")
            end()
    elif action == "2":
        print_pause("You try and open the treasure chest.")
        if "chest_key" not in items:
            print_pause("The treasure chest seems to be locked. "
                        "Maybe a key is needed...")
            room_one_action(lights, items, hallway_adj, colour_one, colour_two,
                            chest_key_adj, table_adj)
        else:
            print_pause(f"You use your {chest_key_adj} key to open the "
                        "treasure chest")
            if "door_key" not in items:
                print_pause("There is another key inside!")
                print_pause("This key looks like a door key!")
                items.append("door_key")
            else:
                print_pause("There is nothing inside.")
            room_one_action(lights, items, hallway_adj, colour_one, colour_two,
                            chest_key_adj, table_adj)
    elif action == "3":
        room_two(lights, items, hallway_adj, colour_one, colour_two,
                 chest_key_adj, table_adj)
    else:
        room_one_action(lights, items, hallway_adj, colour_one, colour_two,
                        chest_key_adj, table_adj)

# ==============================================================


def room_two(lights, items, hallway_adj, colour_one, colour_two,
             chest_key_adj, table_adj):
    print_pause(f"You are in the {colour_two} room.\n")

    if "light_two" not in lights:
        print_pause("It's a little bit dark.\n")
        print_pause("You go and turn the light on.\n")
        lights.append("light_two")

    if "chest_key" not in items:
        chest_key_vis = f", and there is a {chest_key_adj} key on top of the "
        "table"
    else:
        chest_key_vis = ""
    print_pause(f"You see a {table_adj} table in the middle of the room with a"
                f" rug{chest_key_vis}.\n")

    if "gloves" not in items:
        gloves_vis = " the floor is uneven, and"
    else:
        gloves_vis = ""
    print_pause(f"As you walk towards the {table_adj} table, you notice"
                f"{gloves_vis} there is a piece of paper on the {table_adj} "
                "table that reads 'It\'s poisonous!'\n")

    room_two_action(lights, items, hallway_adj, colour_one, colour_two,
                    chest_key_adj, table_adj)

# ==============================================================


def room_two_action(lights, items, hallway_adj, colour_one, colour_two,
                    chest_key_adj, table_adj):
    action = input("\nWould you like to:\n\n"
                   f"1. Go towards the {table_adj} table\n"
                   "2. Investigate the rug\n"
                   f"3. Go to the {colour_one} room\n\n"
                   "(Please choose 1, 2 or 3.)\n\n")
    if action == "1":
        print_pause(f"You walk towards the the {table_adj} table.")
        if "gloves" not in items and "chest_key" not in items:
            death(chest_key_adj)
            print_pause("\n\nGAME OVER\n\n")
            end()
        else:
            if "chest_key" not in items:
                print_pause(f"You grab the {chest_key_adj} key.")
                print_pause("You feel the gloves protecting you as the key "
                            "tries to burn through the gloves, but fails to.")
                items.append("chest_key")
            else:
                print_pause(f"There is nothing on the {table_adj} table.")
            room_two_action(lights, items, hallway_adj, colour_one, colour_two,
                            chest_key_adj, table_adj)
    elif action == "2":
        print_pause("You investigate the rug by lifting it up")
        if "gloves" not in items:
            print_pause("You find there is a pair of surgical gloves!")
            print_pause("You put them on.")
            items.append("gloves")
        elif "gloves" in items:
            print_pause("There is nothing underneath the rug.")
        room_two_action(lights, items, hallway_adj, colour_one, colour_two,
                        chest_key_adj, table_adj)
    elif action == "3":
        room_one(lights, items, hallway_adj, colour_one, colour_two,
                 chest_key_adj, table_adj)
    else:
        room_two_action(lights, items, hallway_adj, colour_one, colour_two,
                        chest_key_adj, table_adj)

# ==============================================================


def choose_room(lights, items, hallway_adj, colour_one, colour_two,
                chest_key_adj, table_adj):

    room = input("\nWhich room would you like to enter?\n\n"
                 f"1. {colour_one.title()} room\n"
                 f"2. {colour_two.title()} room\n\n"
                 "(Please choose 1 or 2.)\n\n")
    if room == "1":
        room_one(lights, items, hallway_adj, colour_one, colour_two,
                 chest_key_adj, table_adj)
    elif room == "2":
        room_two(lights, items, hallway_adj, colour_one, colour_two,
                 chest_key_adj, table_adj)
    else:
        print_pause("I don't know what that is.\n")
        choose_room(lights, items, hallway_adj, colour_one, colour_two,
                    chest_key_adj, table_adj)

# ==============================================================


def death(chest_key_adj):
    print_pause(f"You grab the {chest_key_adj} key, and it starts burning your hand.")
    print_pause("Maybe it really is poisonous...")
    print_pause("The burning gets worse........")
    print_pause("Moments later, you can't feel your hands.")
    print_pause("The burning gets to your whole body.")
    print_pause("You start to shiver...")
    print_pause("You start to feel........")
    print_pause("..")
    time.sleep(1.5)

# ==============================================================


def end():
    response = input("\nWould you like to play again? (y/n): ")
    if response == "y":
        print_pause("Yay! Here we go again!")
        print_pause("Restarting...")
        for line in range(10):
            print("\n\n")
            time.sleep(0.1)
        play_game()
    elif response == "n":
        print_pause("\nThanks for playing!\n")
    else:
        end()

# ==============================================================


def play_game():
    lights = []
    items = []

    colour_one = random.choice(words.colour)
    colour_two = random.choice(words.colour)
    while colour_one == colour_two:
        colour_two = random.choice(words.colour)

    chest_key_adj = random.choice(words.key_adj)
    table_adj = random.choice(words.big_adj)
    hallway_adj = random.choice(words.small_adj)

    intro(hallway_adj, colour_one, colour_two)
    choose_room(lights, items, hallway_adj, colour_one, colour_two,
                chest_key_adj, table_adj)

# ==============================================================


play_game()
