import random;
chances = 0
randint1 = random.randint(100,200)
randint2 = random.randint(200,300)
rand = random.randint(randint1,randint2)
print(rand)
print("Number guessing game by Coder 119")
print("Guess a number between", randint1, "and", randint2 )
while chances < 5:
    guess = int(input("Tell me the number that I am thinking of. "))
        # if(isinstance(guess, int))
    if(guess == rand):
        print("Nice job. The number was, in fact, ", rand)
        playagain = input("Would you like to play again?")
        if(playagain=="yes"):
            print("Awesome!")
# Now what?
        break   
    elif(guess<rand):
      print("Your number was too low! Guess a number higher than ", guess )
    else:
     print("Your number was too high. Guess a a number lower than ", guess)

    chances+=1

if not chances<5:
    print("Well...um. You lost. The number was " , rand)