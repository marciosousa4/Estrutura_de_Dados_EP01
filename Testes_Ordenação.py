import math
from random import random
from random import randint
from random import shuffle
from time import time
from timeit import timeit
def principal():

  cabecalho()

  inicio = time()             
  fim = time()                

  qtd_elementos = 2000        
  
  while(fim - inicio <= 100):  

    tempos_ordenacao = []   
    buscas_totais = []          
    
    lista_original = gera_lista(qtd_elementos)  
    lista_copia = lista_original.copy()             

    tempos_ordenacao = calcula_tempo_ordenacao(lista_copia)

    imprime_resultados(qtd_elementos, tempos_ordenacao) 

    qtd_elementos += 2000     

    fim = time()    

  print('|---------------------------------------------------------------------|')


def calcula_tempo_ordenacao(lista):
  funcoes = ['selecao', 'mergesort', 'quicksort','sort_nativo'] 
  tempos = []

  for f in funcoes:
    tempos.append(timeit(f"{f}({lista})", setup=f"from  __main__ import {f}", number = 1))

  return tempos


def selecao(v):
  r = []
  while v:
    m = v[0]
    for num in v:
      if num < m: m = num     
    r.append(m)
    v.remove(m)
  return r




def mergesort(v):
    if len(v) <= 1: return v  
    else:
        m = len(v) // 2
        e = mergesort(v[:m])
        d = mergesort(v[m:])
        return merge(e, d)

def merge(e, d):
    r = []         
    i, j = 0, 0
    while i < len(e) and j < len(d):
        if e[i] <= d[j]:
            r.append(e[i])
            i += 1
        else:
            r.append(d[j])
            j += 1
    r += e[i:]
    r += d[j:]
    return r




def quicksort(v):
    if len(v) <= 1: 
      return v
    pivô = v[0] 
    iguais  = [x for x in v if x == pivô]
    menores = [x for x in v if x <  pivô]
    maiores = [x for x in v if x >  pivô]
    return quicksort(menores) + iguais + quicksort(maiores)



def sort_nativo(v):
  return v.sort()


def gera_lista(elementos):
  lista = list(range(1,elementos))
  shuffle(lista)
  return lista

def cabecalho():
    print()
    print('|-----------------------[EP1 - Ordenação]-----------------------------|')
    print('|     n      |              Time                                      |')
    print('|---------------------------------------------------------------------|')
    print('|            |   Selecao   Merge.   Quick.   Sort                     |')
    print('|---------------------------------------------------------------------|')




def imprime_resultados(qtd_elementos, lista_de_tempo):

  
  if len(str(qtd_elementos)) < 3 :
    
      print(f'| {qtd_elementos}|   {lista_de_tempo[0]:.2f}     {lista_de_tempo[1]:.2f}      {lista_de_tempo[2]:.2f}     {lista_de_tempo[3]:.2f}|')

      
  if len(str(qtd_elementos)) >= 3 : 
    
    
    
      if lista_de_tempo[0] < 10.0:
        print(f'|      {qtd_elementos}|   {lista_de_tempo[0]:.2f}     {lista_de_tempo[1]:.2f}      {lista_de_tempo[2]:.2f}     {lista_de_tempo[3]:.2f}|')

      elif lista_de_tempo[0] > 10.0:
        print(f'|      {qtd_elementos}|   {lista_de_tempo[0]:.2f}    {lista_de_tempo[1]:.2f}      {lista_de_tempo[2]:.2f}     {lista_de_tempo[3]:.2f}|')



principal()
