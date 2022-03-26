import csv
import os
import matplotlib.pyplot as plt

def csv_finder():
    return [_ for _ in os.listdir('.') if _.endswith('.csv')]

with open(csv_finder()[0], "r") as f:
    reader = csv.reader(f, delimiter=";")
    table = [line for line in reader]
    table = table[1:]
    f.close()

dates, p = [], 0

while table[p][1] == table[0][1]:
    dates.append(table[p][2])
    p += 1

def selection(table, test):
    return [line for line in table if test(line)]

region = "44"

selection1 = selection(table, lambda line: line[1]=="0" and line[0]==region)

y = [int(line[24]) for line in selection1]
v = [int(line[25]) for line in selection1]
u = [int(line[26]) for line in selection1]

color1 = "#A2CBE6"
color2 = "#1796E6"
color3 = "#0676BD"

plt.plot(dates, y, color=color1, label="personnes partiellement vacciner")
plt.plot(dates, v, color=color2, label="personnes totalement vacciner")
plt.plot(dates, u, color=color3, label="pzeqonnzq vacciner (rappel)")

plt.fill_between(dates, y, color=color1)
plt.fill_between(dates, v, color=color2)
plt.fill_between(dates, u, color=color3)

plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc='lower center', ncol=3, borderaxespad=0.)
plt.xticks(range(1, len(dates), int(len(dates)/7)))
plt.xlim(dates[0], dates[-1])
plt.ylim(y[0], y[-1]+100000)
plt.show()
