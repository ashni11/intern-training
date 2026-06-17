def mainoops_adv():
    
    print("1.animal")
    print("2.shape")
    choice = int(input("Enter your choice (1-4): "))

    if choice ==1:
        class Animal:
            def speak(self):
                print("animal speaking")

        class dog(Animal):
            def speak(self):
                print("bark")

        class cat(Animal):
            def speak(self):
                print("meow")
                
                

        animal=[dog(), cat()]

        for i in animal:
            i.speak()
        
    elif choice ==2:
    #task 2 

        class shape :
            def __init__(self,name):
                self.name=name
            def area(self):
                pass
                
        class rectangle(shape):
            def __init__(self,l,b):
                super().__init__("rectangle")
                self.l=l
                self.b=b
                
            def area(self):
                return self.l * self.b
            
        class circle(shape):
            def __init__(self,r):
                super().__init__("cicle")
                self.r=r
                
            def area(self):
                return 3.14 *self.r * self.r
            
        r1 = rectangle(10, 5)
        c1 = circle(7)

        print(f"{r1.name} Area =", r1.area())
        print(f"{c1.name} Area =", c1.area())
            
            
    else:
        print("exit")
            