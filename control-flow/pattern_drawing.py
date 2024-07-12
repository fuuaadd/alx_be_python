size = 0
n = int(input("Enter the size of the pattern:"))
while size < n:
    for i in range(n):
        print("*", end="")
    size+=1
    print()