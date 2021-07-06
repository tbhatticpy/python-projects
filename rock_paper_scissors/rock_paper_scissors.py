import random

def play():
    user = input("Enter 'r' for rock, 'p' for paper or 's' for scissors: \n")
    comp = random.choice(['r', 'p', 's'])
    print(f"Computer selected {comp}")
    if user == comp:
        return 'It\'s a tie!'
    elif is_win(user, comp):
        return 'You win!'
    return 'You lose!'

def is_win(player, opponent):
    #r>s, s>p, p>r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True

print(play())