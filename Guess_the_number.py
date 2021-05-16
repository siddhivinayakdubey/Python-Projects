import random
def guess(x):
    random_number= random.randint(1,x)
    guess=0

    while(guess != random_number):
        guess = int(input(f"Guess the no. between 1 &{x}: "))
        if (guess<random_number):
            print("Sorry try again, Too Low")
        elif (guess>random_number):
            print("Sprry Try Again, Too High")
    print(f"Hurray You guessed the right no. which is: {random_number}")

guess(10)