import random

def guess(x):
    random_num = random.randint(1, x)
    guess = 0
    while guess != random_num:
        guess = int(input(" Guess the number between 1 and %s : " %x))
        if random_num < guess:
            print("Sorry, guess again, too high !!")
        elif random_num > guess:
            print("Sorry, guess again, too low ")

    print("You got the number, number is %s" %random_num)


def ai(x):
    guess = int(input("give me a challenge !! : "))
    a=1
    user = " "
    while user != "correct":
        num = random.randint(a, x)
        print("Was it %s" % num)
        user = input("> low(l)/high(h)/correct(c)? ")
        if num < guess:
            if user == "l":
                a=num+1
        if num > guess:
            if user == "h":
                x=num-1
        else:
            if user == "c":
                if num == guess:
                    print("Yay!, i found the number")
                    break
                if num!=guess:
                    print("Hmm..that was fast!!, but something tells me i'm wrong!! ")





sel = input(" How would you like to play (p/a) : ")
x1=int(input("Enter the max limit : "))

if sel == "p":
    guess(x1)
elif sel == "a":
    ai(x1)