import random

player1_guess_count=0
player2_guess_count=0

def number_chooser():
    player_number = input("Player, set the number: ")
    if player_number.isdigit():
        pass
    else:
        print("The input is not a digit.")
        while not player_number.isdigit():
            player_number = input("Player, set a DIGIT: ")
    return player_number

def player_number_guesser():
    player_guess = input("Player , guess the number: ")
    if player_guess.isdigit():
        pass
    else:
        print("The input is not a digit.")
        while not player_guess.isdigit():
            player_guess = input("Player , set a DIGIT: ")
    return player_guess


def game():
    player1_number = 0

    player2_guess = 0

    player2_guess_count = 0

    player1_number = number_chooser()

    while player1_number != player2_guess:
        player2_guess = player_number_guesser()

        player1_number = list(player1_number)
        player2_guess = list(player2_guess)

        player2_guess_count+=1

        guess_digit_list = ['X','X','X','X']
        guess_digit_count = 0
        counter_x=0
        for x in player2_guess:
            counter_y=0
            for y in player1_number:
                if (x is y) and (counter_x == counter_y):
                    guess_digit_list [player2_guess.index(x)]= x
                    guess_digit_count+=1
                counter_y+=1
            counter_x+=1


        if player2_guess == player1_number and guess_digit_count == 1:
            print("Great! You guessed the number in just 1 try! You're a Mastermind!")
            break
        elif player2_guess == player1_number:
            print("player  won!")
            for x in guess_digit_list:
                print(x,end=" ")
            print()
            print("player guess count : ",player2_guess_count)
            break
        else:
            print("Not quite the number. You get", guess_digit_count ,"digit(s) correct!")
            print("Also these numbers in your input were correct.")
            for x in guess_digit_list:
                print(x,end=" ")
            print()
    return player2_guess_count


if __name__ == '__main__':
    player2 = game()
    player1 = game()
    print("player1 guessed in: ",player1,"times")
    print("player2 guessed in: ",player2,"times")

    if player1 == player2:
        print("You guessed the number at the same amount of count")
    elif player1 > player2:
        print("player2 won")
    else:
        print("player1 won")