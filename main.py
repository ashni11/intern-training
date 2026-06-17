from week1.conditionals import mainconditions
from week1.functions import mainfunctions
from week1.hello import mainhello
from week1.loops import mainloops
from week2.oops_advanced import mainoops_adv
from week2.oops_basics import mainoops_basics



print ("1.conditions")
print ("2.functions")
print ("3.hello")
print ("4.loops")
print("5.oops_basics")
print("6.oops_advanced")
choice = int(input("Enter your choice (1-4): "))
if choice == 1:
    mainconditions()
elif choice == 2:
    mainfunctions()
elif choice == 3:
    mainhello()
elif choice == 4:
    mainloops()
elif choice ==5:
    mainoops_basics()
elif choice ==6:
    mainoops_adv()
else:
    print("invalid")