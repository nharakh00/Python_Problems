

n = 5

for i in range(0, 5):
    for j in range(0,5):
        print("#", end=" ")
    print()

print()


# Increasing Triangle  
for i in range(0,n):
    for j in range(0,i):
        print("#", end=" ")
    print()


print()    

# Decreasing Triangle Pattern

for i in range(0, n):
    for j in range(0, n - i - 1):
        print("#", end= " ")
    print()

print()






# Think of the above two patterns as building blocks
# https://www.youtube.com/watch?v=xzstcj3Cuso&list=WL&index=3&t=1004s&ab_channel=SimplyCoding






# Regular Triangle

for i in range(0,n):
    for j in range(0,n-i -1):
        print(end=" ")

    for j in range(0, i):
        print("#", end=" ")
    print()

print()

# Left Triangle
for i in range(0,n):
    for j in range(0,i):
        print(" ", end=" ")

    for j in range(0, n-i-1):
        print("#", end=" ")
    print()





# Right Triangle

for i in range(0, n):
    for j in range(0, n - i - 1):
        print(" ", end= " ")
    for k in range(0, i):
        print("#", end=" ")
    print()








    


        
        
