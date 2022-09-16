#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 18:06:41 2022

@author: catherinecho
"""

#Q1 Write a program that prompts the user for a meal: breakfast, lunch, or dinner. Then using if statements and else statements print the user a message recommending a meal. For example, if the meal was breakfast, you could say something like, “How about some bacon and eggs?”

meal = input('What meal would you like a recommendation for? Breakfast, lunch, or dinner? ')

if meal == 'breakfast':
    print('How about some bacon and eggs')
if meal == 'lunch':
    print('How about a sandwich and fruit')
if meal == 'dinner':
    print('How about steak and eggs')

#Q2 The mailroom has asked you to design a simple payroll program that calculates a student employee’s gross pay, including any overtime wages. If any employee works over 20 hours in a week, the mailroom pays them 1.5 times their regular hourly pay rate for all hours over 20. You should take in the user’s input for the number of hours worked, and their rate of pay.
worked_hours = input('How many hours did you work this week? ')
pay_rate = input('How much do you earn per hour? ')

## if you worked more than 20 hours per week, the first 20 hours are multiplied by pay_rate but any hours after 20 are multiplied by 1.5 times pay_rate
if float(worked_hours) > 20: 
    print(20 * float(pay_rate)  + (float(worked_hours)-20) * float(pay_rate) * 1.5)
#any other hours worked per week (i.e. 20 hours or less) the number of hours is multiplied by pay_rate
else:
    print(float(worked_hours) * float(pay_rate))
    
#Q3 Write a function named times_ten. The function should accept an argument and display the product of its argument multiplied times 10.
def times_ten(x):
    print(x * 10)

#Q4 Find the errors, debug the program, and then execute to show the output.
## changed input statement of Calories2 to change from first to second food.
## converted the str input values to float so Calories1 and Calories2 can be added
## edited the format method to define placeholder using {} in string statement. 
## added : at the end of each function definition
## capitalized input variables in showCalories
def main():
      Calories1 = float(input("How many calories are in the first food? "))
      Calories2 = float(input("How many calories are in the second food? "))
      showCalories(Calories1, Calories2)
      
def showCalories(Calories1,Calories2):
   print('The total calories you ate today {:.2f} '.format(Calories1 + Calories2))
      
#Q5 Write a program that uses any loop (while or for) that calculates the total of the following series of numbers: 1/30 + 2/29 + 3/28 ............. + 30/1
## created empty cell, list1, to append each iteration of loop. The sum of the items in list1 is printed. 
list1 = []
for i in range(1,31):
    list1.append(i/(31-i))

print(sum(list1))

#Q6 Write a function that computes the area of a triangle given its base and height. The formula for an area of a triangle is: AREA = 1/2 * BASE * HEIGHT
def triangle_area(base,height):
    print(0.5 * base * height)


    


    
