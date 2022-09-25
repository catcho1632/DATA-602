# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Q1 Create a class called BankAccount that has four attributes: bankname, firstname, lastname, and balance.

class BankAccount:
    def __init__(self, bankname, firstname, lastname, balance = 0): # attributes are initialized and balance is set to 0
        self.bankname = bankname
        self.firstname = firstname
        self.lastname = lastname
        self.balance = balance
    def deposit(self, amount): # method deposit will accept user input amount to add to the balance attribute
        self.balance = self.balance + amount
        return print('Your current balance is ', self.balance) 
    def withdrawal(self, amount): # method withdrawal accepts user input of amount to withdraw
        if self.balance >= amount: # checks that there is enough in the balance for withdrawal
            self.balance = self.balance - amount # if enough in balance, balance is reduced by amount
            print('Your current balance is ', self.balance)
        else:
            print('Withdrawal request exceeds the available balance.') # message is returned if not enough is in balance for withdrawal
    def __str__(self): # this dunder method allows user to access attribute values as strings, user can enter print() to access object details
        return 'Bank Name: {self.bankname} \nOwner Name: {self.firstname} {self.lastname} \nCurrent Balance: ${self.balance}'.format(self = self)

# test 1 
account1 = BankAccount('chase','cat','cho',2000) 
account1.deposit(200) # deposit 200
print(account1) # balance should be 2200
account1.withdrawal(500) # withdraw 500
print(account1) # balance should be 1700

# test 2
account2 = BankAccount('wells fargo','Tim','Smith',10000) 
account2.deposit(1000) # deposit 1000
print(account2) # balance should be 11000
account2.withdrawal(2000) # withdraw 2000
print(account2) # balance should be 9000

# Q2: Create a class Box that has attributes length and width that takes values for length and width upon construction (instantiation via the constructor).
import math

class Box:
    def __init__(self, length, width): #initialized with attributes length and width of a box/rectangle
        self.length = length
        self.width = width
    def render(self):
        for l in range(1,self.length+1): #for every row the following indented code is performed
            for w in range(1,self.width+1): #for every row, the for loop will cycle through the number of columns to print an '*' until the end of width. 
                print('*', end = " ")
            print('\n') # a new row begins for the next row of asterisks
    def invert(self):
        length_orig = self.length #original attributes are stored in new variable to make a proper swap of values
        width_orig = self.width
        self.width = length_orig 
        self.length = width_orig
        return 'The new width is {self.width} and the new length is {self.length}'.format(self = self)
    def get_area(self):
        return 'The area of this box is {}'.format(self.width * self.length)
    def get_perimeter(self):
        return 'The perimeter of this box is {}'.format(self.width * 2 + self.length * 2)
    def double(self):
        self.length = 2 *  self.length
        return 'Doubling the size of the box results in an area of {}'.format(self.length * self.width) # the length is doubled to double the area of the box 
    def __eq__(self, other):
        if isinstance(other, Box): #checks that the objects being compared are of the class Box
            if other.width == self.width and other.length == self.length: # checks that width and length are equal between two boxes
                return True
        return False
    def print_dim(self):
        return 'The width of the box is {self.width} and the length of the box is {self.length}'.format(self = self)
    def combine(self, other):
        self.length = self.length + other.length
        self.width = self.width + other.width
        return 'The new width is {self.width} and new length is {self.length}'.format(self = self)
    def get_hypot(self):
        d = math.sqrt(float(self.length**2) + float(self.width**2))
        return 'the diagonal length of the box is {:.2f}'.format(d)

# Instantiate 3 boxes of dimensions 5,10 , 3,4 and 5,10 and assign to variables box1, box2 and box3 respectively    
box1 = Box(5,10)
box2 = Box(3,4)
box3 = Box(5,10)

# Print dimension info for each using print_dim()
box1.print_dim()
box2.print_dim()
box3.print_dim()

# Evaluate if box1 == box2, and also evaluate if box1 == box3, print True or False to the screen accordingly
box1 == box2
box1 == box3

# Combine box3 into box1 
box1.combine(box3)

# Double the size of box2
box2.double()

# Combine box2 into box1
box1.combine(box2)




                    
            
        
        
 
       
       

            
            
            
        
        
    
            
    
    
       
        
  
    
        
    
    
   
            
            
           
            
                
            
        
        
    

    
    

        
            
            
        


        
        

          


        