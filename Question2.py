#! /usr/bin/python3
# Author: Wayne Robinson
# Number: 21205974
# Python Script Assignment1
# Script: Question2.py

# List Variable declaration
sentence = ''
third_letter_sentence =''
vowel_sentence = ''

# Display Function
def display_anwers():
    print("\n===================================================")

#=================== Question 2 Part A =========================
# Function call
display_anwers()

# Prompt user and take in sentence from user
sentence = input("Please enter sentence: ")
print("\nThe sentence enter by the user is: " + sentence)

#=================== Question 2 Part B =========================
display_anwers()

# String split, starting at postion 0, finish at the length of the sentence, with a step size of 3.
third_letter_sentence = sentence[0:len(sentence):3]
print("The new sentence with every third letter print out is: ", third_letter_sentence)

#=================== Question 2 Part C =========================
display_anwers()

# Iterate through sentence list.
for letter in sentence:

    # If statement to detect any vowels present in string, if so add to new string.
    if letter in 'aeiou' or letter in 'AEIOU':
        vowel_sentence = vowel_sentence + letter
    else:
        pass

print("The new sentence with each vowel printed is as follows: ", vowel_sentence)
