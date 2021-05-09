from transformers import AutoModelForMaskedLM, AutoTokenizer
import torch
import csv
import numpy as np

model_tok="bert-large-cased"
tokenizer = AutoTokenizer.from_pretrained(model_tok)  
model = AutoModelForMaskedLM.from_pretrained(model_tok)

tab=[]
table=[]
t=""

with open('Data/Ajout2.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=';', quotechar='|')
    for row in reader:
        tab.append(row)
print(tab)

for i in range(len(tab)-1):
    nu=tab[i+1][0]
    var=tab[i+1][1]
    for j in range(9):
        if(tab[i+1][j+3] != ""):
            region=j+1
            phrase=f""
            for k in range(9):
                if(k!=j):
                    phrase=phrase+" "+tab[i+1][k+3]
                else:
                    s=tab[i+1][j+3].split()
                    if(s):
                        s2=f""
                        for s1 in range(len(s)-1):
                            s2=s2+" "+s[s1]
                        phrase=phrase+" "+s2+" "+f"{tokenizer.mask_token}"
                        label=s[-1]
        t1=t
        t=[nu,var,region,phrase,label,"BERT","Anglais",0]
        if(t!=t1):
            table.append(t)


def resultat(sequence,labels):
    input_ids = tokenizer.encode(sequence, return_tensors="pt")
    mask_token_index = torch.where(input_ids == tokenizer.mask_token_id)[1]

    token_logits = model(input_ids)[0]
    mask_token_logits = token_logits[0, mask_token_index, :]
    mask_token_logits = torch.softmax(mask_token_logits, dim=1)
    
    #On calcul le mot qui obteint le meilleur score
    top = torch.topk(mask_token_logits, 1, dim=1)
    #top_5_tokens = zip(top.indices[0].tolist(), top.values[0].tolist())
    #On imprime la phrase avec le mask
    #print(sequence)
    #for token, score in top_5_tokens:
        #On calcul surprisal grace au score et on affiche le meilleur score
        #surprisal=-np.log2(score)
        #print(sequence.replace(tokenizer.mask_token, tokenizer.decode([token])), f"(score: {score}), surprisal: {surprisal}")

    # On calcule le score et surprisal pour le label
    sought_after_token = labels
    sought_after_token_id = tokenizer.encode(sought_after_token, add_special_tokens=False)[0]  # 928

    token_score = mask_token_logits[:, sought_after_token_id]
    #print(f"Score of {sought_after_token}: {mask_token_logits[:, sought_after_token_id]}")
    
    surprisal=-torch.log2(mask_token_logits[:, sought_after_token_id])
    #On affiche le score et surprisal pour le mot que l'on attendait
    #print(sequence.replace(tokenizer.mask_token, labels), f"(score: {mask_token_logits[:, sought_after_token_id].item()}, surprisal : {surprisal.item()})")
    return surprisal.item()
 
    

for i in range(len(table)):
    phrase=table[i][3]
    lab=table[i][4]
    res=resultat(phrase,lab)
    table[i][7]=res
    print(table[i])
        


# Imprimer le résultat dans un csv
cfile = csv.writer(open('Resultats/Ajout2_EN.csv', "w"))
cfile.writerow(['numero','variable','region','model','langue','surprisal'])

for [a,b,c,d,e,f,g,h] in table:
    cfile.writerow([a,b,c,f,g,h])