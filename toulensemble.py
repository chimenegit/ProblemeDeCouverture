#!/usr/bin/env python
# coding: utf-8

# In[13]:


import pandas as pd
import numpy as np
import operator
import copy
from pandas import DataFrame

data_file = "BMSVIEW1 (1).txt"
#data_file = "BMS2.txt"

# Delimiter

data_file_delimiter = '-1 '

largest_column_count = 0


with open(data_file, 'r') as temp_f:
   
    lines = temp_f.readlines()

    for l in lines:
        
        column_count = len(l.split(data_file_delimiter)) + 1

        
        largest_column_count = column_count if largest_column_count < column_count else largest_column_count


temp_f.close()


column_names = ['col'+ str(i) for i in range(0, largest_column_count)]


df = pd.read_csv(data_file, header=None, delimiter=data_file_delimiter, names=column_names, dtype=str)
df=df.fillna(0)

# LA TAILLE DE DONNEES CONSIDEREES

dh=df.loc[45001:50000]#head(5000)#
data=dh.values.tolist()

data_int=[]
for i in range(len(data)):
    data_int1=[]
    for j in range(len(data[i])): 
        data_int1.append(int(data[i][j]))
    data_int.append(data_int1)
    
def liste_de_set(liste):
    li_set=[]
    for i in liste:
        li_set.append(set(i))
    for ligne in li_set:
        for t in list(ligne):
            if 0 in ligne:
                ligne.remove(0)
    return(li_set)
dataseto=liste_de_set(data_int)

#print(data)
#print(dataseto)


# In[14]:


print(len(dataseto))


# In[12]:


# PARTITION HORIZONTALE

#dh=df.loc[2000:3000]


def get_unique_data(liste):
    T =set([])
    for s in liste:
        T.update(s)
    return T


#T=get_unique_data(dataseto)
#list_T=[]
#for i in T:
#    list_T.append(i)
    

def most_frequent(T_ignore, liste):
    #print("most_frequent")
    T_ignore_list=list(T_ignore) 
    #print("T_ignore_list:", T_ignore_list )
    dct = {i:0 for i in T_ignore_list}
    for item in T_ignore_list:
        if item !=0:
            for d in liste:
                dct[item]= dct[item]+list(d).count(item)
    #print(dct.items())
    a = max(dct.items(), key=operator.itemgetter(1))[0]
    return a


def partioned_D(D,a):
    D1_list, D2_list = [], []

    for d in D:
        if a in d:
            D1_list.append(d)
        else:
            D2_list.append(d)
    
    return D1_list, D2_list
                
#print(partioned_D(DI,a))


def Horpat(D, ignore):

    if len(D)<MAX_CLUSTER_SIZE: #Cette fonction compare si la taille du dataset D est inférieure à une constante N
        #print("horpat_if")
        return D
            
    else:
        T= get_unique_data(D)
        T_ignore= T.difference(ignore)
        #print(T_ignore)
        if len(T_ignore)==0:
            #print('horpat_elif')
            return D

        a= most_frequent(T_ignore, D)
        D1, D2=partioned_D(D,a)
        #print('horpat_else')
        return Horpat(D1, ignore.union(set([a]))), Horpat(D2, ignore)
    
# test de l'algorithme Horpat


     #return list_result


# LA MAXIMALE DE CLUSTER CONSIDEREE

MAX_CLUSTER_SIZE=20

ignore_set = set([])
#data=dh.values.tolist()

#print(len(dataseto))


#print(Horpat(dataseto, ignore_set))


#print(translate(Data_to_translate)) 


# In[ ]:


Data_to_translate= Horpat(dataseto, ignore_set)


# In[ ]:


def tup(Data):
    if isinstance(Data, tuple):
        if Datatransforme(Data[0]) not in l1:
            l1.append(Datatransforme(Data[0]))
        #ab = Datatransform(Data[0]
        #print(type(ab))
              
        if Datatransforme(Data[1]) not in l1:
            l1.append(Datatransforme(Data[1]))
            
    return l1
           
def Datatransforme(Data):
    if isinstance(Data, list):
        return Data
    else:
        return tup(Data)

l1 = []
l1 = tup(Data_to_translate)

l3=l1
print(len(l3))
#for i in l3:
    #print("IIIIIIII:",i)


a = 0
for i in range(len(l1)):
    #print("val :",i," ",len(l1[i]),"\n")
    a = len(l1[i]) + a


# In[ ]:

try:
    for i in range(len(l3)):
        if len(l3[i])==len(l3):
            l3.remove(l3[i])
    #print(l3)

except:
    print("Survenue de l'exception inutile")
finally:

      # In[ ]:


      a = 0
      for i in range(len(l3)):
          #print("val :",i," ",len(l3[i]),"\n")
          a = len(l3[i]) + a
      print(a)
      print(len(l3))


      # In[ ]:


      # PARTITION VERTICALE
      data_partition_horizontale=l3
      def ComptOccurrence2(liste):
          global sor
          liste2=[]   
          for i in liste:
              for j in i:
                  liste2.append(j)
          dct = {} 
          for item in liste2:
              dct[item] = dct.get(item,0) + 1
              sor=sorted(dct.items(), key=lambda x: x[1], reverse=True)
          return(sor)

      def parametrer (k, liste=[]):  

          res = ComptOccurrence2(liste)
          l = []
          for elt in res:
              if elt[1]< k:
                  l.append(elt[0])

          return(l)

      def RenvRestant (k, liste=[]):  
          res = ComptOccurrence2(liste)
          l = []
          for elt in res:
              if elt[1]>= k:
                  l.append(elt[0])

          return(l)
      def check_for_two(dataset, two_items):
          # two_items = {a,b}
          # pass
          list_of_set = [] # liste des ensemble: []
          for i in range(len(dataset)):
              list_of_set.append(set(dataset[i]))
          count = 0  
          for i in range(len(list_of_set)):
              one_set = list_of_set[i]
              if one_set.intersection(two_items) == two_items: # vérifie si la combinaison des 2 termes est dans l'enregistrement.
                  count += 1
          return count
      #print(check_for_two(liste, two_items))
      def is_kmAnonnym(Cset_to_test,liste=[]):
          # Les données de test
          data_set = copy.deepcopy(liste)
          var = len(Cset_to_test)
          if var == 1:
              return True
          elif var == 2:
              if check_for_two(data_set, Cset_to_test) >= k:
                  return  True
              else:
                  return False
          elif var >= 3:
              list_set_two_items = []
              ctest_list = list(Cset_to_test)
              for i in range(len(ctest_list) - 1):
                  for j in range(i+1, len(Cset_to_test)):
                      list_set_two_items.append(set([ctest_list[i], ctest_list[j]]))

              kassign = True

              #list_set_two_items = list(set_two_items)
              #print(list_set_two_items)
              #exit(0)
              for i in range(len(list_set_two_items)):

                  item = list_set_two_items[i]
                  if check_for_two(data_set,item)  >= k:
                      continue
                  else:
                      kassign = False
                      break
              if kassign:
                  return True
              else:
                  return False


      def dataframe_de(liste):
          for i in T:
              chunk= []
              for j in liste:
                  c= set(i).intersection(j)
                  chunk.append(list(c))
              return(pd.DataFrame(chunk))

      # On suppose que l'Algorithme de construction de Tremain effectué
      k=3
      cluster_list= []
      for liste in data_partition_horizontale:

              Tremain = RenvRestant (k, liste)
              #Tremain= Trem[1:len(Trem)]

              dict_of_classes = dict() # dictionnaire contenant les classes obtenues
              i = 0
              #dict_of_classes = dict()
              while len(Tremain) != 0:
                  Tcur_set = set([])
                  for i in range(len(Tremain)):
                      Ctest = set([])
                      Ctest = Ctest.union(Tcur_set)
                      Ctest = Ctest.union((set([Tremain[i]])))
                      # Algorithme de détermination de K pour un Ctest
                      #print(Ctest)
                      if is_kmAnonnym(Ctest, liste):
                          Tcur_set = Tcur_set.union(set([Tremain[i]]))
                  i = i+ 1
                  dict_of_classes[i] = Tcur_set
                  Tremain = list(set(Tremain).difference(Tcur_set))


              T = [] 
              for key, value in dict_of_classes.items():
                  T.append(list(value))

                  chunk_list= []
                  for i in T:

                      chunk= []
                      for j in liste:
                           c= set(i).intersection(j)
                           chunk.append(list(c))
                  #print(pd.DataFrame(chunk))
                      chunk_list.append(chunk)

              cluster_list.append(chunk_list)             
              #print(chunk_list)
              #print(T)
      #print(cluster_list)

                  #for i in Dataframe_liste1:
                  #Dataframe_liste=Dataframe_liste1.values.tolist()
                       #print(DataFrame_liste1.values.tolist())
               

      # RECUPERATION D'ELEMENT COUVERT

      #cluster_lister=[[[['s', 'p', 'r', 'u', 'q'], ['p', 'r'], ['s', 'p', 'r'], ['s', 'p', 'r', 'u', 'q'], ['s', 'p', 'r']], [[], [], ['v'], ['v'], []], [[], [], ['y'], [], ['y']], [[], ['w'], [], ['w'], []]], [[['u', 'v', 'w'], ['u', 'v', 'w']]]]
      #data= [[], [], [10307, 10315, 10295, 12667, 12671], [], [], [], [10307, 10315, 10295, 12667, 12671]]
      #data=[[12823, 18751, 12847, 10311], [10311], [12823, 18751, 12847, 10311], [10311], [10311], [10311], [10311]]
      #data=[['u', 'v', 'w'], ['u', 'v', 'w']]
      #data = [['s', 'p', 'r', 'u', 'q'], ['s', 'p', 'r'], ['s', 'p', 'r', 'u', 'q']]
      #data = [['s', 'p', 'r', 'u', 'q'], ['p', 'r'], ['s', 'p', 'r'], ['s', 'p', 'r', 'u', 'q'], ['s', 'p', 'r']]
      #data = [["a","b","c","d"],["a","b","c","d"],["a","b","c","d"],["a","b","c","d"],["a","b"]] 
      #data = [["a","b"],["a","b","c"],["a","b","c"],["a"],["b"]]
      #datas=[[83579, 83547, 83571], [83547, 83579, 83571], [83547, 83579], [83547, 83579], [83547, 83579], [83547, 83579], [83579, 83547, 83571]]

      #datas=[[222339, 55267, 55271, 55315, 55351, 55319], [55315, 55267], [55267, 55351, 55271], [55267, 55271, 55351], [55267, 55351], [55267, 55271], [55267, 55351, 55271], [55315, 55267, 55351], [55267], [55267, 55351], [222339, 55267, 55271, 55315, 55351, 55319], [55267], [55315, 55267, 222339, 55351], [55267, 55271], [55267, 55271]]
      #datas12=[[83579, 83547, 83571], [83579, 83547, 83571], [83547, 83579], [83547, 83579], [83547, 83579], [83547, 83579], [83579, 83547, 83571]]
      datas=[[[10311, 12487], [12487], [12479, 12483, 18619, 12487], [10311, 12487], [10311, 12487], [12487], [12483, 10311, 12487, 18619, 12479], [10311, 12487], [10311, 12487], [12487], [12479, 12483, 12487], [12479, 12483, 12487], [12479, 12483, 10311, 12487], [12483, 12487], [12487], [12479, 12483, 10311, 12487], [12483, 10311, 12487], [10311, 12487], [12483, 18619, 12487], [18619, 10311, 12487], [10311, 12487], [12487]], [[], [], [], [], [], [], [], [12547, 12567], [12567], [], [], [], [], [], [], [], [], [], [12547, 12567], [], [], []], [[], [], [], [10849, 12655], [], [], [], [10849, 12551, 12655, 12823, 12347, 10877, 12895], [10849, 12551, 12655, 12823, 12347, 10877, 12895], [], [12823], [], [], [], [], [], [12347, 10877], [12823], [], [], [], []], [[], [], [12555, 12715], [12715], [], [], [], [12555, 12715], [], [], [], [], [], [], [], [], [12715], [], [], [12715], [], []], [[], [], [], [12703, 12875, 10829, 10319, 12571, 12699, 10837, 10869, 12859, 10303], [], [], [], [12583, 12703, 12587, 12875, 10829, 12621, 12591, 10319, 12571, 12563, 12699, 10837, 10869, 10841, 12859, 10303], [], [], [12699, 12621, 12703], [], [], [], [], [], [12621, 10829, 10319, 10837, 10869, 10841, 10303], [12571, 12875, 12703], [], [12583, 12703, 12587, 12875, 10829, 12621, 12591, 10319, 12571, 12563, 12699, 10837, 10869, 10841, 12859, 10303], [12703, 10319], []], [[], [], [], [12679, 12799, 12827, 12575, 12323, 12835, 12839, 12711, 12847, 12719, 12851, 12471, 12475, 12735, 12863, 12867, 12739, 12743, 10833, 10323, 12883, 12887, 12759, 12763, 10339, 10853, 10343, 12647, 10857, 12651, 12779, 10861, 10865, 12659, 12667, 12671], [], [], [10861, 12759], [12679, 12799, 12827, 12575, 12323, 12835, 12839, 12711, 12847, 12719, 12851, 12471, 12475, 12735, 12863, 12867, 12739, 12743, 10833, 10323, 12883, 12887, 12759, 12763, 10339, 10853, 10343, 12647, 10857, 12651, 12779, 10861, 10865, 12659, 12667, 12671], [], [], [10865, 10857, 12867], [], [10323], [], [], [12659], [12323, 12711, 12719, 12735, 12739, 12743, 10833, 12759, 12763, 10853, 12647, 10857, 12651, 12779, 10861, 10865, 12659, 12667, 12671], [], [], [], [12679], []], [[], [], [], [], [], [], [], [10881, 12355, 12327, 12331, 12335, 12431, 12343, 10845, 12351], [], [], [], [], [], [], [], [], [10881, 12355, 12327, 12331, 12335, 12431, 12343, 10845, 12351], [], [], [], [], []], [[10307], [], [], [], [], [], [], [], [10307, 10295], [], [12683], [], [], [], [], [], [10307, 12683, 10295], [10307, 12683, 10295], [], [10295], [10307], []], [[], [], [], [], [10315, 12523], [], [], [], [10315, 12831, 12523], [], [], [], [], [], [], [], [], [], [], [10315, 12831, 12523], [10315], []], [[], [], [], [], [], [], [12491, 12663], [], [], [], [12491], [], [], [], [], [], [12491, 12663], [], [], [], [], []], [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [12687], [], [12687], [], []], [[], [], [], [], [], [], [], [], [12463, 12627, 12495], [], [], [12463], [], [], [], [], [12463, 12627, 12495], [], [], [], [], []], [[], [], [], [], [], [], [], [], [12695], [], [12695], [], [], [], [], [], [], [], [], [], [], []], [[], [], [], [], [], [], [18847], [], [], [], [], [], [], [], [], [], [], [], [], [18847], [], []], [[], [], [], [], [], [], [], [], [], [], [18787], [], [], [18787], [], [], [], [], [18787, 18723, 18735], [18787, 18723, 18735], [], []], [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [12643], [12643], [], [], [], [], []], [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [10299, 12451, 12731, 12771], [], [], [10299, 12451, 12731, 12771], [], []], [[], [], [], [], [], [], [18863], [], [], [], [], [18863], [], [], [], [], [], [], [], [], [], []], [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [12467], [], [], [], [], [12467]], [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [12403, 12411], [], [12403, 12411], [], [], [], [], []], [[], [], [12723], [], [], [], [], [], [], [], [], [], [], [], [], [], [12723], [], [], [], [], []], [[], [], [], [], [], [], [], [], [], [], [12607], [], [], [], [], [], [12607], [], [], [], [], []]]


      #data=[[85995], [85995]]

      def  ComptOccurrence(liste):


          liste2=[]   
          for i in liste:
              for j in i:
                  liste2.append(j)
          dct = {} 
          for item in liste2:

              dct[item] = dct.get(item,0) + 1
              #sor=sorted(dct.items(), key=lambda x: x[1], reverse=True)
          return  dct

      #Algo comptant le nombre d'enregistrements

      def  ComptListes(liste): 

          Dtrie=[]
          for i in liste:
              Dtrie.append(sorted(i))

          list_of_tuple = [] # liste des ensemble: []
          for i in Dtrie:
              list_of_tuple.append(tuple(i))

          dct = {} 
          for item in list_of_tuple:

              dct[item] = dct.get(item,0) + 1
          return dct 

      def RenvoiEnsCouvert(liste):

          d1 = ComptListes(liste)
          d2 = ComptOccurrence(liste)

          enscouv1=[]

          for i in d1.keys():
              for j in d2.keys():
                   if d1[i]== d2[j]:
                      if d2[j]==min(d2.values()):

                        if j in i:
                              if not i in enscouv1:  
                                  enscouv1.append(i)
          enscouv=[]
          for t in range(len(enscouv1)):
              for u in range (len(enscouv1[t])):
                  enscouv.append(enscouv1[t][u])

          return(enscouv)


      def RenvoiEltCouvert(liste):

          d1 = ComptListes(liste)
          d2 = ComptOccurrence(liste)

          eltcouv=[]
          for i in d1.keys():
              for j in d2.keys():
                  #print("i:",i,"j:",j)
                  if len(i)>= 2:
                      if d1[i]== d2[j]:
                          #print("i:",d1[i],"j:", d2[j])

                          if d2[j]==min(d2.values()):

                              if j in i:
                                  eltcouv.append(j)

          return(eltcouv)

      #Listes non couvert dont l'ajout d'un élément couvert ne forme pas un ens. couvert
      def ListNonCouv1(liste):  #Les listes différentes de la liste couverte

          enscouv=RenvoiEnsCouvert(liste)
          eltcouv=RenvoiEltCouvert(liste)

          e1=eltcouv[0:(len(eltcouv)//2)]
          e2=eltcouv[(len(eltcouv)//2):len(eltcouv)]

          ListNonCouv=[]
          for j in liste:

            if set(j)!= set(enscouv):
                      ListNonCouv.append(j)

          return(ListNonCouv)

      #print(RenvoiEltCouvert(datas12))

      # FONCTIONS D'AJOUT(ADCOV), IDGC, IDSA

      #datas12=[[222339, 55267, 55319], [222339, 55267, 55319], [55267, 222339], [55267], [55267]]
      #datas12=[[222339, 55267, 55319,83547], [222339, 55267, 55319,83547], [55267], [55267], [83547]]
      #datas12=[[83579, 83547, 83571,], [83547, 83579, 83571], [83547, 83579], [83547, 83579], [83547, 83579], [83547, 83579], [83579, 83547, 83571]]]
      #datas12=[[83579, 83547, 83571], [83579, 83547, 83571], [83547, 83579, 83571]]
      #datas12=[[83579, 83547, 83571], [83579, 83547, 83571]]
      #datas12=[[12739, 12771, 12775, 12715, 12747, 12779, 12751, 12723, 0, 12767], [12751, 0], [12751], [12751], [12747, 12723, 12751], [12751], [12751], [12751], [12739, 12771, 12775, 12715, 12747, 12779, 12751, 12723, 12727, 12767], [12739, 12771, 12775, 12715, 12747, 12779, 12751, 12723, 12727, 12767], [12751], [12751], [12751, 12723, 12775], [12751, 12739]]
      #datas12=[[12739, 12771, 12775, 12715, 12747, 12779, 12751, 12723, 0, 12767], [12751, 0], [12751], [12751], [12747, 12723, 12751], [12751], [12751], [12751], [12739, 12771, 12775, 12715, 12747, 12779, 12751, 12723, 12727, 12767], [12739, 12771, 12775, 12715, 12747, 12779, 12751, 12723, 12727, 12767], [12751], [12751], [12751, 12723, 12775], [12751, 12739]]
      datas12=[[0], [], [12747, 0, 12647], [12747, 12651, 12647], [], [], [], [], [], [], [], [], [], [], [], [12747, 12651, 12647], [], [12747]]

      def AjoutEltN(Disassociated_data): # Algo ajoutant l(es) élément(s) couvert(s) // fait avec ATTA

          liste=Disassociated_data
          enscouv=RenvoiEnsCouvert(liste)
          eltcouv=RenvoiEltCouvert(liste)

          e1=eltcouv[0:(len(eltcouv)//2)]
          e2=eltcouv[(len(eltcouv)//2):len(eltcouv)]
          ListNonCouv=ListNonCouv1(liste) 


          if len(eltcouv)==1:
              trouve=False
              for i in range(len(liste)):

                  if set(liste[i])!=set(enscouv):
                      tempList_i=copy.deepcopy(liste[i])
                      tempList_i.extend(eltcouv)
                      tempList=copy.deepcopy(liste)
                      tempList[i]=tempList_i
                      if set(tempList[i])!=set(enscouv):
                          Disassociated_data=tempList    
                          trouve=True
                          break
              if trouve==False:

                  Disassociated_data.append(eltcouv)

          if len(eltcouv)>=2:


                  if len(ListNonCouv)==0:
                      if set(eltcouv)!=set(enscouv):
                          liste.append(eltcouv)
                      else:

                               liste.append(e1)
                               liste.append(e2)

                  if len(ListNonCouv)==1:  
                      for i in range(0, len(liste)):
                          if set(liste[i])==set(ListNonCouv[0]):

                              liste[i].extend(e1)
                              liste.append(e2)

                  if len(ListNonCouv)>=2:
                      trouve2=False
                      for i in range(len(liste)):
                          if set(liste[i])!=set(enscouv):
                              tempList_2i=copy.deepcopy(liste[i])
                              tempList_2i.extend(eltcouv)
                              tempList2=copy.deepcopy(liste)
                              tempList2[i]=tempList_2i
                              if set(tempList2[i])!=set(enscouv):
                                  Disassociated_data=tempList2    
                                  trouve2=True
                                  break
                      if trouve2==False:
                          e1trouve= False
                          e2trouve= False
                          for i in range(0, len(liste)):
                              if set(liste[i])==set(ListNonCouv[0]):
                                  liste[i].extend(e1)
                                  e1trouve= True
                              elif set(liste[i])==set(ListNonCouv[1]):
                                  liste[i].extend(e2)
                                  e2trouve= True
                                  break

          return(Disassociated_data)



      #print(AjoutEltN(datas12))



      #import time

      def IDGC(cluster_li):
          #start_time = time.time()
          for cluster in cluster_li:
              for block in cluster:
                  RenvEltC=copy.deepcopy(RenvoiEltCouvert(block))
                  RenvoiEnsC=copy.deepcopy(RenvoiEnsCouvert(block))
                  if len(RenvEltC)!=0:
                      p=get_unique_data(block)
                      #print(p)
                      for i in range(0, len(block)):

                          if set(block[i])==set(RenvoiEnsC):
                              for j in range(len(block[i])):                        
                                  if block[i][j] in RenvEltC:
                                      bloc_ij=copy.deepcopy(block[i][j])
                                      bloc_ij= p #get_unique_data(bloc)
                                      block[i].extend(bloc_ij)
          #print("\n\nTemps d execution : %s secondes ---" % (time.time() - start_time))                       
          return(cluster_li)
      #print("\n\nTemps d execution : %s secondes ---" % (time.time() - start_time))      

      #print(IDGC(cluster_lis))
                                      #min(p) #"[", min(p), "-", max(p), "]"

      #print(p)

      # CODES DE IDSA

      #elements_de_I0
      #datas=[[['p', 'r', 'u', 's', 'q'], ['p', 'r'], ['p', 'r', 's'], ['p', 'r', 'u', 's', 'q'], ['p', 'r', 's']]]
      #datas1=[[['u', 'v', 'w'], ['u', 'v','w'], ['u', 'v'], ['u', 'v']]] 
      #datas=[[[18707, 10311], [12439, 18707, 10311, 12447], [12439, 18707, 10311, 12447]]]
      #datas=[[[12751], [12751, 12775], [12751, 12775]]]
      #datas=[[[], [], [], [], [], [12755, 12751], [], [], [], [], [12755, 12751], [], [], [], [], [], [], []]]
      #datas=[[[10315, 12895], [12487, 10315, 12895], [10315, 12895], [10315, 12895], [12487, 10315, 12895], [10315, 12895], [10315, 12895]]]
      #datas=[[[10311, 12487], [12487], [12479, 12483, 18619, 12487], [10311, 12487], [10311, 12487], [12487], [12483, 10311, 12487, 18619, 12479], [10311, 12487], [10311, 12487], [12487], [12479, 12483, 12487], [12479, 12483, 12487], [12479, 12483, 10311, 12487], [12483, 12487], [12487], [12479, 12483, 10311, 12487], [12483, 10311, 12487], [10311, 12487], [12483, 18619, 12487], [18619, 10311, 12487], [10311, 12487], [12487]], [[], [], [], [], [], [], [], [12547, 12567], [12567], [], [], [], [], [], [], [], [], [], [12547, 12567], [], [], []], [[], [], [], [10849, 12655], [], [], [], [10849, 12551, 12655, 12823, 12347, 10877, 12895], [10849, 12551, 12655, 12823, 12347, 10877, 12895], [], [12823], [], [], [], [], [], [12347, 10877], [12823], [], [], [], []], [[], [], [12555, 12715], [12715], [], [], [], [12555, 12715], [], [], [], [], [], [], [], [], [12715], [], [], [12715], [], []], [[], [], [], [12703, 12875, 10829, 10319, 12571, 12699, 10837, 10869, 12859, 10303], [], [], [], [12583, 12703, 12587, 12875, 10829, 12621, 12591, 10319, 12571, 12563, 12699, 10837, 10869, 10841, 12859, 10303], [], [], [12699, 12621, 12703], [], [], [], [], [], [12621, 10829, 10319, 10837, 10869, 10841, 10303], [12571, 12875, 12703], [], [12583, 12703, 12587, 12875, 10829, 12621, 12591, 10319, 12571, 12563, 12699, 10837, 10869, 10841, 12859, 10303], [12703, 10319], []], [[], [], [], [12679, 12799, 12827, 12575, 12323, 12835, 12839, 12711, 12847, 12719, 12851, 12471, 12475, 12735, 12863, 12867, 12739, 12743, 10833, 10323, 12883, 12887, 12759, 12763, 10339, 10853, 10343, 12647, 10857, 12651, 12779, 10861, 10865, 12659, 12667, 12671], [], [], [10861, 12759], [12679, 12799, 12827, 12575, 12323, 12835, 12839, 12711, 12847, 12719, 12851, 12471, 12475, 12735, 12863, 12867, 12739, 12743, 10833, 10323, 12883, 12887, 12759, 12763, 10339, 10853, 10343, 12647, 10857, 12651, 12779, 10861, 10865, 12659, 12667, 12671], [], [], [10865, 10857, 12867], [], [10323], [], [], [12659], [12323, 12711, 12719, 12735, 12739, 12743, 10833, 12759, 12763, 10853, 12647, 10857, 12651, 12779, 10861, 10865, 12659, 12667, 12671], [], [], [], [12679], []], [[], [], [], [], [], [], [], [10881, 12355, 12327, 12331, 12335, 12431, 12343, 10845, 12351], [], [], [], [], [], [], [], [], [10881, 12355, 12327, 12331, 12335, 12431, 12343, 10845, 12351], [], [], [], [], []], [[10307], [], [], [], [], [], [], [], [10307, 10295], [], [12683], [], [], [], [], [], [10307, 12683, 10295], [10307, 12683, 10295], [], [10295], [10307], []], [[], [], [], [], [10315, 12523], [], [], [], [10315, 12831, 12523], [], [], [], [], [], [], [], [], [], [], [10315, 12831, 12523], [10315], []], [[], [], [], [], [], [], [12491, 12663], [], [], [], [12491], [], [], [], [], [], [12491, 12663], [], [], [], [], []], [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [12687], [], [12687], [], []], [[], [], [], [], [], [], [], [], [12463, 12627, 12495], [], [], [12463], [], [], [], [], [12463, 12627, 12495], [], [], [], [], []], [[], [], [], [], [], [], [], [], [12695], [], [12695], [], [], [], [], [], [], [], [], [], [], []], [[], [], [], [], [], [], [18847], [], [], [], [], [], [], [], [], [], [], [], [], [18847], [], []], [[], [], [], [], [], [], [], [], [], [], [18787], [], [], [18787], [], [], [], [], [18787, 18723, 18735], [18787, 18723, 18735], [], []], [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [12643], [12643], [], [], [], [], []], [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [10299, 12451, 12731, 12771], [], [], [10299, 12451, 12731, 12771], [], []], [[], [], [], [], [], [], [18863], [], [], [], [], [18863], [], [], [], [], [], [], [], [], [], []], [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [12467], [], [], [], [], [12467]], [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [12403, 12411], [], [12403, 12411], [], [], [], [], []], [[], [], [12723], [], [], [], [], [], [], [], [], [], [], [], [], [], [12723], [], [], [], [], []], [[], [], [], [], [], [], [], [], [], [], [12607], [], [], [], [], [], [12607], [], [], [], [], []]]

      def Compt_list_couv(liste):
          enscouv= RenvoiEnsCouvert(liste)
          compt=0
          for i in liste:
              if i==enscouv:
                  compt=compt+1
          return(compt)

      # bloc est un ensemble d'éléments où un élément d'un ensemble de couverture est supprimé



      def IDSA3(Disassociated_data, k):  


          for z in range(0, len(Disassociated_data)):
              liste=Disassociated_data[z]
              enscouv=RenvoiEnsCouvert(liste)
              eltcouv=RenvoiEltCouvert(liste)
              Compt=Compt_list_couv(liste)

              #print(Disassociated_data[z])

              if len(eltcouv)!=0:
                  #print("eltcouv", eltcouv)

                  if Compt>k: 
                      trouve=False
                      for i in range(0, len(liste)):
                          if liste[i]==enscouv: 
                              for j in range(len(liste[i])):
                                  if liste[i][j]!= eltcouv[-1]:
                                      liste[i].remove(liste[i][j])
                                      trouve=True
                                      break
                          if trouve:
                              break
                  else:
                      for i in range(0, len(liste)):


                          if set(liste[i])==set(enscouv):


                              for j in range(len(liste[i])):
                                  #try:
                                      #print(liste[i])
                                      #print(i,j)
                                      #print("first:",liste[i][j])

                                  #except IndexError:
                                     # print("erreur")
                                  if liste[i][j]!=0 and liste[i][j]!= eltcouv[-1]:


                                      item_del = {'index_i':i, 'index_j':j, 'value':copy.deepcopy(liste[i][j])}
                                      #liste[i].remove(liste[i][j])
                                      liste[i][j]=0
                                      Sviolate=copy.deepcopy(eltcouv)
                                      #print("listei Apres Sviolate", liste[i])
                                      if len(Sviolate)!=0:
                                          #for k in Sviolate:
                                          #print("second:",liste[i][j])
                                          #print("liste:", liste)
                                          #return

                                          for l in range(0, len(liste)):
                                              if set(liste[l])!=set(enscouv):
                                                  ##is_Sviolate=True
                                                  for p in Sviolate:
                                                      if p not in liste[l]:
                                                         ## is_Sviolate=False
                                                        ##  break
                                                 ## if is_Sviolate:

                                                          temp_list_l=copy.deepcopy(liste[l])
                                                          temp_list_l.append(p)
                                                          temp_list=copy.deepcopy(liste)
                                                          temp_list[l]=temp_list_l
                                                          #print("temp_list[l]", temp_list, enscouv)
                                                          if set(temp_list[l])!=set(enscouv): #and is_kmAnonnym(temp_list, k):
                                                              Disassociated_data[z]=temp_list
                                                              #print("Disassociated", Disassociated_data[z])
                                                          break

                                          liste[item_del['index_i']][item_del['index_j']]= item_del['value']                                    
                              break    
          return(Disassociated_data)


      #datasFonction=IDSA3(datas, 3)



      # In[ ]:


      #APPEL DES FONCTIONS
      cluster_list_IDSA=copy.deepcopy(cluster_list)
      cluster_list_Ajout=copy.deepcopy(cluster_list)
      cluster_lis=copy.deepcopy(cluster_list)
      cluster_list_Disso=copy.deepcopy(cluster_list)

      IDGCl=IDGC(cluster_lis)
      import time
      start_time = time.time()
      AjoutEN=[]
      for cluster in cluster_list_Ajout:
          for bloc in cluster:
              start_time = time.time()
              AjoutEN.append(AjoutEltN(bloc))
      #print("\n\nTemps d execution : %s secondes ---" % (time.time() - start_time))

      AjoutI=[]
      #start_time = time.time()
      for cluster in cluster_list_IDSA:
          #for bloc in cluster:
              AjoutI_bloc=IDSA3(cluster, 3)
              AjoutI.append(AjoutI_bloc)
      #print("\n\nTemps d execution : %s secondes ---" % (time.time() - start_time))
      #print(AjoutI)


      #NOMBRE DE BLOCS COUVERTS ET LISTE DES TERMES AJOUT, IDGC, IDSA

      # In[ ]:


      # CODES POUR LE CALCUL DE FMI (AJOUT, IDGC, IDSA)

      #LISTE DES TERMES AJOUT, IDGC, IDSA

      list_de_clusterList=[]
      for i in cluster_list_Disso:
          for j in i:
              for k in j:
                  list_de_clusterList.append(k)
      print("I_disso:",len(list_de_clusterList))

      list_de_AjoutIList=[]
      for i in AjoutI:
          for j in i:
              for k in j:
                  list_de_AjoutIList.append(k)
      print("I_IDSA:",len(list_de_AjoutIList))
      
      
      list_de_IDGC=[]
      for u in IDGCl:
          for v in u:
              for x in v:
                  #print(x)
                  list_de_IDGC.append(x)
      print("I_IDGC:",len(list_de_IDGC))


      list_de_AjoutEList=[]
      for i in AjoutEN:
          for j in i:
                  list_de_AjoutEList.append(j)
      print("I_Ajout:",len(list_de_AjoutEList))


      # CODES POUR LE CALCUL DE RAE

      # Dissociation de base pour RAE
      liste3=[]   
      for p in range(len(list_de_clusterList)):
          for q in range(len(list_de_clusterList[p])):
              liste3.append(list_de_clusterList[p][q])
      List_Di=liste3

      list_coupDi=[]
      for e in range(len(List_Di) - 1):
          for f in range(e+1, len(List_Di)):
                      list_coupDi.append(set([List_Di[e], List_Di[f]]))
  
# RAE_Ajout
      liste4_jou=[]   
      for r in range(len(list_de_AjoutEList)):
          for s in range(len(list_de_AjoutEList[r])):
              liste4_jou.append(list_de_AjoutEList[r][s])
      List_datJou=liste4_jou

      list_coupledatJou=[]
      for n in range(len(List_datJou) - 1):
          for o in range(n+1, len(List_datJou)):
                      list_coupledatJou.append(set([List_datJou[n], List_datJou[o]]))

      Couple_Essai={10307, 10311}
      compteDi=list_coupDi.count(Couple_Essai)
      compteJou=list_coupledatJou.count(Couple_Essai)
      print(compteDi, compteJou)

      import statistics
      support=[compteDi,compteJou]
      moyenne=statistics.mean(support)
      re=abs(support[1]-support[0])/moyenne
      print("re_Ajout:",re)


      # RAE_IDSA

      liste4_IDSA=[]   
      for r in range(len(list_de_AjoutIList)):
          for s in range(len(list_de_AjoutIList[r])):
              liste4_IDSA.append(list_de_AjoutIList[r][s])
      List_datIDSA=liste4_IDSA

      list_coupledatIDSA=[]
      for n in range(len(List_datIDSA) - 1):
          for o in range(n+1, len(List_datIDSA)):
                      list_coupledatIDSA.append(set([List_datIDSA[n], List_datIDSA[o]]))


      Couple_Essai={10307, 10311}
      compteDi=list_coupDi.count(Couple_Essai)
      compteIDSA=list_coupledatIDSA.count(Couple_Essai)
      print(compteDi, compteIDSA)

      #import statistics
      support=[compteDi,compteIDSA]
      moyenne=statistics.mean(support)
      re=abs(support[1]-support[0])/moyenne
      print("re_IDSA:",re)
   
      # RAE_IDGC
      liste4=[]   
      for r in range(len(list_de_IDGC)):
          for s in range(len(list_de_IDGC[r])):
              liste4.append(list_de_IDGC[r][s])
      List_dat=liste4


      list_coupleIDGC=[]
      for n in range(len(List_dat) - 1):
          for o in range(n+1, len(List_dat)):
                      list_coupleIDGC.append(set([List_dat[n], List_dat[o]]))

      Couple_Essai={10307, 10311}
      compteDi=list_coupDi.count(Couple_Essai)
      compteIDGC=list_coupleIDGC.count(Couple_Essai)
      print(compteIDGC, compteDi)

      import statistics
      support=[compteDi,compteIDGC]
      moyenne=statistics.mean(support)
      re=abs(support[1]-support[0])/moyenne
      print("re_IDGC:",re)




      # In[ ]:




