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
        
    def lambdaPalindrome(self, name:str):
        self.line("lambda Palidrome")
        self.inputValidate(name, str)
        is_palin = lambda x : x == name[::-1]
        if  is_palin(name) == True:
            return f'{name} is palindrom'
        else:
            return f'{name} is not palindrom'
        
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
    
    def GetDuplicateFromList(self, input_list:list[int]):
        self.line("Get Duplicate from List")
        self.inputValidate(input_list, list)
        seen = set()
        duplicate = set()
        for i in input_list:
            if i not in seen:
                seen.add(i)
            else:
                duplicate.add(i)
        return duplicate

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
        lastnum = input_list[len(input_list) - 1]
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
            
    def groupByKey(self):
        self.line("Group by key")

        data = [
            {"name": "a", "dept": "IT"},
            {"name": "b", "dept": "HR"},
            {"name": "c", "dept": "IT"},
        ]

        result = {}
        for i in data:
            dept = i['dept']

            if dept not in result:
                result[dept] = []
            result[dept].append(i['name'])
        return result
        
    def Subtract(self, arr:list, op:int):
        # Take each candidate value (starting from largest) Subtract it from all elements . If any result equals op → return that candidate value (int) Else try next largest
        # 5-5 = 0 ->wrong
        # 5-6 = 1 ->wrong
        # 5-3 = 2 ->wrong
        self.line("ubtract it from all elements")

        uniq_sort = sorted(set(arr), reverse=True)
        for i in uniq_sort:
            if any(i-x == op for x in arr):
                return i
        return -1

    def WordFrequencyCount(self, text:str):
        self.line("Word Frequency Count")
        self.inputValidate(text, str)
        # {'hello': 2, 'world': 1}

        result = {}
        for i in text.split():
            if i in result:
                result[i] +=1
            else:
                result[i] =1 
        return  result




obj = solution()
# 
print(obj.reverseStr("Mohamed"))
print(obj.inBuildPalidrome("Mom"))
print(obj.lambdaPalindrome("Teacher"))
print(obj.CustomPalindrome("Mom"))
print(obj.RemoveDuplicatePreventList([2,5,2,4,9,8,9]))
print(obj.GetDuplicateFromList([2,5,2,4,9,8,9]))
print(obj.CountUniqueLisOfDict())
print(obj.TwoSum(9))
print(obj.missingNumber([1, 2, 3, 4, 6,7]))
print(obj.fibbonacciGenerator(10))
print(obj.groupByKey())
print(obj.Subtract([5, 6, 3], 3))
print(obj.WordFrequencyCount("hello world hello"))