#Q1 Fix all the syntax and logical errors in the given source code 
#add comments to explain your reasoning

# This program gets three test scores and displays their average.  It congratulates the user if the 
# average is a high score. The high score variable holds the value that is considered a high score.

HIGH_SCORE = 95
 
# Get the test scores.
test1 = input('Enter the score for test 1: ')
test2 = input('Enter the score for test 2: ')
## test score 3 was missing based on Q1 prompt so an additional input function is included.
test3 = input('Enter the score for  test 3: ')
# Calculate the average test score.
## The scores from tests 1-3 are captured in paranthesis to follow correct order of operation. All the inputs are type string and are converted to integers.
average = (int(test1) + int(test2) + int(test3)) / 3
# Print the average.
print('The average score is ',average)
# If the average is a high score,
# congratulate the user.
## the "HIGH_SCORE variable is corrected to upper class since variables are case sensitive
if average >= HIGH_SCORE:
    print('Congratulations!')
print('That is a great average!')

#Q2
#The area of a rectangle is the rectangle’s length times its width. Write a program that asks for the length and width of two rectangles and prints to the user the area of both rectangles. 
## The split function allows the input function to accept more than one input from the user. The user is asked to input h and w of each rectangle in one line.
length1,width1 = input('Enter the length and width of rectangle 1, separated by a space: ').split()
length2,width2 = input('Enter the length and width of rectangle 2, separated by a space: ').split()

## The input string values are converted to integers then the areas are calculated for each rectangle.
area1 = int(length1) * int(width1)
area2 = int(length2) * int(width2)

## The area of each rectangle is printed.
print('The area of rectangle 1 is',area1,'and','the area of rectangle 2 is',area2)

#Q3 
#Ask a user to enter their first name and their age and assign it to the variables name and age. 
#The variable name should be a string and the variable age should be an int.  

## The input from age is converted to integer from string
name = input('What is your name? ')
age = int(input('What is your age? '))


#Using the variables name and age, print a message to the user stating something along the lines of:
# "Happy birthday, name!  You are age years old today!"
## The print statement gets rid of all spaces between variables so that I can control exactly where the spaces are. 
print('Happy birthday',' ',name,"!",' You are',' ',age,' years old today!',sep="")

