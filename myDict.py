#!/usr/bin/env python
# coding: utf-8

# # Name: Yichien Chou

# In[160]:


import numpy as np


# # Q1. Edit distance function

# In[161]:


def editDistance(str1, str2, deleteCost=1, defaultSubCost=2, subCostList={}): 
    
    #Convert into lowercase
    
    str1 = str(np.char.lower(str1))
    str2 = str(np.char.lower(str2))
    
    #Creating array (initialized with 0 of dimension of size of both strings)
    
    matrix = np.zeros((len(str1)+1,len(str2)+1))
    
    
    # Cross relation loop through each character of each string with each other and
    # fill the respective index of matrxi (row,column)
    
    for i in range(len(str1)+1): 
        for j in range(len(str2)+1): 
            
            #Only string 1 is empty
            if i == 0:  
                matrix[i][j] = j  
            #Only string 2 is empty
            elif j == 0: 
                matrix[i][j] = i
            #Both strings are empty
            elif i ==0 and j ==0:
                matrix[i][j] = np.zeros((i,j))
            else: 
                # Default cost of insertion/deletion=1 
                insercost = matrix[i][j-1] + deleteCost
                deletecot = matrix[i-1][j] + deleteCost
                if str1[i-1] != str2[j-1]:
                    if subCostList == {}:
                        #Default cost of substitution=2
                        subcost = matrix[i-1][j-1] + defaultSubCost
                    else:
                        if tuple(sorted([str1[i-1],str2[j-1]])) in subCostList:
                            subcost = matrix[i-1][j-1] + subCostList[tuple(sorted([str1[i-1],str2[j-1]]))]
                        else:
                            subcost = matrix[i-1][j-1] + defaultSubCost
                else:
                    subcost = matrix[i-1][j-1] + 0
                
                matrix[i][j] = min(insercost,  
                                   deletecot,        
                                   subcost)     
                                         
    
    return matrix[len(str1)][len(str2)]  # Returning the final


# # Q2. Search function

# In[164]:


class myDict:
    wordlist = []   
    
    def __init__(self, w): 
        self.wordlist = [x for x in w]  
        
    def print(self):         
        for x in self.wordlist:  
            print(x)      
    
    def search(self, str, maxDistance, deleteCost = 1, defaultSubCost = 2, subCostList = {}):
        result = []
        for x in self.wordlist:       
            temp = editDistance(str, x, deleteCost, defaultSubCost, subCostList)
            if temp <= maxDistance:
                result.append(x)
        result = sorted(result)
        return result

