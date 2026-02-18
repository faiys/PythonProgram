import time
import asyncio

data_list = ["Mohamed", "Faiyas", "Ali"]

class Solution():
    def __init__(self):
        pass

    def instanceExecute(self, name):
        return name
    
    def setTime(self, name):
        time.sleep(1)
        return name

    async def inner_async(self, name):
        await asyncio.sleep(1)
        return name


obj = Solution()

# Call time and normal function
for inx, i in enumerate(data_list):
    if inx != 0:
        result = obj.setTime(i)
    else:
        result = obj.instanceExecute(i)
    print(result)

# call async functions. This will execute as concurrently
# Note: If A task is failed, rest of tast will cancel automatically
# If i add return_exceptions=True, all task will work without cancel. 
async def runAsync():
    # This will work if the task task-A must finish first, task-B waits for task-A
    res1 = await obj.inner_async("Mohamed")
    res2 = await obj.inner_async(f"{res1} Faiyas")
    res3 = await obj.inner_async(f"{res2} Ali")
    print(res3)

    # This will work if tasks are running independenly
    result = await asyncio.gather(
        *[obj.inner_async(i) for i in data_list],
        return_exceptions=True
    )
    print(result)

asyncio.run(runAsync())