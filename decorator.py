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
