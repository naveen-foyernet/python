class parent:
    def func1(self):
         print("this is function1")


class parent2(parent):
    def func3(self):
        print("this is function3")


class child:
    def func2(self):
        print("this is function2")

ob = child()
ob1= parent2()
ob.func1()
ob1.func1()