# Async Activity April 8th, 2024

# 1. In your own words, describe what a while loop is?

#1 a. A while loop is a type of loop that repeatedly executes a block of code as long as a specified condition is true . it continues to execute the block of code until the condition becomes false 




#2. Create a function that uses a while loop to determine if a user has typed in 
# the the correct word guess. If the user types in the wrong word, your program 
# should inform them that their guess was inccorect and to try again, but if the
# user guesses the word correctly, your program shoul tell the user they have 
# guessed correctly and have won the game, stopping the loop.

def word_guess_game (): 
correct _word = "apple"
user_guess=input (guess the word : " ") 

while user_guess.lower() ! = correct word :
print ( incorrect guess. please try again ."")
user_guess = input ("guess the word: " )


print ( " comgratulations ! you have guessed correctly and won the game .")