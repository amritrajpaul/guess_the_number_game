#this is the guess the number game
import random
print('Hello. What is your name?')
name = input()
print('Well, ' + name + ', I am thinking of a number between 1 and 20 take a guess')
num = random.randint(1,20)
for i in range(1 , 7):

    print('Take a guess.')
    guess = int (input())

    if guess > num:
        print ('Your guess is too high')
    elif guess < num:
        print('Your guess is too low')
    else :
        break #this condition is for the corect guess
if guess == num:
    print('good job ' + name + ' ! You guessed my number in ' +str(i) + ' guesses !' )
else:
    print('Nope. The number I was thinking of was ' + str(num))
    
print('tap any key to Exit')
input()
 
