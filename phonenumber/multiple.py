class parent:
    def func1(self):
         print("this is function1")


class parent2:
    def func3(self):
        print("this is function3")


class child(parent,parent2):
    def func2(self):
        print("this is function2")

ob = child()
ob.func1()
ob.func3()