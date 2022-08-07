import random
number = random.randint(1,9)
chances = 0

 print ("Guess a number (between 1 and 9)"):

# While loop to count the number of chances 
while chances < 5:
    guess = input("enter the number ")

    if guess  == number :
  # if number entered by the user is same as the generated 
  # number by radiant function then break from loop using loop 
  # control statement "break"
      print("Congratulations YOU WON!!!")
      break
    elif guess < number 
        print("your guess is too low,guess higher number",guess)
    else :
        print("your number  is too high,guess lower number",guess)
    chances = chances+1

if not chances <5:
        print("yoiu lost the number is ",number)