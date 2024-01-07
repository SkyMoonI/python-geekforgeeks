import logic

if __name__ == '__main__':
    game_matrix = logic.start_game()

while(True):
 
    # taking the user input
    # for next step
    x = input("Press the command : ")
 
    # we have to move up
    if(x == 'W' or x == 'w'):
 
        # call the move_up function
        game_matrix, flag = logic.move_up(game_matrix)
 
        # get the current state and print it
        status = logic.get_current_state(game_matrix)
        print(status)
 
        # if game not over then continue
        # and add a new two
        if(status == 'GAME NOT OVER' and flag == True):
            game_matrix = logic.add_new_2(game_matrix)


        # else break the loop 
        elif status == 'LOST':
            break
 
    # the above process will be followed
    # in case of each type of move
    # below
 
    # to move down
    elif(x == 'S' or x == 's'):
        game_matrix, flag = logic.move_down(game_matrix)
        status = logic.get_current_state(game_matrix)
        print(status)
        if(status == 'GAME NOT OVER' and flag == True):
            game_matrix = logic.add_new_2(game_matrix)

        elif status == 'LOST':
            break
 
    # to move left
    elif(x == 'A' or x == 'a'):
        game_matrix, flag = logic.move_left(game_matrix)
        status = logic.get_current_state(game_matrix)
        print(status)
        if(status == 'GAME NOT OVER' and flag == True):
            game_matrix = logic.add_new_2(game_matrix)

        elif status == 'LOST':
            break
 
    # to move right
    elif(x == 'D' or x == 'd'):
        game_matrix, flag = logic.move_right(game_matrix)
        status = logic.get_current_state(game_matrix)
        print(status)
        if(status == 'GAME NOT OVER' and flag == True):
            game_matrix = logic.add_new_2(game_matrix)
        elif status == 'LOST':
            break
    else:
        print("Invalid Key Pressed")
 
    # print the game_matrixrix after each
    # move.
    for i in range(4):
        print(game_matrix[i])