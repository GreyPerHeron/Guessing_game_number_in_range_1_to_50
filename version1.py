import random
confirmation = "y"


print("\nHello My friend!\nWe are going to play a guessing game.\nI am thinking of number between 1-50\n")
number=random.randint(1,50)
print(number)
guess1=int(input("What number am I thinking of?: "))

# FIRST GUESS:

if guess1 is number:
    print("\nThat was impressive! First shot!")
    exit()
else:
    print("\nNope. That is not the number I am thinking of. Your chances were pretty small though.")
    hint=input("Do You need a hint (y/n)?: ")
    if hint is confirmation:
        if number%3 ==0:
            hint1="The number can be divided by 3."
            print("\nThe number can be divided by 3.")
            guess2=int(input("\nWhat number am I thinking of?: "))
        else:
            hint1="The number can NOT be divided by 3."
            print("\nThe number can NOT be divided by 3.")
            guess2=int(input("What number am I thinking of?: "))
    else:
        hint1="You didn't want this clue. Too bad."
        print("\nOk. Brave.")
        guess2=int(input("What number am I thinking of?: "))

# SECOND GUESS:

if guess2 is number:
    print("\nThat was impressive! You did it so fast!")
    exit()
else:
    print("\nYou failed this time.")
    print("I will give You a hint: ")
    if number>25:
        hint2="The number is higher than 25."
        print("The number is higher than 25.")
        guess3=int(input("\nWhat number am I thinking of?: "))
    else:
        hint2="The number is NOT higher than 25."
        print("The number is NOT higher than 25.")
        guess3=int(input("\nWhat number am I thinking of?: "))

# THIRD GUESS:

if guess3 is number:
    print("\nThat was impressive! You did it so fast!")
    exit()
else:
    print("\nYou failed this time. That was Your 3rd guess.")
    print("I will give You another hint: ")
    if number%5==0 and number%2==0:
        hint3="The number can be divided by 2 and by 5."
        print("The number can be divided by 2 and by 5.")
        
    elif number%5!=0 and number%2==0:
        hint3="The number can be divided by 2 but can NOT be divided by 5."
        print("The number can be divided by 2 but can NOT be divided by 5.")
        
    else:
        hint3="The number can NOT be divided by 2 or 5."
        print("\nThe number can NOT be divided by 2 or 5.")
        

# Reminding guesses and clues:

print("\nSo Your first three guesses were: ",guess1,", ",guess2,", ",guess3)
print("\nThe hints:")
print(hint1)
print(hint2)
print(hint3)
print("\nThere will be no more clues. Keep trying. You can do this.")
guess4=int(input("\nWhat number am I thinking of?: "))

# 4th guess and so on...

while guess4 is not number:
    print("\nNot so great, try on more time.")
guess4=int(input("\nWhat number am I thinking of?: "))
print("\nGood job! You are a winner!")
#print("You guessed in the ",count," time.")
exit()