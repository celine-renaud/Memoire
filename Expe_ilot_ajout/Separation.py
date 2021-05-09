import csv

tab=[]

with open('Data/Ajout_FR.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=';', quotechar='|')
    for row in reader:
        tab.append(row)
tableau=[]

for i in range(len(tab)):
    for j in range(len(tab[i])-1):
        tableau.append([j+1,i+1,"français",tab[i][j+1]])


cfile = csv.writer(open('Data/Ajout_FR_separe.csv', "w"))
cfile.writerow(['numero','variable','langue','phrase'])

for [a,b,c,d] in tableau:
    cfile.writerow([a,b,c,d])



