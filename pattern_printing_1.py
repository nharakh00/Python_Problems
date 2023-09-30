"""
# This is the code for a square or rectangle 


print("First enter a height. Next enter a width.\n")

r = int(input())
c = int(input())

row = ""
shape = ""


for i in range(0,c):
    row = row + '#'
row = row + '\n'
    

for j in range(0, r):
    shape = shape + row

print(shape)
"""



# This is the code for a right pyramid 

print("How many rows for do you want for the right pyramid?")
rows = int(input())

for i in range(0, rows + 1):
    for j in range(0, i):
        print("#", end = " ")
    print()




"""

print("How many rows do you want for the left pyramid?\n")

# number of rows 
rows = int(input())

# Iterating value for column - This is the trick to this problem 
k = 2*rows-2

# Loop through rows 
for i in range(rows):
    #print(i) number of iteration is equal to the rows
    for j in range(k):
        print(end = " ")

    # Updating value of k
    k = k-2


    # Loop to print '#'
    for j in range(i + 1):
         print("#", end=" ")
    print()


"""
































