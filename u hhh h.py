'''
ADVENTURE PROGRAM
-----------------
1.) Use the pseudo-code on the website to help you set up the basic move through the house program
2.) Print off a physical map for players to use with your program
3.) Expand your program to make it a real adventure game
'''

room_list = []

room = ["Current Location: You are in the office", 8, None, None, None]
room_list.append(room)
room = ["Current Location: You have entered into the Language Arts Classroom. \n You realise this might be a great opportunity to grab a pencil", 3, 8, None, None]
room_list.append(room)
room = ["Current Location: You are in the Lunch Room. To your right, theres a long table with assorted produce. ", 4, None, None, 8]
room_list.append(room)
room = ["Current Location:You are in the Geometry Classroom. Everything is pretty normal, but theres a filing cabinet to the right that sticks out to you.", 5, 9, 1, None]
room_list.append(room)
room = ["Current Location: You are in Gymnasium", 6, None, 2, 9]
room_list.append(room)
room = ["Current Location: You are in the Biology Classroom", None, 10, 3, None]
room_list.append(room)
room = ["Current Location: You are in the Physics Classroom. \n To your left theres a door with a sign in bold letters: 'HVACC'.", None, None, 4, 10]
room_list.append(room)
room = ["Current Location: You are in the Janitors Closet. You notice a row of cabinets along the walls.", None, None, 10, None]
room_list.append(room)
room = ["Current Location: You are in a long dark hallway(specifically hallway 8). The lights slightly flicker above you, making it so you can see a couple feet ahead of you.", 9, 2, 0, 1]
room_list.append(room)
room = ["Current Location: You are in a long dark hallway(specifically hallway 9). The lights slightly flicker above you, making it so you can see a couple feet ahead of you.", 10, 4, 8, 3]
room_list.append(room)
room = ["Current Location: You are in a long dark hallway(specifically hallway 10). The lights slightly flicker above you, making it so you can see a couple feet ahead of you.", 7, 6, 9, 5]
room_list.append(room)


current_room = 0
inventory = []
backpack = False
notebook = False
pencil = False
lunch = False
machine = False
print("""\

                                       ._ o o
                                       \_`-)|_
                                    ,""       \ 
                                  ,"  ## |   ಠ ಠ. 
                                ," ##   ,-\__    `.
                              ,"       /     `--._;)
                            ,"     ## /
                          ,"   ##    /


                    """)



print("\n \nGOAL: Get to the bus. \n But before you leave, you need to collect these items: \n --> School Backpack \n --> Notebook \n --> Pencil \n --> A Packed Lunch \n --> A time machine")




done = False
while not done:
    print("")
    print(room_list[current_room][0])
#####LANG AND LIT ROOM ######
    if current_room == 1:
        look = input("Would you like to look around for a pencil?")
        if look.lower() == "yes" or look.lower() == "y":
            if pencil == False:
                pencil = input("You move over to the desk and find a pencil. Its a red pencil, would you like to add it to your inventory?")
                if pencil.lower() == "yes" or pencil.lower() == "y":
                    print("You grab the red pencil and add it to your inventory.")
                    inventory.append("red pencil")
                    pencil = True
                elif pencil.lower() == "no" or pencil.lower() == "n":
                    print("you make a bold move and dont put it in your inventory")
            else:
                print("You remember you already got the pencil and decide to move on.")
        elif look.lower() == "no" or look.lower() == "n":
            print("You get rid of the idea to look around. Moving to another room is a better option.")
        else:
            print("Sorry, that is not an option. Try Again.")

          ####PHYSICS CLASSROOM####
    if current_room == 6:
        look1 = input("Would you like to look inside the 'HVACC' room?")
        if look1.lower() == "y" or "yes":
            if machine == False:
                print("As you cautiously walk inside, you notice a time machine! \n You grab the time machine and add it to your inventory.")
                inventory.append("time machine")
                machine = True
            else:
                print("You remember you already got the pencil and decide to move on.")
        elif look1.lower() == "no" or look1.lower() == "n":
            print("You get rid of the idea to look around. Moving to another room is a better option.")
        else:
            print("Sorry, that is not an option. Try Again.")



###LUNCH ROOM ###
    if current_room == 2:
        if lunch == False:
            look2 = input("Do you want to make yourself a sandwich for your lunch?")
            if look2.lower() == "yes" or look2.lower() == "y":
                sand = input("Would you like turkey, beef, or pork on it?")
                if sand.lower() == "beef" or sand.lower() == "b":
                    print("You make the beef sandwich and put it in your inventory \n")
                    inventory.append("beef sandwich(lunchbox)")
                    lunch = True
                elif sand.lower() == "turkey" or sand.lower() == "t":
                    print("You make the turkey sandwich and put it in your inventory \n")
                    inventory.append("turkey sandwich(lunchbox)")
                    lunch = True
                elif sand.lower() == "pork" or sand.lower() == "p":
                    print("You make the pork sandwich and put it in your inventory \n")
                    inventory.append("pork sandwich(lunchbox)")
                    lunch = True
                else:
                    print("sorry thats not an option.")
            elif look2.lower() == "no" or look2.lower() == "n":
                print("You get rid of the idea to make a sandwich. Moving to another room is a better option.")
        else:
            print("Everything is untouched.")

#### JANITORS CLOSET ###

    if current_room == 7:
        look8 = input("Would you like to look around inside the cabinets?")
        if look8.lower() == "yes" or look8.lower() == "y":
            if backpack == False:
                backpack = input("You find 5 backpacks stuffed inside. Would you like a backpack?")
                if pencil.lower() == "yes" or "y":
                    print("You grab a black backpack and add it to your inventory. \n \n")
                    inventory.append("Backpack")
                    backpack = True
                else:
                    print("You dont get a backpack and move on.")
            else:
                print("You remember you already got the pencil and decide to move on.")
        elif look8.lower() == "no" or look8.lower() == "n":
            print("You get rid of the idea to look around. Moving to another room is a better option.")
        else:
            print("Sorry, that is not an option. Try Again.")

###GEOMETRY ###
    if current_room == 3:
        look44 = input("Would you like to inspect the filing cabinet?")
        if look44.lower() == "y" or look44.lower() == "yes":
            if notebook == False:
                print("With glee, you find that theres a stack of notebooks and add one to your inventory")
                inventory.append("notebook")
                notebook = True
            else:
                print("You move away from the filing cabinet due to you already finding the notebooks in there.")
        elif look44.lower() == "n" or look44.lower() == "no":
            print("you turn around and figure out where to go next.")
        else:
            print("sorry thats not an option.")

            # if len(inventory) == 5:
            #     print("You have collected all the materials! Game is complete!")



    direction = input("\n \n \n where would you like to go? \n N for North \n E for East \n W for West \n S for South \n Q for Quit Game \n or I for inventory")


    if direction.lower() == "n" or direction.lower() == "north":
        next_room = room_list[current_room][1]
        if next_room == None:
            print("You can't go that way")
        else:
            current_room = next_room




    elif direction.lower() == "e" or direction.lower() == "east":
        next_room = room_list[current_room][2]
        if next_room == None:
            print("You can't go that way")
        else:
            current_room = next_room


    elif direction.lower() == "s" or direction.lower() == "south":
        next_room = room_list[current_room][3]
        if next_room == None:
            print("You can't go that way")
        else:
            current_room = next_room




    elif direction.lower() == "w" or direction.lower() == "west":
        next_room = room_list[current_room][4]
        if next_room == None:
            print("You can't go that way")
        else:
            current_room = next_room


    elif direction.lower() == "q" or direction.lower() == "quit":
        print("Thanks for playing!")
        done = True
    elif direction.lower() == "i" or direction.lower() == "inventory":
        print(inventory)
    else:
        print()
        print("Invalid.")
        print()
        continue
    if len(inventory) == 5:
        print("You have collected all the materials! Game is complete!")

###LANG AND LIT ROOM ###
