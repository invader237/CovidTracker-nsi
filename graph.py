import csv
import os
import matplotlib.pyplot as plt

def start(reg):
    cumul_vacs_plot(reg)

def csv_finder():
    return [_ for _ in os.listdir('.') if _.endswith('.csv')]

def selection(table, test):
    return [line for line in table if test(line)]

def csv_opener():
    with open(csv_finder()[0], "r") as f:
        reader = csv.reader(f, delimiter=";")
        table = [line for line in reader]
        table = table[1:]
        f.close()
    return table


def cumul_vacs_plot(reg):
    """
        Function: generate the first plot
        
        Input: 
            -'reg' the number of the region

        Returns: ---

        Local variables:
            -'dates' the liste of all the date to diplay
            -'selection1' a table of the data for the good region
            -'y', 'v', 'u' a list containing the number of people vaccinated (according to certain criteria) since the start of the pandemic
            -'color' a list of color in hexa to color the plot
            -'table' the content of the csv file
    """ 
    dates, p, table = [], 0, csv_opener()

    color = ["#A2CBE6", "#1796E6", "#0676BD"]
    
    while table[p][1] == table[0][1]:
        dates.append(table[p][2])
        p += 1

    selection1 = selection(table, lambda line: line[1]=="0" and line[0]==reg)

    y = [int(line[31]) for line in selection1]
    v = [int(line[32]) for line in selection1]
    u = [int(line[33]) for line in selection1]

    #gives the different curve their value, color, title
    plt.plot(dates, y, color=color[0], label="Personnes partiellement vacciner")
    plt.plot(dates, v, color=color[1], label="Personnes totalement vacciner")
    plt.plot(dates, u, color=color[2], label="Personnes vacciner (rappel)")

    #fills the space between the curve and the abscissa
    plt.fill_between(dates, y, color=color[0])
    plt.fill_between(dates, v, color=color[1])
    plt.fill_between(dates, u, color=color[2])

    #position the legend above the graph
    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc='lower center', ncol=3, borderaxespad=0.)

    #allows to display only certain values ​​on the axes
    plt.xticks(range(1, len(dates), int(len(dates)/7)))
    plt.yticks([10000000, 20000000, 30000000, 40000000, 50000000, 60000000, 70000000])

    #remove space between curves and axes
    plt.xlim(dates[0], dates[-1])
    plt.ylim(y[0], y[-1]+500000) 

    #displays a grid over the graph for easy reading
    plt.grid()

    #display the plot
    plt.show()

