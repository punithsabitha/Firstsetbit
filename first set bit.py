# Program to find position of the first set bit

n = int(input("Enter number: "))

pos = 1
while n > 0:
    if n & 1 == 1:
        print("Position of the first set bit:", pos)
        break
    n = n >> 1
    pos += 1
