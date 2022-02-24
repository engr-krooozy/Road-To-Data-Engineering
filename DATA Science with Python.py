
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[7]:


oneDArray = np.array([1, 2, 3, 4, 5])  #NumPy Arrays
print(oneDArray)


# In[8]:


print(oneDArray.ndim)   #No of dim of Numpy Arrays


# In[15]:


print(oneDArray[1])     #Indexing


# In[29]:


print(oneDArray.shape)    #Array Shape


# In[32]:


for i in oneDArray:     #iterate over OneD
    print (i)


# In[50]:


print(oneDArray + 2)   # * for multiplication / for float // for division ** for power


# In[9]:


twoDArray = np.array([[1, 2, 3], [4, 5, 6]])  #2-1, 1-2
print(twoDArray)


# In[10]:


print(twoDArray.ndim)    


# In[16]:


print(twoDArray[0 , 1])      


# In[17]:


print(twoDArray[0])


# In[30]:


print(twoDArray.shape)    #(no of dim, no of element)


# In[36]:


for i in twoDArray:         #Iterate over twoD
    for j in i:
        print(j)


# In[52]:


print(twoDArray.T)


# In[46]:


print(twoDArray + 2)


# In[12]:


threeDArray = np.array([[[1, 2, 3], [-1, -2, -3]], [[4, 5, 6], [-4, -5, -6]]])  #3-1, 1-2, 2-1, 1-3
print(threeDArray)


# In[14]:


print(threeDArray.ndim)


# In[21]:


print(threeDArray[1])


# In[26]:


print(threeDArray[0, 1])


# In[27]:


print(threeDArray[0, 1, 2])


# In[31]:


print(threeDArray.shape)


# In[37]:


for i in threeDArray:          #Iterate over threeD
    for j in i:
        for k in j:
            print(k)
    


# In[48]:


print(threeDArray + 2)


# In[53]:


print(threeDArray.T)


# In[43]:


zerosArray = np.zeros(10)  #Create an array with 10 zeros; works for zeros and ones
print(zerosArray)


# In[44]:


zerosArray = zerosArray.astype(int)  #Convert to int)
print(zerosArray)


# In[45]:


preFilledArray = np.full(10, 5)  #(Array size, value)
print(preFilledArray)


# In[56]:


matrix1 = np.array([[1,2,3], [4,5,6], [7,8,9]])        #Element-wise operation) No of col in first mat = no of rows in sec mat   
matrix2 = np.array([[10,11,12], [13,14,15], [16,17,18]])
print(matrix1)
print(matrix2)
print(matrix1 + matrix2)
print(matrix2 - matrix1)
print(matrix2 / matrix1)
print(matrix1 / matrix2)
print(matrix1 * matrix2)


# In[63]:


matmul= np.matmul(matrix1, matrix2)    #Matix Multiplication
print(matmul)


# In[68]:


np.min(matrix1)    #minimum value in a matrix


# In[69]:


np.max(matmul)    #max value in a matrix


# In[70]:


np.sum(matmul)  #sum of all values


# In[71]:


np.mean(matmul)  #mean of all value


# In[72]:


np.std(matrix1)  #standard deviation of all value


# In[74]:


np.median(matrix2)   #median of matrix 2

