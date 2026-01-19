class stack():
    def __init__(self, nums):
        self.nums = nums
    
    def push(self, appendList):
        self.nums.extend(appendList)
        # return self.nums
    
    def pop(self):
        self.nums.pop()
        # return self.nums
    
    def peek(self):
        return self.nums[-1] if self.nums else None
        

my_list = [1,2]
obj = stack(my_list)
obj.push([3,4])
print(obj.peek())
obj.pop()
print(obj.peek())

        
    