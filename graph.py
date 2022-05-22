import csv
import os
import matplotlib.pyplot as plt

def start(reg):
    cumul_vacs_plot(reg)
    evol_vacs_cov(reg)
    

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

table = csv_opener


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
    plt.plot(dates, y, color=color[0], label="Personnes partiellement vacciné")
    plt.plot(dates, v, color=color[1], label="Personnes totalement vacciné")
    plt.plot(dates, u, color=color[2], label="Personnes vacciné (rappel)")

    #fills the space between the curve and the abscissa
    plt.fill_between(dates, y, color=color[0])
    plt.fill_between(dates, v, color=color[1])
    plt.fill_between(dates, u, color=color[2])

    #position the legend above the graph
    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc='lower center', ncol=3, borderaxespad=0.)

    #allows to display only certain values on the axes
    plt.xticks(range(1, len(dates), int(len(dates)/7)))
    plt.yticks([10000000, 20000000, 30000000, 40000000, 50000000, 60000000, 70000000], [10,20,30,40,50,60,70])
    

    #remove space between curves and axes
    plt.xlim(dates[0], dates[-1])
    plt.ylim(y[0], y[-1]+500000) 

    #displays a grid over the graph for easy reading
    plt.grid()
    
    #display the title
    plt.title('Nombre cumulé de personnes vaccinées',fontsize=20,backgroundcolor='white',y=1.07, loc='center')

    #display the plot
    plt.show()

def evol_vacs_cov(reg):
    table = csv_opener()
    
    vaccins_covid0=selection(table, lambda ligne:ligne[0]==str(reg) and ligne[1]=="0")#table, lambda ligne:ligne[0]==reg and ligne[1]=="0"

    labels=["0-4 ans","5-9 ans","10-11 ans","12-17 ans","18-24 ans","25-29 ans","30-39 ans","40-49 ans","50-59 ans","60-64 ans","65-69 ans","70-74 ans","75-79 ans","80 ans et +"]
    couleurs=['indigo','darkblue','mediumblue','royalblue','lightgreen','yellow','gold','orange','darkorange','chocolate','coral','tomato','orangered','red']
    
    plt.figure(1, figsize=(10.88, 8.16), frameon=False)
    figure, ax = plt.subplots(figsize=(10.88, 8.16))
            
    classeA=["4","9","11","17","24","29","39","49","59","64","69","74","79","80"]
    
    for i in range(len(classeA)):
        k=int(classeA[i])
        vaccins_covid1=selection(table, lambda ligne:ligne[0]==reg and ligne[1]==classeA[i])
        X=[ligne[2] for ligne in vaccins_covid1]
        Y=[float(ligne[-2]) for ligne in vaccins_covid1]
        if Y==[]:
            y=0
        else:
            y=Y[len(Y)-1]
                
        plt.plot(X,Y,label=labels[i],color=couleurs[i])
        
        plt.text(len(vaccins_covid0),y, labels[i], ha='left', va='center', fontsize = 7, color=couleurs[i])
        
        tickLabels = [i for i in range(0,len(vaccins_covid0),(len(vaccins_covid0)//14))]
        plt.gca().get_xaxis().set_ticklabels(tickLabels, fontsize = 8, rotation = 45)
        plt.xticks(tickLabels,['Jan 2021','Feb 2021','Mar 2021','Apr 2021','May 2021','Jun 2021','Jul 2021','Aug 2021','Sep 2021','Okt 2021','Nov 2021','Dec 2021','Jan 2022','Feb 2022','Mar 2022'],rotation=45)
        
        plt.grid(which='major', linestyle=':', axis='y', linewidth='0.5', color='darkgreen')
        plt.text(len(vaccins_covid0)//2,60,'60 %',fontsize=6, color='white',backgroundcolor='grey')
        plt.text(len(vaccins_covid0)//2,80,'80 %',fontsize=6, color='white',backgroundcolor='green')
        plt.text(len(vaccins_covid0)//2,100,'100 %',fontsize=6, color='white',backgroundcolor='darkgreen')
    
    plt.legend(loc='upper left',bbox_to_anchor=(-0.03,1.1,2,0),ncol=7) 
    
    plt.title('Evolution de la couverture vaccinale',loc='center',fontsize=20,backgroundcolor='white',y=1.1)
    #plt.tight_layout()
    plt.show()
    

evol_vacs_cov(44)
