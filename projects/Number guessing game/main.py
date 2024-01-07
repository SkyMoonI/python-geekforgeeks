import random
import math

lowest=0
highest=0
guess_count=0
guess=None
minimum_Number_of_Guessing=None

print("please enter a range: ")
lowest = int(input("Lowest number: " ))
highest = int(input("Highest number: "))

random_number = random.randint(lowest,highest)
print(random_number)
minimum_Number_of_Guessing = int(math.log2(highest - lowest + 1))
print(minimum_Number_of_Guessing)

guess = int(input("Guess a number: "))


while guess != random_number:  
    if guess > random_number:
        guess = int(input("You guessed too high! Try Again:  "))
    elif guess < random_number:
        guess = int(input("You guessed too small! Try Again:  "))
    guess_count+=1
guess_count+=1

if(guess_count <= minimum_Number_of_Guessing):
    print("That's it, You won! It only took "+str(guess_count)+" times :)")
else:
    print("You found the number but not in minimum number of guessing")