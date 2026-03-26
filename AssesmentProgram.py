class solution:
    def __init__(self):
        pass

    def RatHouse(self):
        # output 4
        r = int(input()) #7
        unit =  int(input()) #2
        house_arr = list(map(int,input().split())) # 2 8 3 5 4 1 2

        foods = r * unit
        total = 0
        if r==0:
            return 0
        else:
            for inx, i in enumerate(house_arr):
                total+=i
                if total >= foods:
                    return inx +1

    def RotateArray(self):
        arr = list(map(int, input().split())) # 1 2 3 4 5
        k = int(input()) #2
        
        k = k % len(arr)
        result = arr[-k:] + arr[:-k]
        return result

    def SecondLargeNumberUsingSort(self):
        arr = list(map(int,input().split())) #10 20 4 45 99
        removeDuplicate = list(set(arr))
        removeDuplicate.sort(reverse=True)
        return removeDuplicate[-2]
    
    def SecondLargeNumberWithoutSort(self):
        arr = [10,20,4,45,99]
        first = second = -1

        for num in arr:
            if num > first:
                second = first
                first = num
            elif num > second and num != first:
                second = num
        print(second)

    def CountVowels(self):
        n = "Faiyas"
        cnt = 0
        vowels = "aeiouAEIOU"
        for i in n:
            if i in vowels:
                cnt += 1
        return cnt



op = solution()
print(op.RatHouse())
# print(op.RotateArray())
# print(op.SecondLargeNumberUsingSort())
# print(op.SecondLargeNumberWithoutSort())
# print(op.CountVowels())

