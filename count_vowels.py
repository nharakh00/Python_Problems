"""
Count Vowels – Enter a string and the program counts the number of vowels
in the text. For added complexity have it report a sum of each vowel found.

1) Create counter variable
2)iterate through string and count each vowel in the string
3) return the number of vowels
"""


def count_vowels(string):

    # Defining counter variable
    counter = 0

    #looping through string
    for i in range(0, len(string)):
        # checking for vowel
        if(string[i] == 'a' or string[i] == 'e' or string[i] == 'i' or string[i] == 'o' or string[i] == 'u'):
            # Incrementing counter 
            counter += 1

    return counter


print(count_vowels('coffee'))
