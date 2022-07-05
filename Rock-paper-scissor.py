import random

def play():
        ai = random.choice(['r','p','s'])
        user = input("Rock(r), Paper(p), or Scissor(s) : ")
        if user == ai:
            print("Tie!!")

        if win(user, ai):
            return "You won!!"

        return("You lost, i chose %s"%ai)



def win(user, ai):
        if (user == 'r' and ai =='s') or (user == 'p' and ai =='r') or (user == 's' and ai =='p'):
            return True


print(play())



