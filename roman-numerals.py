#ROMAN NUMERAL PROGRAM
#This program will give users an opportunity
#to see what numbers 1-10 looks like when
#converted to Roman Numerals

#Set the constants
I=1
II=2
III=3
IV=4
V=5
VI=6
VII=7
VIII=8
IX=9
X=10

print("Roman Numeral Generator")

#Ask user to enter number 1-10
number = int(input("Please enter a number 1-10: "))
if number == I:
    print("This is Roman Numeral: I")
elif number == II:
    print("This is Roman Numeral: II")
elif number == III:
    print("This is Roman Numeral: III")
elif number == IV:
    print("This is Roman Numeral: IV")
elif number == V:
    print("This is Roman Numeral: V")
elif number == VI:
    print("This is Roman Numeral: VI")
elif number == VII:
    print("This is Roman Numeral: VII")
elif number == VIII:
    print("This is Roman Numeral: VIII")
elif number == IX:
    print("This is Roman Numeral: IX")
elif number == X:
    print("This is Roman Numeral: X")
else:
    print("Oops! You need to enter a number 1-10.")
