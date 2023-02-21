n = int(input("Enter a number (1 to 10): "))
if n<1 or n>10:
    print("Please enter number between 1 to 10 only")
else:
    for i in range (1, 11, 1):
        p = i*n
        print(i, "X" , n, "=", p)
