import csv, os

def csv_finder():
    return [_ for _ in os.listdir('.') if _.endswith('.csv')]

def selection(table, test):
    return [line for line in table if test(line)]

def csv_opener():
    with open(csv_finder()[0], "r") as f:
        reader = csv.reader(f, delimiter=";")
        table = [line for line in reader]
        #table = table[1:]
        f.close()
    return table

table = csv_opener()

column = {"reg":"","clage_vacsi":"","n_dose1_e":"","n_complet_e":"","n_rappel_e":"",
        }

for element in column:
    i=-1
    while table[0][i] != element:
        column.update({element:str(i+1)})
        i+=1

print(column)
