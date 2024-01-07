import random

guess_counter = 1

name = input("enter your name: ")
print("Hello " + str(name) )

words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']

original_word = list(random.choice(words))
word = list(original_word)
print(word)

turns = len(word)*2
print("Find the word in", turns, "roudns")

guessed_Letter = ""
guessed_word = []

for i in range(len(word)):
    guessed_word.append("-")

while guess_counter <= turns:
    print("Round: ", guess_counter)
    guessed_Letter = str(input("Enter a letter: "))
    while len(guessed_Letter) != 1:
        guessed_Letter = str(input("Enter only one letter again: "))
    

    if guessed_Letter in word:
        print("the letter is in the word!")
        for letter in word:
            if guessed_Letter is letter:
                guessed_word[word.index(letter)] = letter
                word[word.index(letter)] = "-"
    else:
        print("the letter is NOT in the word!")
    
    for i in guessed_word:
        print(i)

    guess_counter+=1

    if guessed_word == original_word:
        print("You won! it only took: " + str(guess_counter) + " times :)")
        break
    else:
        pass

if guessed_word != original_word:
        print("wong wong! you lost. The word is : ", end=" ") 
        for i in original_word:
            print(i, end="")


