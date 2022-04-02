#from typing_extensions import self


class atm:

    counter=1 #static variable
    #property->noun
    #behaviour->verb

    #pin
    #__balance
    #objects are mutable

    #if a function in class then it is called method otherwise function...in java everything in classs so  all in method
   # self.pin=None
    #self.__balance
    # there are two types of variable instantce variable -where the values are different

    #static varibale = value remains same
    def __init__(self): #constructor it can only be callled by __init__
        print("***************hello,welcome to JHIKIMIKI bank*************************")
        self.__balance=0
        self.cid=atm.counter #when using static variable we use class name at front
        atm.counter+=1
        
    def create_pin(self):
        user_pin = input('enter new pin: ')
        confirm_pin=input('enter again: ')
        if user_pin == confirm_pin:
            self.pin=user_pin
            print('pin set successfully')
        else:
            print('input dosent match')
    def change_pin(self):
        old_pin = input('enter old pin:')
        if self.pin==old_pin:
            self.create_pin()
        else:
            print("password dont match")

    def withdraw(self):
        user_input= input('enter pin:')
        if self.pin==user_input:
            amount=int(input("enter amt: "))
            if amount<=self.__balance:
                self.__balance = self.__balance - amount
                print('transaction succesfull')
            else:
                print("incufficent __balance")
        else:
            print("incorrect pin")


        
    def deposite(self):
        user_input= input('enter pin:')
        if self.pin==user_input:
            amount=int(input("enter amt: "))
            self.__balance = self.__balance + amount
            print('blanace->',self.__balance)
            
        else:
            print("incorrect pin")
        
    def check___balance(self):
        user_input= input('enter pin:')
        if self.pin==user_input:
            print("__balance->",self.__balance)
        else:
            print("incorrect pin")
    
