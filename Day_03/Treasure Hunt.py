print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("Scene 1: The Crossroads\n You find yourself at a fork in the road.\n To the left, a mysterious forest beckons with the sound of rustling leaves and chirping birds.\n To the right, a rocky path leads toward the ominous echoes of falling rocks\n")
path = input("Type 'left' or 'right'\n").lower()
if path == 'left':
    print("Scene 2: The Riverbank\n After safely navigating through the forest, you arrive at a wide, rushing river.\n There's no bridge, but you notice two options: swim across the river or wait for something to appear")
    choice = input(" Type 'swim' or 'wait'\n").lower()
    if choice == 'wait':
        print('''         88                                               
         88                                               
         88                                               
 ,adPPYb,88  ,adPPYba,   ,adPPYba,  8b,dPPYba, ,adPPYba,  
a8"    `Y88 a8"     "8a a8"     "8a 88P'   "Y8 I8[    ""  
8b       88 8b       d8 8b       d8 88          `"Y8ba,   
"8a,   ,d88 "8a,   ,a8" "8a,   ,a8" 88         aa    ]8I  
 `"8bbdP"Y8  `"YbbdP"'   `"YbbdP"'  88         `"YbbdP"'  \n''')
        print("Scene 3: The Doors of Fate \n A raft carries you to a mysterious castle with three doors: Red, Blue, and Yellow.")
        door = input(" Type 'red' or 'blue' or 'yellow' \n").lower()
        if door == 'yellow':
            print("The door creaks open to reveal a dazzling room filled with gold, jewels, and the legendary Treasure of Eldorado. You win!")
        elif door == 'red':
            print('Flames erupt from within, consuming everything. Game over!')
        else:
            print('A ferocious beast leaps out and devours you. Game over!')
    elif choice == 'swim':
        print("You bravely dive into the water, but a school of trout mistakes you for dinner. Game over!")
    else:
        print('Game Over!')
else:
    print("You stumble into a deep, dark hole. Game over!")



