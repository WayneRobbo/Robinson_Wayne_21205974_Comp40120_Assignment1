#! /usr/bin/python3
# Author: Wayne Robinson
# Number: 21205974
# Python Script Assignment1
# script: Question1.py

# Gunners list containing players second names declared
gunners = ['ljungberg', 'pires', 'vieira', 'bergkamp', 'henri',
'wright', 'adams', 'overmars', 'campbell', 'kanu', 'petit', 'cole', 'anelka']

def display_anwers():
    print("\n===================================================")

#=================== Question 1 Part A =========================
# Function declaration to find the required letter.
def find_item_number(gunners):
    # Initilise counter variable.
    counter = 0
    # For loop to interate through list the lenght of gunners list.
    for item in range(len(gunners)):

        # use counter function to count the occurances of letter 'e'.
        counter = counter + gunners[item].count('e')

    # Print resulting count value to the user.
    print("The gunners list has", counter ,"items with an \'e'")

#=================== Question 1 Part B =========================
# Function declaration to print each item on a seprate line with the lenght.
def count_length_of_each_item(gunners):
    display_anwers()
    # For loop to interate through list,
    # interating through each item counting each letter.
    for item in range(len(gunners)):
        print(gunners[item], "has", len(gunners[item]), "letters")

#=================== Question 1 Part C =========================
# Function declaration to print each item on a seprate line with the lenght.

def new_list_less_then_6(gunners):

    newgunners = []
    # For loop to interate through list,
    # interating through each item counting each letter.
    for item in range(len(gunners)):

        count = len(gunners[item])
        if(count < 6 ):
            newgunners.append(gunners[item])
        else:
            pass

    display_anwers()
    print(newgunners)

#=================== Question 1 Part D =========================
# Function declaration to filter names >= 8, and remove the last letter.

def length_greater_than_equal(gunners):
    display_anwers()
    i = 0
    while i < len(gunners):
        count = len(gunners[i])
        name = gunners[i]
        i = i + 1

        if(count >= 8 ):
            print(name[0:count-1])
        else:
            pass

#=================== Question 1 Part E =========================
# Function declaration to find the longest and shortest names in list.

def longest_Shortest_Words(gunners):
    display_anwers()
    longest_Names = len(gunners[0])
    longest_Word = []

    shortest_Names = len(gunners[0])
    shortest_Word = []

    for item in gunners:

        if len(item) > longest_Names:
            longest_Names = len(item)
            longest_Names = [item]

        elif len(item) == longest_Names:
            longest_Word.append(item)

        if len(item) < shortest_Names:
            shortest_Names = len(item)
            shortest_Word = [item]

        elif len(item) == shortest_Names:
            shortest_Word.append(item)

    print("The longest words are: ", longest_Word)
    print("The shortest words are: ", shortest_Word)
    display_anwers()
#=================== Question 1 Complete =========================
display_anwers()

# Function call to find item occurances (Question 1 part A)
find_item_number(gunners)

# Function call to find item letters (Question 1 part B)
count_length_of_each_item(gunners)

# Function call to find items with less then 6 letters (Question 1 part C)
new_list_less_then_6(gunners)

# Function call to find items with greater 8 (Question 1 part D)
length_greater_than_equal(gunners)

# Function call to find longest and shortest items (Question 1 part E)
longest_Shortest_Words(gunners)
