import random

#TODO: User selects a range
lower = int(input("choose your low number: "))
upper = int(input("choose your high number: "))
#TODO: Some random natural number will be chosen by the system within the range
ans = random.randint(lower, upper)
#TODO: the user has to guess the number as fewer trials as possible
count = 0
game_on = True #The game keeps playing until user guess it right
while game_on:

    guess = int(input("Guess number: "))
    print(ans) #testing

    if lower > upper:
        print("Sorry your lower number cannot be bigger than upper number. Try again.")
    elif guess > ans:
        count += 1
        print("Your guess is too high. Try again.")
        print(f"You've tried {count} times")
    elif guess < ans:
        count += 1
        print("Your guess is too low. Try again.")
        print(f"You've tried {count} times")
    else:
        count += 1
        print("You just guessed the number right! Congrats! 😎")
        print(f"You've tried {count} times")
        game_on = False # the game turns off








