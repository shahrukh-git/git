import random
import time

guess = 0
tries = 0

number = random.randint(1,10)

name = input("Hey!, May I Know Your Name?: ")
print("Hello "+name+".")
question = input("Are You Ready To Guess? (yes/no): ")
time.sleep(1)

if question.lower() == 'no':
    time.sleep(1)
    print("I'm sorry, We'll meet each other next time!")
    exit()
elif question.lower() == 'yes':
    time.sleep(1)
    print("I'm thinking of anumber between 1 & 10")

while not (guess == number):
    time.sleep(1)
    guess = int(input("What's your guess? "))
    tries = tries + 1
    if guess == number:
        print("Brilliant")
        print("Congrats, You Guess was correct. The number was indeed {}.".format(number))
        time.sleep(1)
        print("It has taken you {} tries".format(tries))
        time.sleep(1)
    elif guess < number:
        print("No! Guess Higher")   
    elif guess > number:
        print("No! Guess Lower")              