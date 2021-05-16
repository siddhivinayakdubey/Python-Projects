import random

def play():
    user= input("R-rock, P-paper, S-scissor")
    computer= random.choice(['r','p','s'])
    if user==computer:
        return 'tie'
    if win(user,computer):
        return 'You won'
    return 'You Lost'

#r>s, p>r, s>p
def win(player, opponent):
    if(player=='r' and opponent=='s') or (player=='p' and opponent=='r') or (player=='r' and opponent=='s'):
        return True

print(play())