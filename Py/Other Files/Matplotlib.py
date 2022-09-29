import matplotlib.pyplot as plt

from pandas import DataFrame

a = [10, 20, 30, 40]
b = [50, 60, 70, 80]
c = [90, 100, 110, 120]
d = [25, 35, 45, 55]

data = {"Hindi": a, "English": b, "Maths": c, "Science": d}

df = Dataframe(data, index = ["Aman", "Naman", "Kartik", "Hridyansh"])
print(df)