import math

print("Select no. to calculate your desire shape",
                   "1. Square",
                   "2. Rectangle",
                   "3. Triangle",
                   "4. Circle")
choose = float(input("Enter your choice"))

if choose == 1:
    side = float(input("Enter side"))
    area = side ** 2
    print(area)

elif choose == 2:
    length = float(input("Enter length"))
    width = float(input("Enter width"))
    area = length * width
    print(area)

elif choose == 3:
    height = float(input("Enter Height"))
    base = float(input("Enter base"))
    area = (height * base) / 2
    print(area)

elif choose == 4:
    radius = float(input("Enter radius"))
    area = math.pi * (radius ** 2)
    print(area)
    
else:
    print("Invalid input")