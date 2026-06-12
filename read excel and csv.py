import pandas as pd

winedatac=pd.read_csv('D:/4088/csv/wine.csv')

print(winedatac)
print(winedatac.head())
print("Shape\n",winedatac.shape)
print("Column\n",winedatac.columns)
print("Data Types\n",winedatac.dtypes)
print("ndim\n",winedatac.ndim)
print("Szie\n",winedatac.size)

winedatae=pd.read_excel('D:/4088/csv/wine.xls')

print('\n')
