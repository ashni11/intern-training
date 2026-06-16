#question1

stored_password= "python123"
password=input("enter the password")
if stored_password == password:
    print("login validated")
else :
    print ("not able to login")
    
#question2
    
a = int(input("enter the numbers:")) 
b = int(input("enter the numbers:")) 
c = int(input("enter the numbers:")) 
if a>=b and a>=c:
    print("a is largest",a)
elif b>=a and b>=c:
    print("b is largest",b)
else:
    print ("c is largest",c)
    
    
#QUESTION 3
sum=0
for i in range(1,101):
    sum+=i
print(sum)


tasks=[]
def add_task(task):
    tasks.append(task)

    
def show_tasks():
    for task in tasks:
        print(task)
        
add_task("leraned python")
add_task("completed tasks")
show_tasks()


    
class bankaccount:
    def __init__(self,deposite):
        self.deposite = deposite
        
s1=bankaccount(1000)
