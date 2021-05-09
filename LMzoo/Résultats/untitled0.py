import csv
import lm_zoo 


tab=[]
ORCpl=open("ORCpl.txt", "a")
ORCsg=open("ORCsg.txt", "a")
CMPsg=open("CMPsg.txt", "a")
CMPpl=open("CMPpl.txt", "a")

with open('an_ORC.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=';', quotechar='|')
    for row in reader:
        tab.append(row)
print(tab)       

for i in range(len(tab)-1):
    phrase=""
    for j in range(8):
        phrase=phrase+" "+tab[i+1][j+3]
    if(tab[i+1][1]=="ORC"):
            if(tab[i+1][2]=="pl"):
                ORCpl.write("\n"+phrase)
            else:
                ORCsg.write("\n"+phrase)
    else:
            if(tab[i+1][2]=="pl"):
                CMPpl.write("\n"+phrase)
            else:
                CMPsg.write("\n"+phrase)

CMPsg.close()
CMPpl.close()
ORCpl.close()
ORCsg.close()