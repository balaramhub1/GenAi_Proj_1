'''
Demonstrate data preprocessing, cleanup
- remove puntuation from text data

in the script, we are implementing the removal of punctuation via 2 methods
 - by excluding the punctuation in method via replace()
 - by using translate() method
'''
import pandas as pd
import string, time

exclude = string.punctuation

def removePunctuation1(text):
    for ch in exclude:
        text = text.replace(ch,'')
    return text

def removePunctuation2(text):
    return text.translate(str.maketrans('','',exclude))


dataframe1 = pd.read_csv('../resources/IMDBDataset.csv')
#print(dataframe1)
fiveRowData = dataframe1.head(5)

print(fiveRowData)
print()
print("Data before removal of punctuation..")
print("-"*50,"\n")
print(dataframe1['review'][3])
print("-"*50,"\n")
print("Data after removal of punctuation..")
print("-"*50,"\n")
print(removePunctuation1(dataframe1['review'][3]))
print("-"*50,"\n")

print("Data for review 19 : \n",dataframe1['review'][19])
print("Data after removal of punctuation..")
print("-"*50,"\n")
print(removePunctuation2(dataframe1['review'][19]))

