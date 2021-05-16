import random
def computer_guess(x):
    low=1
    high =x
    feedback=''
    while feedback!='c':
        guess = random.randint(low, high)
        print(f"Computer guesses: {guess}")
        feedback=input("h, c or l").lower()
        if feedback=='h':
            high =guess
        elif feedback=='l':
            low =  guess

    print(f"Hurray Computer guessed it right which is: {guess}")
computer_guess(10)