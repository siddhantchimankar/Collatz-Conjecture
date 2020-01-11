#!/usr/bin/env python
# coding: utf-8

# In[32]:


import numpy
import pandas as pd
import math
import random
from operator import truediv
import matplotlib.pyplot as plt
import matplotlib.pylab as pylab
import seaborn as sns

get_ipython().run_line_magic('matplotlib', 'inline')
from matplotlib import rcParams
rcParams['figure.figsize'] = 8,8
import warnings
warnings.filterwarnings('ignore')


# In[2]:


sequenceTree = []
def collatz(num):
    global sequenceTree
    
    if(num == 1):
        
        sequenceTree.append(num)
        seq = sequenceTree
        sequenceTree = []
        return seq
    
    if(num%2 == 0):
        sequenceTree.append(num)
        num = num/2
        
        return (collatz(num))
    else:
        sequenceTree.append(num)
        num = 3*num + 1
        
        return (collatz(num))
    
    
    
collatz(8)


# In[3]:


collatz(8)


# In[4]:



def lengthOfTrees(n,length=0):
    
    if(n == 1):
        length = length + 1
        return length
    
    if(n%2 == 0):
        n = n/2
        length = length + 1
        return (lengthOfTrees(n,length))
    else:
        n = 3*n + 1
        length = length + 1
        return (lengthOfTrees(n,length))
    
lengthOfTrees(9)


# In[5]:




def generateTrees(size, heightArray = []):
    heightArray = []
    for i in range(1,size+1):
        heightArray.append(lengthOfTrees(i))
        
    return heightArray
        

generateTrees(5)


# In[6]:


def index(n,indexArray = []):
    indexArray = []
    for i in range(1,n+1):
        indexArray.append(i)
    
    return indexArray
    
index(5)


# In[7]:


index(5)


# In[ ]:




    


# In[ ]:





# In[8]:


#count for how many numbers are greater than the number !
#count for how many numbers are smaller than the number !
#Ratio of the above two !
#largest number in the tree !
#Number of even and odd numbers in the tree !
#Number of primes in the Tree !
#Number of square numbers in the Tree !


# In[9]:


def greaterThan(n):
    count = 0
    greaterArray = []
    for i in range(1,n+1):
        for j in collatz(i):
            if(i < j):
                count = count + 1
        greaterArray.append(count)
        count = 0
    return greaterArray
    

greaterThan(10)


# In[10]:


def smallerThan(n):
    count = 0
    smallerArray = []
    for i in range(1,n+1):
        for j in collatz(i):
            if(i > j):
                count = count + 1
        smallerArray.append(count)
        count = 0
    return smallerArray
    

smallerThan(5)    


# In[11]:


def largestNum(n):
    num = 0
    largeArray = []
    for i in range(1,n+1):
        for j in collatz(i):
            if(j > num):
                num = j
        largeArray.append(num)
        num = 0
    return largeArray

type(largestNum(5)[0])


# In[12]:


def evenNums(n):
    num = 0
    evenArray = []
    for i in range(1,n+1):
        for j in collatz(i):
            if(j%2 == 0):
                num = num + 1
        evenArray.append(num)
        num = 0
    return evenArray

evenNums(5)
    


# In[13]:


def oddNums(n):
    num = 0
    oddArray = []
    for i in range(1,n+1):
        for j in collatz(i):
            if(j%2 == 1):
                num = num + 1
        oddArray.append(num)
        num = 0
    return oddArray

oddNums(5)


# In[14]:


def isPrime(n):
    t = 0
    if(n == 1):
        return False
    for i in range(2,math.ceil(math.sqrt(n+1))):
        if(n%i == 0 and n > 1):
            return False
    return True
        
isPrime(17)


# In[15]:


def primeNums(n):
    num = 0
    primeArray = []
    for i in range(1,n+1):
        for j in collatz(i):
            if(isPrime(j) == True):
                num = num + 1
        primeArray.append(num)
        num = 0
    return primeArray

primeNums(7)


# In[ ]:





# In[16]:


def isSquare(n):
    sqrt = math.sqrt(n)
    return (sqrt - int(sqrt)) == 0
isSquare(5)


# In[17]:


def squareNums(n):
    num = 0
    squareArray = []
    for i in range(1,n+1):
        for j in collatz(i):
            if(isSquare(j) == True):
                num = num + 1
        squareArray.append(num)
        num = 0
    return squareArray

squareNums(7)


# In[38]:


def parity(n):
    parityArray = []
    for i in range(1,n+1):
        if(i%2 == 0):
            parityArray.append('0')
        else:
            parityArray.append('1')
    return parityArray
parity(5)


# In[19]:


def prime(n):
    primeArray = []
    for i in range(1,n+1):
        if(isPrime(i) == True):
            primeArray.append(1)
        else:
            primeArray.append(0)
    return primeArray
prime(5)


# In[20]:


def square(n):
    squareArray = []
    for i in range(1,n+1):
        if(isSquare(i) == True):
            squareArray.append(1)
        else:
            squareArray.append(0)
    return squareArray
square(5)


# In[118]:


df = []
def createData(ran,a = [],b = []):
    a = index(ran)
    b = generateTrees(ran)
    c = greaterThan(ran)
    d = smallerThan(ran)
    e = map(truediv, b, a)
    f = largestNum(ran)
    g = evenNums(ran)
    h = oddNums(ran)
    i = primeNums(ran)
    j = squareNums(ran)
    k = parity(ran)
    l = prime(ran)
    m = square(ran)
    data = {'Number' : a, 'Height' : b, 'GreaterNums' : c, 'SmallerNums' : d, 'RatioOfGreater&Smaller' : e, 'LargestNum' : f, 'EvenNumbers' : g, 'OddNumbers' : h, 'PrimeNumbers' : i, 'SquareNumbers' : j, 'Parity' : k, 'Prime' : l, 'Square' : m}
    global df
    df = pd.DataFrame(data) 
    df.Parity = df.Parity.astype('category')
    df.Prime = df.Prime.astype('category')
    df.Square = df.Square.astype('category')

    return(df)


# In[119]:


createData(10000)


# In[ ]:


#Parity, Prime and Square are assigned 1 if they satisfy the title property otherwise 0


# In[520]:


f, axes = plt.subplots(2, 2, figsize=(12, 15))
sns.despine(left=True)

sns.set_style('whitegrid')
sns.barplot(data = df, x = df.Square, y = df.Height, hue = df.Parity, ax=axes[0, 0])

sns.set_style('whitegrid')
sns.barplot(data = df, x = df.Parity, y = df['LargestNum'], hue = df.Square, ax=axes[1, 0])

sns.set_style('whitegrid')
sns.barplot(data = df, x = df.Parity, y = df['RatioOfGreater&Smaller'], hue = df.Square, ax=axes[0,1])

sns.set_style('whitegrid')
sns.barplot(data = df, x = df.Parity, y = df.Height, hue = df.Prime, ax=axes[1, 1])

plt.show()


# In[521]:


#From this dashboard we can observe :
#In the first graph we clearly see that Odd parity generates higher Collatz sequence trees
#Also we find that non-Square numbers generate higher Collatz trees than Square numbers
#From graph 2 we see that Square numbers have a larger proportion of Greater numbers in their Collatz trees than Non-Square numbers.
#And also it shows that Odd numbers generate longer Collatz trees which is quite intuitive
#Next graph shows us strikingly that Odd numbers generate larger magnitudes of numbersin their trees which is again quite intuitive
#The last graph simply shows that Prime numbers gennerate longer trees compared to composite numbers


# In[467]:


f, axes = plt.subplots(1, 2, figsize=(15, 7))
sns.despine(left=True)

sns.set_style('whitegrid')
sns.distplot(a = df.Height, bins = 20, ax = axes[1])

sns.set_style('whitegrid')
sns.distplot(a = df['PrimeNumbers'], bins = 20, ax = axes[0])

plt.show()


# In[ ]:


#Both these distplots show the numbers of Prime numbers and Tree heights across the dataframe. It is surprising to see that they
#resemble each other in their form and shape and create this sort of camel-ish normal distribution


# In[371]:


sns.scatterplot(data = df, x = df.Number, y = df.Height, palette = 'seismic', hue = df.Prime, s = 10, linewidth = 0.25)
plt.show()


# In[ ]:


#Possibly the most important graph which depicts how the heights of the numbers in our dataframe look like according to the numbers.
#The colors show the distinguishment between Primes and composites and shows that primes are uniformly and randomly present between the numbers.


# In[469]:


sns.scatterplot(data = df, x = df.Height, y = df['RatioOfGreater&Smaller'], palette = 'seismic', hue = df.Parity)
plt.show()


# In[ ]:


#This scatterplot shows that around Heights = 100 and 0 the ratio of Greater Numbers in tree sequences is much higher than at around other heights


# In[500]:


sns.set_style('whitegrid')

sns.scatterplot(data = df, x = df.Number, y = df['LargestNum'], hue = df.Prime)
plt.show()


# In[ ]:


#This scatterplot demonstartes that most numbers have smaller values as their largest number in their tree sequences but as you move 
#further away to larger numbers some Largest Numbers can be very laarge as shown by the single point at the top right corner of this graph


# In[470]:


sns.scatterplot(data = df, x = df.PrimeNumbers, y = df['RatioOfGreater&Smaller'], palette = 'seismic', hue = df.Parity)
plt.show()


# In[ ]:


#This scatterplot shows that around Number of Prime Numbers in sequence tree = 25 the ratio of Greater Numbers in tree 
#sequences is much higher than at around other heights


# In[507]:


f, axes = plt.subplots(1, 2, figsize=(15, 7))
sns.despine(left=True)

sns.lineplot(data = df, x = df.PrimeNumbers, y = df['RatioOfGreater&Smaller'], palette = 'inferno_r', hue = df.Prime, ax = axes[0])

sns.lineplot(data = df, x = df.PrimeNumbers, y = df['RatioOfGreater&Smaller'], palette = 'inferno_r', hue = df.Square, ax = axes[1])

plt.show()


# In[ ]:


#Inference from lineplot 2 : Square numbers with 15-20 primes in their Collatz trees have the most Greater Numbers in their tree sequences


# In[509]:


f, axes = plt.subplots(1, 2, figsize=(15, 7))
sns.despine(left=True)

sns.lineplot(data = df, y = df.LargestNum, x = df.PrimeNumbers, palette = 'seismic', hue = df.Square, ax = axes[0])

sns.lineplot(data = df, y = df.LargestNum, x = df.PrimeNumbers, palette = 'seismic', hue = df.Parity, ax = axes[1])

plt.show()


# In[ ]:


#Inference from lineplot 1 : Square numbers with 30-40 primes in their Collatz trees have the Largest Numbers in their tree sequences
#Inference from lineplot 2 : Odd numbers with 20-40 primes in their Collatz trees have the Largest Numbers in their tree sequences


# In[510]:


sns.lineplot(data = df, x = df.Height, y = df.SquareNumbers, palette = 'seismic', hue = df.Square)
plt.show()


# In[ ]:


#Another striking lineplot which shows how Height of a Collatz tree correlates to the number of Square numbers present in it.
#It also shows that Square numbers generaate higher Collatz trees which is an established fact by now


# In[511]:


sns.kdeplot(df.Number, df.Height , cmap="Reds", shade=True, shade_lowest=False)
sns.kdeplot(df.Number, df.Height , cmap="Reds")

plt.show()


# In[ ]:


#Thsi is a heatmp showing the relationship between  number aand the height of the collatz tree that it generates


# In[512]:


sns.kdeplot(df.SquareNumbers, df.Height , cmap="Reds",height = 9, shade=True, shade_lowest=False)
sns.kdeplot(df.SquareNumbers, df.Height , cmap="copper",height = 9, shade=False, linewidth = 0.1)


plt.show()


# In[ ]:


#Very interesting heatmap that shows that certain number of Square Numbers in a collatz sequence affect the different heights of the sequence


# In[148]:


sns.set_style('whitegrid')
sns.jointplot(data = df, x = df.Height, y = df.PrimeNumbers, kind = 'hex',height = 9, space = 0, color="#4CB391")
plt.show()


# In[ ]:


#A hex-jointplot which correlates the heights of collatz trees with the number of Prime numbers in them. It is almost linear.


# In[29]:


for i in df['RatioOfGreater&Smaller']:
    if(i > 4):
        print(i)


# In[30]:


df[df['RatioOfGreater&Smaller'] > 4 ]


# In[522]:


#27 is the number which has the most unequal distribution of Greater numbers to smaller numbers in its sequence tree
#Let us look at its Collatz Tree

collatz(27)

#As we can see most of the numbers are very large with respect to 27. Most are 3 digit numbers and a few 4 digit numbers.
#It is cool to see that 27 being such a small number generates this effect whearas as the numbers get larger we see rapid
#decrease in this trend as the ratio falls fast towards 0. This can be explained by the fact that their are fewer and fewer
#prime numbers as we go up and this scarceness in prime numbers affects the ratio of the trees.


# In[517]:


sns.clustermap(df.corr(), cmap = 'summer', linewidth = 1, linecolor = 'black', figsize=(7,7))
plt.show()


# In[ ]:


#A final clustermap showing all the correlatiions between different parameters of the dataframe

