'''
Demonstrate pandas data frame
'''

import pandas as pd

dataframe1 = pd.read_csv('/Users/beherb2/PycharmProjects/GenAi_Proj_1/resources/IMDBDataset.csv')

def toLowerCase(df):
    return df.str.lower()

def removeHtmlTags(text):
    pattern = ''

print(dataframe1.head(2))

print("\nData type of dataframe1.head(2) is : ",type(dataframe1.head(2)))

# print(dataframe1.head(2).apply(toLowerCase))
print(dataframe1.head(2).apply(toLowerCase))

# apply() method is not applicable for below as "dataframe1['review'][1]" returns String and not DataFrame
print("\nData type of dataframe1['review'][1] is : ",type(dataframe1['review'][1]))

print("\n2nd Review : ",dataframe1['review'][1])

print("\n2nd Review in lower case  : ",dataframe1['review'][1].lower())


