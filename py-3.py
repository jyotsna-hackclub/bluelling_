print("This is your report card, please enter the appropriate information correctly.")
marks=int(input("Enter your total percentage:"))
if marks>=90:
    print("You have an A grade, congratulations!")
elif marks>=80:
    print("You have scored a B grade, good job!")
elif marks>=70:
    print("You have got a C grade.")
elif marks>=60:
    print("You have got a D grade.")
elif marks>=50:
    print("You have got an E grade.")
elif marks>=40:
    print("You got an F grade, you need to work harder next time!")
else:
    print("You have failed, work harder next time!")
    