#! /usr/bin/python3
# Author: Wayne Robinson
# Number: 21205974
# Python Script Assignment1
# Script: Question1.py

sentence = ''
third_letter_sentence =''
vowel_sentence = ''

#def user_input(sentence):
sentence = input("Please enter sentence: ")
print("The sentence enter by the user is: " + sentence)
#def third_letter(sentence):

third_letter_sentence = sentence[0:len(sentence):3]
print("The new sentence with every third letter print out is: ", third_letter_sentence)
    #return new_sentence

for letter in sentence:

    if letter in 'aeiou':
        vowel_sentence = vowel_sentence + letter

print("The new sentence with each vowel printed is as follows: ", vowel_sentence)

#user_input(sentence)
#print(third_letter(sentence))
