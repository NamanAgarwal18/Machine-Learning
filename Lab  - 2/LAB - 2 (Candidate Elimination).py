# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 08:53:22 2021

@author: bmsce
"""

import csv

def createG():
    G = []
    for i in range(len(arr[1])-1):
        G.append("?")
    return G

arr = []

with open ("sample.csv",'r') as csvfile:
    for row in csv.reader(csvfile):
        arr.append(row)
    #print(arr[0][0])
    
S = []
G = []


for i in range(len(arr[1])-1):
    S.append("ϕ")
    
for i  in range(len(arr)):
    if arr[i][len(arr[1])-1] == "yes":
        for j in range(len(arr[1])-1):
            if S[j] == "?":
                continue
            elif S[j] == "ϕ":
                S[j] = arr[i][j]        
            elif arr[i][j] != S[j]:
                S[j] = "?"
                
for i  in range(len(arr)):
    if arr[i][len(arr[1])-1] == "no":
        for j in range(len(arr[1])-1):
            if S[j]!= arr[i][j] and S[j]!="?":
                temp = createG()
                temp[j] = S[j]
                G.append(temp)
            
    
#for i in range(1,len(arr)):
 #   for j in range(len(arr[1])-1):
  #      if S[j] == "?" or arr[i][len(arr[1])-1] == "no":
   #         continue
    #    elif ans[j] == "ϕ":
     #       ans[j] = arr[i][j]        
      #  elif arr[i][j] != ans[j]:
       #     ans[j] = "?"
    #print(S)

print("\n\n S: " , S)
print("\n\n G: " , G)

            