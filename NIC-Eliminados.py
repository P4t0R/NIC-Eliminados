import pandas as pd
import time
import wget
import os


#Eliminamos datos antiguos 'data.txt'
if os.path.exists('data.txt'):
    os.remove('data.txt')


#Link descarga datos txt ultima semana nic.cl
url= 'https://www.nic.cl/registry/Eliminados.do?t=1s&f=txt'


#Descarga 'data.txt', contiene lista de dominios eliminados la última semana
filename = wget.download(url, out='data.txt')


#Leemos el archivo descargado 'Eliminados.txt'
f = open("data.txt", "r",encoding='utf-8')
dat1= f.readlines()


#Visualizamos los datos
while True:
    try:
        letras = int (input('\nIngrese longitud del dominio '))
    except:
        break


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

print('\nEspero que haya encontrado su nuevo Dominio!')