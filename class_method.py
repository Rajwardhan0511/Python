class Person:
    count = 0
    num = 0
    
    @classmethod
    def increment(cls):
        cls.count += 1
        cls.num += 2

Person.increment()
print(Person.count)  
print(Person.num)  
