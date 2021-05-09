import csv

tab=[]

with open('Resultats/Resultat_EN_BERT.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=';', quotechar='|')
    for row in reader:
        tab.append(row)
tableau=[]
print(tab)
for i in range(len(tab)-1):
    tab[i+1][1]=tab[i+1][1]+"Gap"
    if(int(tab[i+1][2])>6):
        tab[i+1][2]=int(tab[i+1][2])+1
    tableau.append(tab[i+1])
    
tab=[]
with open('Resultats/Resultat_EN_BERT_noGap.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in reader:
        tab.append(row)

for i in range(len(tab)-1):
    tab[i+1][1]=tab[i+1][1]+"NoGap"
    tableau.append(tab[i+1])


        
cfile = csv.writer(open('Resultats/Resultat_EN_BERT_Gap_et_noGap.csv', "w"))
cfile.writerow(['numero','variable','region','model','langue','surprisal'])

for i in range(len(tableau)):
    cfile.writerow(tableau[i])
