import csv
import os
import matplotlib as plt

def csv_finder():
    return [_ for _ in os.listdir('.') if _.endswith('.csv')]

with open(csv_finder()[0], "r") as f:
    reader = csv.reader(f, delimiter=";")
    table = [line for line in reader]
    f.close()


somme = 0

for i in range(1, len(table)):
        if table[i][2] == "2022-03-21":
            somme += int(table[i][6])


plt.pyplot.plot("2022-03-21", somme, color='k')
plt.show()
