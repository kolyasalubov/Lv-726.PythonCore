class MyNumbers():
    def __init__(self,num):
        self.num = num      
    
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= self.num - 1:
            x= self.a
            self.a += 1
            return x
        else:
            raise StopIteration


myclass = MyNumbers(int(input("Enter a number:")))
custom_iterator = iter(myclass)
for value in custom_iterator:
    print(value)