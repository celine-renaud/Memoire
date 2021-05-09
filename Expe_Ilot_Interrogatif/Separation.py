import csv

tab=[]

with open('Data/BlocWH_FR.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=';', quotechar='|')
    for row in reader:
        tab.append(row)
tableau=[]

for i in range(len(tab)-1):
    for j in range(len(tab[i])-1):
        tableau.append([i+1,j+1,"frabçais",tab[i+1][j+1]])

cfile = csv.writer(open('Data/BlocWh_FR_separe.csv', "w"))
cfile.writerow(['numero','variable','langue','phrase'])

for [a,b,c,d] in tableau:
    cfile.writerow([a,b,c,d])



