mysquare = lambda x:x*x
print(mysquare(5))

mysum= lambda x,y:x+y
print(mysum(12,3))

new_sum= lambda *args:sum(args)
print(new_sum(12,13,15))

numbers=[12,23,45,767,12,435,23,44,78,23,12,24]
even_numbers=list(filter(lambda x:x%2==0,numbers))
print(even_numbers)


def myfunction(num):
    return lambda x: x*num
ten_multipler=myfunction(10)
print(ten_multipler(10))

