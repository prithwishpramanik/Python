#pattern printing
#guessing game

import random
num=random.randint(1,100)
print(num)

user=int(input("enter your number: "))
counter=1
while num!=user:
  counter=counter+1
  if user==num:
    print("number is right")
  elif user!=num:
    print("wrong")
    user=int(input("enter your number: "))
    if user==num:
        print("good job")

  else :
    print("next time")
print(counter)
    