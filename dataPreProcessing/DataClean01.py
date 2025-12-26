import matplotlib.pyplot as plt
import pandas as pd
import re

data1 = pd.read_csv('../resources/IMDBDataset.csv')
print("Size/Shape of data : ",data1.shape)

print(data1.head())

# get only first 100 rows of data

data_100 = data1.head(10)

print("100 rows of data : ",data_100)

# Prints the 4th sentiment value
print(data1['sentiment'][3])


# Prints the 2nd review
print("Second row data is : \n",data1['review'][1])

# The 2nd row review contains html tags, and upper case letters.
# need to do preprocessing to remove these
'''
Data preprocessing to be done like:
- removal of html tags, emojis.
- converting data to lower case
- removing urls
'''

data2nd_row = data1['review'][1]

print("Data in lower case is :\n",data2nd_row.lower())

def removeHtmlTags(text):
    htmlTagPattern = r'<.*?>'
    result = re.sub(htmlTagPattern,'',text)
    return result

print("Data without html tags :\n")
print(removeHtmlTags(data2nd_row))

# Use apply function to apply a function on input string
print("Before removing html tags : ",data1['review'][17])
# data1['review'][17] = data1['review'][17].apply(removeHtmlTags)

# Remove all html tags from reviews
dataRow1 = data1['review'].apply(removeHtmlTags)

print("After removing html tags : ",dataRow1.head(10).str.lower())


