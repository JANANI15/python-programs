x = float(input("first number:"))
y = float(input("second number:"))
z = float(input("third number:"))
if (x > y) and (x > z):
   largest = x
elif (y > x) and (y > z):
   largest = y
else:
   largest = z
   print("the largest number is",largest)
