import csv
import os
import matplotlib.pyplot as plt
import numpy as np

def start(reg):
    cumul_vacs_plot(reg)
    evol_vacs_cov(reg)
    vacs_age(reg, '2022-03-22')

    
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

table = csv_opener()


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
    dates, p = [], 0

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
    plt.savefig("image1.jpg",bbox_inches='tight')
    plt.show()



def evol_vacs_cov(reg):
    vaccins_covid0=selection(table, lambda ligne:ligne[0]==str(reg) and ligne[1]=="0")

    labels=["0-4 ans","5-9 ans","10-11 ans","12-17 ans","18-24 ans","25-29 ans","30-39 ans","40-49 ans","50-59 ans","60-64 ans","65-69 ans","70-74 ans","75-79 ans","80 ans et +"]
    couleurs=['indigo','darkblue','mediumblue','royalblue','lightgreen','yellow','gold','orange','darkorange','chocolate','coral','tomato','orangered','red']
    
    plt.figure(1, figsize=(10.88, 8.16), frameon=False)
    figure, ax = plt.subplots(figsize=(10.88, 8.16))
            
    classeA=["4","9","11","17","24","29","39","49","59","64","69","74","79","80"]
    
    for i in range(len(classeA)):
        k=int(classeA[i])
        vaccins_covid1=selection(table, lambda ligne:ligne[0]==str(reg) and ligne[1]==classeA[i])
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
    plt.tight_layout()
    plt.savefig("image2.jpg",bbox_inches='tight')

    plt.show()


def vacs_age(reg,date):
    
    fig, ax = plt.subplots()
            
    vaccins_covid1=selection(table, lambda ligne:ligne[0]==reg and ligne[1]=="0" and ligne[2]==date)

    vaccins_covid0=selection(table, lambda ligne:ligne[0]==str(reg) and ligne[1]=="0" and ligne[2]==date)
    vaccins_covid4=selection(table, lambda ligne:ligne[0]==str(reg) and ligne[1]=="04" or ligne[1]=="09" or ligne[1]=="11" and ligne[2]==date)
    vaccins_covid17=selection(table, lambda ligne:ligne[0]==str(reg) and ligne[1]=="17" and ligne[2]==date)
    vaccins_covid24=selection(table, lambda ligne:ligne[0]==str(reg) and ligne[1]=="24" or ligne[1]=="29" or ligne[2]==date)
    vaccins_covid39=selection(table, lambda ligne:ligne[0]==str(reg) and ligne[1]=="39" or ligne[1]=="49" and ligne[2]==date)
    vaccins_covid59=selection(table, lambda ligne:ligne[0]==str(reg) and ligne[1]=="59" and ligne[2]==date)
    vaccins_covid64=selection(table, lambda ligne:ligne[0]==str(reg) and ligne[1]=="64" and ligne[2]==date)
    vaccins_covid69=selection(table, lambda ligne:ligne[0]==str(reg) and ligne[1]=="69" or ligne[1]=="74" and ligne[2]==date)
    vaccins_covid79=selection(table, lambda ligne:ligne[0]==str(reg) and ligne[1]=="79" or ligne[1]=="80" and ligne[2]==date)
    
    Y4_rappel=[float(ligne[29]) for ligne in vaccins_covid4]
    Y17_rappel=[float(ligne[29]) for ligne in vaccins_covid17]
    Y24_rappel=[float(ligne[29]) for ligne in vaccins_covid24]
    Y39_rappel=[float(ligne[29]) for ligne in vaccins_covid39]
    Y59_rappel=[float(ligne[29]) for ligne in vaccins_covid59]
    Y64_rappel=[float(ligne[29]) for ligne in vaccins_covid64]
    Y69_rappel=[float(ligne[29]) for ligne in vaccins_covid69]
    Y79_rappel=[float(ligne[29]) for ligne in vaccins_covid79]
    
    Y4_tot=[float(ligne[28]) for ligne in vaccins_covid4]
    Y17_tot=[float(ligne[28]) for ligne in vaccins_covid17]
    Y24_tot=[float(ligne[28]) for ligne in vaccins_covid24]
    Y39_tot=[float(ligne[28]) for ligne in vaccins_covid39]
    Y59_tot=[float(ligne[28]) for ligne in vaccins_covid59]
    Y64_tot=[float(ligne[28]) for ligne in vaccins_covid64]
    Y69_tot=[float(ligne[28]) for ligne in vaccins_covid69]
    Y79_tot=[float(ligne[28]) for ligne in vaccins_covid79]
    
    Y4_part=[float(ligne[27]) for ligne in vaccins_covid4]
    Y17_part=[float(ligne[27]) for ligne in vaccins_covid17]
    Y24_part=[float(ligne[27]) for ligne in vaccins_covid24]
    Y39_part=[float(ligne[27]) for ligne in vaccins_covid39]
    Y59_part=[float(ligne[27]) for ligne in vaccins_covid59]
    Y64_part=[float(ligne[27]) for ligne in vaccins_covid64]
    Y69_part=[float(ligne[27]) for ligne in vaccins_covid69]
    Y79_part=[float(ligne[27]) for ligne in vaccins_covid79]
    
    x=['75 ans et plus', '65-74 ans', '55-64 ans', '50-54 ans', '30-49 ans', '18-29 ans', '12-17 ans', '0-11 ans']
    
    eff_rappel = [Y4_rappel,Y17_rappel,Y24_rappel,Y39_rappel,Y59_rappel,Y64_rappel,Y69_rappel,Y79_rappel]
    effectifs_rappel=list(reversed(eff_rappel))
    rappel=[]
    for i in range(len(effectifs_rappel)):
        if effectifs_rappel[i]==[]:
            rappel.append(0)
        else:
            rappel.append(effectifs_rappel[i][0])
    
    eff_tot = [Y4_tot,Y17_tot,Y24_tot,Y39_tot,Y59_tot,Y64_tot,Y69_tot,Y79_tot]
    effectifs_tot=list(reversed(eff_tot))
    tot=[]
    for i in range(len(eff_tot)):
        if effectifs_tot[i]==[]:
            tot.append(0)
        else:
            tot.append(effectifs_tot[i][0]-(effectifs_rappel[i][0]))
    
    eff_part = [Y4_part,Y17_part,Y24_part,Y39_part,Y59_part,Y64_part,Y69_part,Y79_part]
    effectifs_part=list(reversed(eff_part))
    part=[]
    for i in range(len(eff_part)):
        if effectifs_part[i]==[]:
            part.append(0)
        else:
            part.append(effectifs_part[i][0]-(rappel[i]+tot[i]))     
    
    non_vacc=[100]*8
    
    bar=plt.figure(1, figsize=(43.52, 32,64), frameon=False)
    
    ax.xaxis.set_major_formatter(ticker.PercentFormatter(xmax=100))

    plt.grid(which='major', linestyle=':', axis='x', linewidth='0.5', color='grey', zorder=0)
    
    x_pos = [i for i  in range(len(x))]
    plt.barh(x,non_vacc,color="whitesmoke",label="Non vaccinés",zorder=3)
    plt.barh(x,part,left=np.array(rappel)+np.array(tot),color="lightblue", label="Personnes partiellement vaccinées", zorder=3)
    plt.barh(x,tot,left=np.array(rappel),color="dodgerblue", label="Personnes totalement vaccinées", zorder=3)
    plt.barh(x,rappel,color="tab:blue",label="Personnes vaccinées (rappel)", zorder=3)
    
    plt.legend(loc='upper left',bbox_to_anchor=(-0.1,1.1,2,0),ncol=4)
       
    plt.title('Vaccinations par âge',loc="left",fontsize=25,y=1.1)
    plt.savefig("image3.jpg",bbox_inches='tight')
    plt.show()

start(44)

