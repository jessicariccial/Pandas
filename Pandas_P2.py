import pandas as pd

cars = pd.read_csv('cars.csv')

Z = cars.iloc[0:5:,range(0,11,2)]
Y = cars.loc[cars['Model']=='Mazda RX4']
X = cars.loc[cars['Model']=='Camaro Z28', ['cyl']]
W = cars.loc[cars['Model']=='Mazda RX4 Wag', ['cyl', 'gear']]
V = cars.loc[cars['Model']=='Ford Pantera L', ['cyl', 'gear']]
U = cars.loc[cars['Model']== 'Honda Civic', ['cyl', 'gear']]

print(Z)
print(Y)
print(X)
print(W)
print(V)
print(U)
