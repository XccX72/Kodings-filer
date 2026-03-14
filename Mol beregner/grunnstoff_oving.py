import pandas as pd

df = pd.read_csv("Mol beregner/grunnstoffer.csv")

print(df.head())

len(df)

df.info()

x = int(input("Hvilket nummer er grunnstoffet du leter etter")) - 1

print(df.iloc[x])


mol = 6.022e23

