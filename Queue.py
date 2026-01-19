class queue():
    def __init__(self, nums):
        self.nums = nums
    
    def enqueue(self, n):
        self.nums.append(n)
    
    def dequeue(self):
        if not self.nums:
            return None
        return self.nums.pop(0)
    
    def display(self):
        return self.nums

obj = queue([])
obj.enqueue(1)
obj.enqueue(2)
obj.enqueue(3)
obj.enqueue(4)
print(obj.display())
print(obj.dequeue())
print(obj.dequeue())
print(obj.display())
        