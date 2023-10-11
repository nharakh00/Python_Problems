"""
# Pattern printing pyramid

n = int(input())
print(n)

# Let n = 2

for i in range(0, n):

    for j in range(i,n):
        print(end= " ")
    
    for k in range(0, i): 
        print("#", end = " ")

    print()
"""


"""
# Pattern printing inverted pyramid

n = int(input())
print(n)

for i in range(0, n):

    for j in range(0,i):
        print(end=" ")
    
    for k in range(i, n):
        print("#", end= " ")
    print()
"""



"""
# patter printing diamond - I think there is a better solution for this


print("Please Select size of diamond. Please note min size = 4 and only even numbers.")

n = int(input())
n = n /2
n = int(n)


for i in range(0, n):

    for j in range(i,n):
        print(end= " ")
    
    for k in range(0, i): 
        print("#", end = " ")

    print()

for i in range(0, n):

    for j in range(0,i):
        print(end=" ")
    
    for k in range(i, n):
        print("#", end= " ")
    print()
"""
