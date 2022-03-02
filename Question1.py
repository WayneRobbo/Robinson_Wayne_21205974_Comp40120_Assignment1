#! /usr/bin/python3
# Author: Wayne Robinson
# Number: 21205974
# Python Script Assignment1
# script: Question1.py

# Gunners list containing players second names declared
gunners = ['ljungberg', 'pires', 'vieira', 'bergkamp', 'henri',
'wright', 'adams', 'overmars', 'campbell', 'kanu', 'petit', 'cole', 'anelka']

def display_anwers():
    print("\n===================================")

#=================== Question 1 Part A =========================
# Function declaration to find the required letter.
def find_item_number(gunners):
    # Initilise counter variable.
    counter = 0
    # For loop to interate through list the lenght of gunners list.
    for i in range(len(gunners)):

        # Store name from list in a tempory variable.
        # use counter function to count the occurances of letter 'e'.
        name = gunners[i]
        counter = counter + name.count('e')

    # Print resulting count value to the user.
    display_anwers()
    print("The gunners list has", counter ,"items with an \'e'")

# Function call to find item occurances
find_item_number(gunners)

#=================== Question 1 Part B =========================
# Function declaration to print each item on a seprate line with the lenght.
def count_length_of_each_item(gunners):
    display_anwers()
    # For loop to interate through list,
    # interating through each item counting each letter.
    for i in range(len(gunners)):
        print(gunners[i], "has", len(gunners[i]), "letters")

# Function call to find item letters
count_length_of_each_item(gunners)

#=================== Question 1 Part C =========================
# Function declaration to print each item on a seprate line with the lenght.

def new_list_less_then_6(gunners):

    newgunners = []
    # For loop to interate through list,
    # interating through each item counting each letter.
    for i in range(len(gunners)):

        count = len(gunners[i])
        if(count < 6 ):
            newgunners.append(gunners[i])
        else:
            pass

    display_anwers()
    print(newgunners)

new_list_less_then_6(gunners)

#=================== Question 1 Part D =========================
# Function declaration to print each item on a seprate line with the lenght.
