class solution:
    def __init__(self):
        self.reverse_str = ""
        
    def line(self, name):
        print(f"--------{name}---------")
    
    def inputValidate(self, n, type):
        if not isinstance(n, type):
            raise TypeError(f"n must be {type}")
        
    def reverseStr(self, stri:str):
        self.line("Reverse Str")
        self.inputValidate(stri, str)
        for i in stri:
            self.reverse_str = i + self.reverse_str
        return self.reverse_str
    
    def inBuildPalidrome(self, name:str):
        self.line("Inbuild Palidrome")
        self.inputValidate(name, str)
        name = name.lower()
        return name[::-1]
        
    def CustomPalindrome(self, name:str):
        self.line("Custom Palindrome")
        self.inputValidate(name, str)
        name = name.lower()
        left , right = 0, len(name)-1
        while left < right:
            if name[left] != name[right]:
                return f"{name} is not polindrome"
            left +=1
            right -=1
        return f"{name} is polindrome"
    
    def RemoveDuplicatePreventList(self, input_list:list[int]):
        self.line("Remove Duplicate Prevent List")
        self.inputValidate(input_list, list)
        seen = set()
        op_list = []
        for i in input_list:
            if i not in seen:
                seen.add(i)
                op_list.append(i)
        return op_list
    
    def CountUniqueLisOfDict(self):
        self.line("Count Unique List of Dict")
        input_dict= [
            {"name" : "Mohamed","age":12},
            {"name" : "Faiyas","age":15},
            {"name" : "Mohamed","age":12},
            {"name" : "Faiyas","age":18},
            ]
        op = {i["name"] for i in input_dict}
        return op
        
    def TwoSum(self, target:int):
        self.line("Two Sum")
        self.inputValidate(target, int)
        input_list = [5,2,8,7]
        seen = {}
        for inx, i in enumerate(input_list):
            diff = target - i
            if diff in seen:
                op =  [seen[diff], inx]
                return [input_list[j] for j in op]
            seen[i] = inx
    
    def missingNumber(self, input_list: list[int]):
        self.line("Missing Number")
        self.inputValidate(input_list, list)
        lastnum = len(input_list) + 1
        calculate_val = lastnum * (lastnum + 1) // 2
        return calculate_val - sum(input_list)
        
    def fibbonacciGenerator(self, n:int):
        self.line("Fibbonacci Using Generator")
        self.inputValidate(n, int)
            
        def generator(n):
            a, b = 0,1
            while a < n:
                yield a
                a , b = b, a+b
        return list(generator(n))
            
        
        
obj = solution()
print(obj.reverseStr("Mohamed"))
print(obj.inBuildPalidrome("Mom"))
print(obj.CustomPalindrome("Mom"))
print(obj.RemoveDuplicatePreventList([2,5,2,4,9,8,9]))
print(obj.CountUniqueLisOfDict())
print(obj.TwoSum(9))
print(obj.missingNumber([1, 2, 3, 4, 5, 7]))
print(obj.fibbonacciGenerator(10))