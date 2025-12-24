import matplotlib.pyplot as plt
import pandas as pd

data1 = pd.read_csv('/Users/beherb2/PycharmProjects/GenAi_Proj_1/resources/IMDBDataset.csv')
print("Size/Shape of data : ",data1.shape)

print(data1.head())

# get only first 100 rows of data

data_100 = data1.head(100)

print("100 rows of data : ",data_100)

'''
Data preprocessing to be done like:

'''
# within the 100 rows of