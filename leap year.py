year=int(input("enter the year to be checked:"))
if (year%4==0 and year%100!==0 or year%400==0):
    print("yes")
 else:
    print("no")
