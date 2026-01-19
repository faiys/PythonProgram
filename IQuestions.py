class solution():
    def __init__(self, nums: list[int]):
        self.nums = nums
        
    def TwoSum(self, target):
        seen = {}
        for idx, num in enumerate(self.nums):
            diff = target - num
            if diff in seen:
                return [seen[diff], idx]
            seen[num] = idx
            
    def Fin(self, n):
        a, b = 0,1
        while a < n:
            yield a
            a,b = b, a+b
    
    def RemoveDuplicate(self):
        seen_set = set()
        op_list = list()
        for i in self.nums:
            if i not in seen_set:
                seen_set.add(i)
                op_list.append(i)
        return op_list
        
    def str_palin(self, mystr):
        return mystr.lower()[::-1]
        
    def palinLambda(self, mystr):
        return "".join(list(map(lambda x : x[::-1],list(mystr.lower()))))
    
    def palinmanual(self, mystr):
        left, right = 0, len(mystr) - 1
        while left < right:
            if mystr[left].lower() != mystr[right].lower():
                return False
            left+=1
            right -=1
        return True
        
    
        
        
myList = [5, 2, 7, 9, 2, 7]
mytarget = 9
obj = solution(myList)
op = obj.TwoSum(mytarget)
print(op)
print("*"*8)
for fin_series in obj.Fin(15):
    print(fin_series)
print("*"*8)
print(obj.RemoveDuplicate())
print("*"*8)
input_str = "Mom"
print(obj.str_palin(input_str))
print("*"*8)
print(obj.palinLambda(input_str))
print("*"*8)
print(f'{input_str} is palindrom' if obj.palinmanual(input_str) else f'{input_str} is not palindrom')

    
