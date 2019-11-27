import pandas as pd

cars = pd.read_csv('cars.csv')

B = cars.head()
C = cars.tail()

print (B)
print (C)
