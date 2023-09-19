"""
This takes a string and checks if its a palindrome

1) create a flag and set it to true 

2) do a for loop and check each character one by one 

3) on the loop if one character is off then set the flag to false

4) create an if statement based on flag if true print its a palindrome
otherwise its not a palindrome 


"""


def isPalindrome(string):
    flag = 1

    for i in range(0, len(string)):
        if string.lower()[i] != string.lower()[len(string) - 1 - i]:
            flag = 0
            break

    if flag == 1:
        print("This is a Palindrome")
    else:
        print("This is not a Palindrome")


isPalindrome("Rotator")




