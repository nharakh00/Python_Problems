# This file contains a function that will take a string as input and reverse it

"""
This function takes a string as input and returns a reverse string

1) create empty string that represents the quote on quote reverse string

2) loop through the input string

3) during the loop concatenate the characters in reverse order  


"""


def reverse_string(string):
    """ Reverses a given string """
    rev_string = ""

    for i in range(0,len(string)):
        rev_string += string[len(string) - 1 - i ]

    return rev_string



my_str = "coffee"
new_str = reverse_string(my_str)

print(my_str)
print(new_str)
















    

