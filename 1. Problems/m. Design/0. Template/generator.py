# A simple generator for Fibonacci Numbers 
def fib(limit: int):   
    a, b = 0, 1

    while a < limit: 
        yield a 
        a, b = b, a + b 
  
# Generator using next
x = fib(5) 
  
print(x.next()) # In Python 3, __next__() 
print(x.next()) 
print(x.next())
  
# Generator using loop
for i in fib(5):  
    print(i) 