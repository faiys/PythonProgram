import sys
import pandas as pd

import matplotlib.pyplot as plt

class PandasWrapper():
    def __init__(self):
        pass

    def version(self):
        print("\t\t\t **PD Version** \t\t\t")
        return pd.__version__

    def csv(self):
        print("\t\t\t **Max Row return only 60 rows default** \t\t\t")
        print(pd.options.display.max_rows)
        print("\t\t\t **Read CSV** \t\t\t")
        pd.options.display.max_rows = 2
        read_csv_var = pd.read_csv("Data/Org Users.csv")
        print(read_csv_var.to_string())
        print(read_csv_var)

    def CreateSeries(self):
        print("\t\t\t **one-dimensional array** \t\t\t")
        one_Diamond_array = [1, 5 , 3, 10]
        arr_myseries = pd.Series(one_Diamond_array, index=["x","y","z","A"])
        one_Diamond_Json = {"Name": "Fai", "Age": 18}
        json_myseries = pd.Series(one_Diamond_Json)
        print(arr_myseries["y"])
        print(json_myseries)

    def createDataFram(self):
        print("\t\t\t **DataFrame** \t\t\t")
        myFram = pd.DataFrame(
            {
                'Customer Name':["Mohamed","Faiyas", "Ali"],
                'Customer Age':[20,22, 17],
                'Amount':[10000,9000, 1000]
            },index=["Sno1","Sno2","Sno3"])
        print(myFram)
        print("\t\t\t **DataFrame use Loc Atttribute** \t\t\t")
        print(myFram.loc["Sno3"])
        print(myFram.loc[["Sno1","Sno2"]])

    def analyzing_date(self):
        print("\t\t\t **Analyzing Data using head()** \t\t\t")
        print("\t\t\t **head() defauld 5 row. head(100) show first 100 rows** \t\t\t")
        hear_var = pd.read_csv("Data/Org Users.csv")
        print(hear_var.head(2))
        print("\t\t\t **tail() defauld 5 row. tail(100) show last 100 rows** \t\t\t")
        print(hear_var.tail(2))
        print("\t\t\t **info() show details from given csv ** \t\t\t")
        print(hear_var.info())

    def correlation(self):
        print("\t\t\t  *correlation corr()* \t\t\t")
        data = {
            'A': [1, 2, 3, 4, 5],
            'B': [5, 4, 3, 2, 1],
            'C': [2, 2, 3, 4, 4]
        }
        MyFrame = pd.DataFrame(data)
        print(MyFrame)
        corr_var = MyFrame.corr()
        print(corr_var)
    
    def plots(self):
        print("\t\t\t  *Plots for visuala Diagram* \t\t\t")
        data = {
            'A': [1, 2, 3, 4, 5],
            'B': [5, 4, 3, 2, 1],
            'C': [2, 2, 3, 4, 4]
        }
        myFrD = pd.DataFrame(data)
        # Default plot
        myFrD.plot()
        # Scatter plot ('line', 'bar', 'barh', 'kde', 'density', 'area', 'hist', 'box', 'pie', 'scatter', 'hexbin')
        myFr = pd.read_csv("Data/Org Users.csv")
        # myFr.plot(kind = 'scatter', x="A",y="C")
        myFr.plot(kind = 'scatter', x='First Name', y = 'User Status')
        plt.show()

pan_obj = PandasWrapper()
# methods = [method for method in dir(pan_obj) if callable(getattr(pan_obj, method)) and not method.startswith("__")]
# print(methods)
methods = [method for method in dir(pan_obj) if not method.startswith("__")]
methods.insert(0, 'Exit')
while True:
    print([f'{method_name} - {methods.index(method_name)}' for method_name in methods])
    filter_var = int(input('Enter the values:'))
    for methName in methods:
        if methods.index(methName) == filter_var:
            if filter_var == 0:
                sys.exit()
            callAttr = getattr(pan_obj, methName)
            if callable(callAttr):
                try:
                    print(callAttr())
                except Exception as e:
                    print(f"Error calling {methName}():", e)
                break



