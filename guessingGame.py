import random
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
random.choice()
number=(random.coice(list1))
print("guess the number")
guess = input("enter string: ")
while chances < 5
if guess == number:
    print("Caongradulations YOU WON!!")
    elif guess < number:
         print("Your guess was too low... try a number higher than ",guess)
    elif guess > number:
        print("your guess was too high... try a number lower than ",guess)
        break
if not chances < 5:
    print("YOU LOOSE the number was: ",number)