import numpy as np
import pandas as pd
import sys

class NumpyWrapper():

    def __init__(self):
        pass

    def readCSV(self):
        read_xls = pd.read_csv("Data/P_L_Query.csv")
        df = pd.DataFrame(read_xls)
        return df
    
    def makeArray(self):
        getFile = self.readCSV()
        # print(getFile0.to_string())
        convertNumpy = getFile.to_numpy()
        print(convertNumpy)
        # print([i for i in convertNumpy])
        original_arr = convertNumpy[10][1:5]
        copy_arr = convertNumpy[10][1:5].copy()
        print(original_arr)
        original_arr[0] = 2025
        print(original_arr)
        print(copy_arr)
        print(convertNumpy.reshape(2,convertNumpy.lenght))
        
        


# Calling class
numpyObj = NumpyWrapper()

# methods looping
methods = [method for method in dir(numpyObj) if not method.startswith("__") and method != "readCSV"]
methods.insert(0,'Exit')

while True:
    print([f'{methodName} - {methods.index(methodName)}' for methodName in methods])
    input_data = int(input("Enter the value:"))
    for method_name in methods:
        if input_data == methods.index(method_name):
            if input_data == 0:
                sys.exit()
            callAttr = getattr(numpyObj, method_name)
            if(callable(callAttr)):
                try:
                    print(callAttr())
                except Exception as e:
                    print(e) 
                break
