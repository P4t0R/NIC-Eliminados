import pandas as pd
import time
import wget

from os import remove


#Elimina
try: 
    remove("Eliminados.txt")
except:
    pass


#Descarga datos
url= 'https://www.nic.cl/registry/Eliminados.do?t=1s&f=txt'

filename = wget.download(url, out='Eliminados.txt')


#Datos
f = open("Eliminados.txt", "r",encoding='utf-8')
dat1= f.readlines()


while True:
    letras = int (input('\ningresa la cantidad de letras '))
    Dominios=[]
    len_3 = []

    for i in dat1:
        i=i.strip().split(',')
        Dominios.append(i)
        if len(i[0]) == (letras + 3):
            len_3.append(i[0])
            
    print(f'Dominios encontrados: {len(len_3)}\n')
    time.sleep(2)
    sum=0
    for n in len_3:
        sum+=1
        n=n.replace('.cl', '')
        print(f'{sum}.- \t{n}') 
        if len(len_3) > 10:
            time.sleep(0.5)
