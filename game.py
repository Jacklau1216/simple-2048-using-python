import random

list1 = [0,0,0,0]  #set up the game grid
list2 = [0,0,0,0]
list3 = [0,0,0,0]
list4 = [0,0,0,0]

game = True #set up the game state

def checklose():  #helper function to check lose
    game = True
    for i in range(4):
        if list1[i] == 0 or list2[i] == 0 or list3[i] == 0 or list4[i] == 0:
            break
        if i == 3:
            game = False
            print("You lose")
    return game

def checkwin():  #helper function to check win
    win = False
    for i in range(4):
        if list1[i] >= 64 or list2[i] >= 64 or list3[i] >= 64 or list4[i] >= 64:  #the winning condition is now 64
            win = True
            break
    return win

def print_screen():  # helper function to print the screen
    print(list1)
    print(list2)
    print(list3)
    print(list4)

def checkstatus(list_num):  #make sure the list have space to insert
    temp_list = []
    if list_num == 1:
        temp_list = list1
    elif list_num == 2:
        temp_list = list2
    elif list_num == 3:
        temp_list = list3
    else:
        temp_list = list4
    for i in range(4):
        if temp_list[i] == 0:
            return False
    return True

def place_random():  #helper function to add random '2' to screen
    rand = random.randint(1,4)
    rand2 = random.randrange(4)
    while checkstatus(rand):
        rand = random.randint(1,4)
    if rand == 1:
        while list1[rand2] != 0:
            rand2 = random.randrange(4)
        list1[rand2] = 2
    elif rand == 2:
        while list2[rand2] != 0:
            rand2 = random.randrange(4)
        list2[rand2] = 2
    elif rand == 3:
        while list3[rand2] != 0:
            rand2 = random.randrange(4)
        list3[rand2] = 2
    else:
        while list4[rand2] != 0:
            rand2 = random.randrange(4)
        list4[rand2] = 2

def check_up_down(listA, listB, i):  #helper function to check the up and dow
    if listA[i] == 0:
        listA[i] = listB[i]
        listB[i] = 0
    elif listA[i] == listB[i]:
        listA[i] += listB[i]
        listB[i] = 0

def up():  #helper function to move up
    for i in range(4):
        check_up_down(list1, list2, i)
        check_up_down(list2, list3, i)
        check_up_down(list1, list2, i)
        check_up_down(list3, list4, i)
        check_up_down(list2, list3, i)
        check_up_down(list1, list2, i)

def down_S():  #helper function to move down
    for i in range(4):
        check_up_down(list4, list3, i)
        check_up_down(list3, list2, i)
        check_up_down(list4, list3, i)
        check_up_down(list2, list1, i)
        check_up_down(list3, list2, i)
        check_up_down(list4, list3, i)

def check_left_right(list, num1, num2):  #helper function to check left and right
    if list[num1] == 0:
        list[num1] = list[num2]
        list[num2] = 0
    elif list[num1] == list[num2]:
        list[num1] += list[num2]
        list[num2] = 0
    
def check_left_right2(list, direction):  #helper function to check left and right
    if direction == 'left':
        check_left_right(list, 0, 1)
        check_left_right(list, 1, 2)
        check_left_right(list, 0, 1)
        check_left_right(list, 2, 3)
        check_left_right(list, 1, 2)
        check_left_right(list, 0, 1)
    else:
        check_left_right(list, 3, 2)
        check_left_right(list, 2, 1)
        check_left_right(list, 3, 2)
        check_left_right(list, 1, 0)
        check_left_right(list, 2, 1)
        check_left_right(list, 3, 2)

def left():  #helper function to move left
    check_left_right2(list1, 'left')
    check_left_right2(list2, 'left')
    check_left_right2(list3, 'left')
    check_left_right2(list4, 'left')

def right():  #helper function to move right
    check_left_right2(list1, 'right')
    check_left_right2(list2, 'right')
    check_left_right2(list3, 'right')
    check_left_right2(list4, 'right')

while checklose():  #main function
    place_random()
    print('The screen: ')
    print_screen()
    user_input = input("Please input your operation (w/a/s/d): ").upper()
    if user_input == 'W':
        up()
    elif user_input == 'A':
        left()
    elif user_input == 'S':
        down_S()
    elif user_input == 'D':
        right()
    else:
        print("Please input a suitable letter")
        continue
    if checkwin():
        print_screen()
        print("You win")
        break
    
    
    

