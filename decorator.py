# function based decorations
def wrapper(func):
    def inner(*args, **kwagrs):
        txt, sum = kwagrs['name'], func(*args, **kwagrs) * 2
        return f'{txt} - {sum}'
    return inner
        
@wrapper
def add(n, name):
    return n
    
tri = add(6, name="User")
print(tri)


# Class based decoration
class wrapper():
    def __init__(self, func):
        self.func = func
        
    def __call__(self, *args,**kwargs):
        return f'{kwargs["sname"]} rank is {self.func(*args,**kwargs)*2}'
        
@wrapper
def add(a, b, sname):
    return a+b

print(add(5, 2, sname="Mohamed"))

# Class based on funtion passing arguments
class wrapper():
    def __init__(self, name):
        self.name = name
        
    def __call__(self, func):
        def inner(*args,**kwargs):
            return f'{self.name} rank is {func(*args,**kwargs)*2}'
        return inner
    
        
@wrapper("Mohamed")
def add(a, b):
    return a+b

print(add(5, 2))