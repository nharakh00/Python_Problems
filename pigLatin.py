"""
Pig Latin – Pig Latin is a game of alterations played on the English language
game. To create the Pig Latin form of an English word the initial
consonant sound is transposed to the end of the word and an ay is affixed
(Ex.: "banana" would yield anana-bay).
Read Wikipedia for more information on rules.


1) we want to store the first character of a string in a variable.
2) Then we want to obtain the string with the first character removed
3) lastly we concatonate the string and "-first_characteray"
"""



def pig_latin(string):

    first_char = string[0]
    new_str = string[1:]
    pl_string = new_str + "-" + (first_char) + "ay"

    return pl_string



print(pig_latin("banana"))
