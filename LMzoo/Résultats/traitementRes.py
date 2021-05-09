import csv

tab=[]
with open('an_ORC.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=';', quotechar='|')
    for row in reader:
        tab.append(row)
 
res=[]       
with open('Resultats_lstm_1.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=';', quotechar='|')
    for row in reader:
        res.append(row)

t=0
table=[]
for i in range(len(tab)-1):
    nu=tab[i+1][0]
    var=tab[i+1][1]+tab[i+1][2]
    for j in range(8):
        region=j+1
        seq=tab[i+1][j+3].split()
        label=seq[-1]
        t=[nu,var,region,label,"lstm","anglais",0]
        table.append(t)

print(res)

for i in range(len(table)-1):
    for j in range(len(res)-1):
        if(table[i+1][1]==res[j+1][4]+res[j+1][5]):
                if(table[i+1][0]==res[j+1][0]):
                    if(table[i+1][3]==res[j+1][2]):
                        table[i+1][-1]=res[j+1][3]

cfile = csv.writer(open('Resultat_lstm_finaux.csv', "w"))
for [a,b,c,d,e,f,g] in table:
    cfile.writerow([a,b,c,d,e,f,g])