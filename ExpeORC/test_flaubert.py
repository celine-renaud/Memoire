from transformers import AutoModelForMaskedLM, AutoTokenizer
import torch
import csv
import numpy as np
from transformers import pipeline
from transformers import AutoTokenizer, AutoModel
tab=[]
table=[]


nlp = pipeline('fill-mask', model='bert-base-multilingual-cased')
with open('Data/ORC_fr.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=';', quotechar='|')
    for row in reader:
        tab.append(row)

for i in range(len(tab)-1):
    nu=tab[i+1][0]
    var=tab[i+1][1]+tab[i+1][2]
    for j in range(8):
        region=j+1
        phrase=f""
        for k in range(8):
            if(k!=j):
                phrase=phrase+" "+tab[i+1][k+3]
            else:
                s=tab[i+1][j+3].split()
                s2=f""
                for s1 in range(len(s)-1):
                    s2=s2+" "+s[s1]
                phrase=phrase+" "+s2+" "+f"{nlp.tokenizer.mask_token}"
                label=s[-1]
        t=[nu,var,region,phrase,label,"BERT","Français",0]
        table.append(t)

def resultat(sequence,labels):
    s=nlp(sequence, targets=labels)
    score=s[0]["score"]
    surprisal=-np.log2(score)
    #On affiche le score et surprisal pour le mot que l'on attendait
    #print(sequence.replace(tokenizer.mask_token, labels), f"(score: {mask_token_logits[:, sought_after_token_id].item()}, surprisal : {surprisal.item()})")
    return surprisal
 
    

for i in range(len(table)):
    phrase=table[i][3]
    lab=table[i][4]
    res=resultat(phrase,lab)
    table[i][7]=res
    print(table[i])
        


# Imprimer le résultat dans un csv
cfile = csv.writer(open('Resultats/Resultat_FR_BERT_multi.csv', "w"))
cfile.writerow(['numero','variable','region','model','langue','surprisal'])

for [a,b,c,d,e,f,g,h] in table:
    cfile.writerow([a,b,c,f,g,h])

















