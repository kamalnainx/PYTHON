# iterators 
# an iterator is object that contains a countable number.
#  iterator have to method :-
#  next()             iter()










# tuple1=("apple","banana","cherry")
# print(tuple1)
# print(tuple1[0])
# print(tuple1[1])
# print(tuple1[2])














# tuple1=("apple","banana","cherry")
# print(tuple1)
# miter1=iter(tuple1)
# print(next(miter1))
# print(next(miter1))
# print(next(miter1))














# tuple1="apple"
# print(tuple1)
# miter1=iter(tuple1)
# print(next(miter1))
# print(next(miter1))
# print(next(miter1))
# print(next(miter1))
# print(next(miter1))












# tuple1="apple"
# print(tuple1)
# for x in tuple1:
#     print(x, end="   ")


























# class Myclass1:
#     def __init__(self):
#         self.num1=0
#         # return self
#     def printop(self):
#         self.num1+=1
#         x=self.num1
#         return x

# mc1=Myclass1()
# print(mc1.printop())
# print(mc1.printop())
# print(mc1.printop())
# print(mc1.printop())
















# class Myclass1:
#     def __init__(self):
#         self.num1=0
#         # return self
#     def printop(self):
#         self.num1+=1
#         x=self.num1
#         return x

# mc1=Myclass1()
# for x in range(10):
#     print(mc1.printop())




























# class Myclass1:
#     def __iter__(self):
#         self.num1=2
#         return self

#     def __next__(self):
#         x=self.num1
#         self.num1*=self.num1
#         return x

# mc1=Myclass1()
# miter1=iter(mc1)
# print(next(miter1))
# print(next(miter1))
# print(next(miter1))
# print(next(miter1))

























class Myclass1:
    def __iter__(self):
        self.num1=2
        return self

    def __next__(self):
        if self.num1<=10:
            x=self.num1
            self.num1+=1
            return x
        else:
            raise StopIteration
mc1=Myclass1()
miter1=iter(mc1)

for x in miter1:
    print(x)






