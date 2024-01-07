import random

def start_game():
    game_matrix = []
    
    """
    [[0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]]
    the cells on the game / grid
    """
    for i in range(4):
        game_matrix.append([0]*4)   
    
    # print the matris
    #for i in range(4):
    #    print(game_matrix[i])

    # printing controls for user
    print("Commands are as follows : ")
    print("‘W’ or ‘w’ : Move Up")
    print("‘S’ or ‘s’ : Move Down")
    print("‘A’ or ‘a’ : Move Left")
    print("‘D’ or ‘d’ : Move Right")

    # a new 2 in grid after every step
    game_matrix = add_new_2(game_matrix)
    game_matrix = add_new_2(game_matrix)

    # print the matris
    for i in range(4):
        print(game_matrix[i])

    return game_matrix

def add_new_2(game_matrix):
    is_there_0 = False

    for i in range(4):
        for j in range(4):
            if game_matrix[i][j] == 0:
                is_there_0 = True
                break
        if is_there_0 == True:
            break

    # initilize random row and column
    
    if is_there_0 == True:
        row = random.randint(0,3)
        column = random.randint(0,3)
        # print(row, column)  
    
        while (game_matrix[row][column] != 0):
            row = random.randint(0,3)
            column = random.randint(0,3)
    
        # assings 2 to a random row and column
        game_matrix[row][column] = 2
    return game_matrix

def get_current_state(game_matrix):

    # if any cell contains
    # 2048 we have won
    for i in range(4):
        for j in range(4):
            if game_matrix[i][j] == 2048:
                return "WON"

    # if we are still left with
    # atleast one empty cell
    # game is not yet over
    for i in range(4):
        for j in range(4):
            if game_matrix[i][j] == 0:
                return "GAME NOT OVER"
    
    # or if no cell is empty now
    # but if after any move left, right,
    # up or down, if any two cells
    # gets merged and create an empty
    # cell then also game is not yet over
    for i in range(3):
        for j in range(3):
            if (game_matrix[i][j] == game_matrix[i+1][j] or game_matrix[i][j] == game_matrix[i][j+1]):
                return "GAME NOT OVER"
    
    for i in range(3):
            if (game_matrix[3][j]== game_matrix[3][j + 1]):
                return "GAME NOT OVER"
    
    for i in range(3):
            if (game_matrix[i][3]== game_matrix[i + 1][3]):
                return "GAME NOT OVER"
    
    # else we have lost the game
    return 'LOST'


# all the functions defined below
# are for left swap initially.
 
# function to compress the grid
# after every step before and
# after merging cells.
def compress(game_matrix):

    # bool variable to determine
    # any change happened or not
    changed = False

    # empty grid 
    new_matrix = []

    # with all cells empty
    for i in range(4):
        new_matrix.append([0]*4)   

    for i in range(4):
        possision = 0

        # here we will shift entries
        # of each cell to it's extreme
        # left row by row
        # loop to traverse rows
        for j in range(4):

            # loop to traverse each column
            # in respective row
            if game_matrix[i][j] != 0:
                new_matrix[i][possision] = game_matrix[i][j]

                # if cell is non empty then
                # we will shift it's number to
                # previous empty cell in that row
                # denoted by pos variable
                if possision != j:
                    changed = True
                
                possision += 1

    # returning new compressed matrix
    # and the flag variable.
    return new_matrix, changed

# function to merge the cells
# in matrix after compressing
def merge(game_matrix):

    changed = False
     
    for i in range(4):
        for j in range(3):

            # if current cell has same value as
            # next cell in the row and they
            # are non empty then
            if(game_matrix[i][j] == game_matrix[i][j + 1] and game_matrix[i][j] != 0):
 
                # double current cell value and
                # empty the next cell
                game_matrix[i][j] = game_matrix[i][j] * 2
                game_matrix[i][j + 1] = 0
 
                # make bool variable True indicating
                # the new grid after merging is
                # different.
                changed = True
 
    return game_matrix, changed

# function to reverse the matrix
# means reversing the content of
# each row (reversing the sequence)
def reverse(game_matrix):
    new_mat =[]
    for i in range(4):
        new_mat.append([])
        for j in range(4):
            new_mat[i].append(game_matrix[i][3 - j])
    return new_mat

# function to get the transpose
# of matrix means interchanging
# rows and column
def transpose(game_matrix):
    new_mat = []
    for i in range(4):
        new_mat.append([])
        for j in range(4):
            new_mat[i].append(game_matrix[j][i])
    return new_mat

# function to update the matrix
# if we move / swipe left
def move_left(grid):
 
    # first compress the grid
    new_grid, changed1 = compress(grid)
 
    # then merge the cells.
    new_grid, changed2 = merge(new_grid)
     
    changed = changed1 or changed2
 
    # again compress after merging.
    new_grid, temp = compress(new_grid)
 
    # return new matrix and bool changed
    # telling whether the grid is same
    # or different
    return new_grid, changed
 
# function to update the matrix
# if we move / swipe right
def move_right(grid):
 
    # to move right we just reverse
    # the matrix 
    new_grid = reverse(grid)
 
    # then move left
    new_grid, changed = move_left(new_grid)
 
    # then again reverse matrix will
    # give us desired result
    new_grid = reverse(new_grid)
    return new_grid, changed
 
# function to update the matrix
# if we move / swipe up
def move_up(grid):
 
    # to move up we just take
    # transpose of matrix
    new_grid = transpose(grid)
 
    # then move left (calling all
    # included functions) then
    new_grid, changed = move_left(new_grid)
 
    # again take transpose will give
    # desired results
    new_grid = transpose(new_grid)
    return new_grid, changed
 
# function to update the matrix
# if we move / swipe down
def move_down(grid):
 
    # to move down we take transpose
    new_grid = transpose(grid)
 
    # move right and then again
    new_grid, changed = move_right(new_grid)
 
    # take transpose will give desired
    # results.
    new_grid = transpose(new_grid)
    return new_grid, changed
 
# this file only contains all the logic
# functions to be called in main function
# present in the other file