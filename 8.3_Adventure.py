'''
ADVENTURE PROGRAM
-----------------
1.) Use the pseudo-code on the website to help you set up the basic move through the house program
2.) Print off a physical map for players to use with your program
3.) Expand your program to make it a real adventure game

'''

room_list = []

room = "You are on the front porch", 2, None, None, None
room_list.append(room)
room = "You have entered into Bedroom 2", 4, 2, None, None
room_list.append(room)
room = "You are on the front South Hall", 5, 3, 0, 1
room_list.append(room)
room = "You are in the Dining Room", 6, None, None, 2
room_list.append(room)
room = "You are in Bedroom 1", None, 5, 1, None
room_list.append(room)
room = "You are in the North Hall", 7, 6, 2, 4
room_list.append(room)
room = "You are in the kitchen",  None, None, 3, 5
room_list.append(room)
room = "You are on the Balcony", None, None, 5, None
room_list.append(room)

current_room = 0

done = False
while not done:



