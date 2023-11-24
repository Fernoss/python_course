print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
# step 1
input_junction = input("You come across a junction, will you go \'left\' or \'right\'?")
if input_junction == "left":
    print("safe")
    # step 2
    input_boat = input("You see a river between you and the temple. Do you \'wait\' or \'swim\'?")
    if input_boat == "wait":
        print("safe")
        # step 3
        input_door = input("You stand before a temple with three doors - \'red\', \'blue\', and \'yellow\'.\n"
                           "Which door do you choose?")
        if input_door == "yellow":
            trap = input("You find the treasure! Do you want to open it? Y or N?")
            if trap == "Y" or trap == "y":
                print("Greedy! Treasure was full of traps, you die. Game Over!")
            else:
                print("Congratulations! You avoided the trap and lived on!")
        elif input_door == "red":
            print("The room was a trap, you were burned alive! Game over.")
        else:
            print("The room was a trap, you were eaten by cock-a-mouse! Game Over.")
    else:
        print("You valiantly swam the river, only to find it was full of crocodiles. Game Over!")
else:
    print("You fell through a hole, you died. Game Over!")

