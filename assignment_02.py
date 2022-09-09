#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 18:17:43 2022

@author: catherinecho
"""

#Q1 What will the following code display?
numbers = [1, 2, 3, 4, 5] 
print(numbers[0:5])

#Q2 Design a program that asks the user to enter a store’s sales for each day of the week. The amounts should be stored in a list. Use a loop to calculate the total sales for the week and display the result.
week = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']

input_list= []
for x in week:
    sale = input('input sales for ' + x + " ")
    input_list.append(int(sale))

print('the total sale for the week is', sum(input_list))

# Q3 Create a list with at least 5 places you’d like to travel to. Make sure the list isn’t in alphabetical order

## Print your list in its original order
places = ['memphis', 'new zealand', 'iceland', 'italy', 'switzerland']
print(places)

## Use the sort() function to arrange your list in order and reprint your list.
places.sort()
print(places)

## Use the sort(reverse=True) and reprint your list.
places.sort(reverse = True)
print(places)

# Q4 Write a program that creates a dictionary containing course numbers and the room numbers of the rooms where the courses meet. The program should also create a dictionary containing course numbers and the names of the instructors that teach each course. After that, the program should let the user enter a course number, then it should display the course’s room number, instructor, and meeting time.
## room, instructor, and time are nested together within each course number
courses = {'DATA602': {"room #": 200, 'instructor': 'Jennifer', 'time': '3:00 pm'}, 'DATA606': {'room #': 354, 'instructor': 'Sam', 'time': "1:30 pm"}, 'DATA607': {'room #': 321, 'instructor': 'Kyle', 'time': '10:00 am'}}
print(courses['DATA602'])
print(courses['DATA606'])
print(courses['DATA607'])

# Q5 Write a program that keeps names and email addresses in a dictionary as key-value pairs. The program should then demonstrate the four options:

contact = {'Smith': 'smith@gmail.com', 'Sharon': 'sharon2@gmail.com', 'Kyle': 'kylew@gmail.com'}

## look up a person’s email address
print(contact['Kyle'])

## add a new name and email address
contact['Fin'] = 'fin@catmail.com'
print(contact)

## change an existing email address, and
contact['Kyle'] = 'Kyle927@school.com'
print(contact)

##  delete an existing name and email address.
del contact['Smith']
print(contact)




