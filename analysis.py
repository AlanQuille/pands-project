import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
sns.set()

df = pd.read_csv("iris.txt")
print(df.head())

print(df.describe().to_csv("summary.txt", index=False))

attribute_list = list(df)[0:4]
print(attribute_list)

species_list = df['species'].unique()

def hist_output(attributes, dataframe):
    for i in attributes:
        temp_df = df[i]
         # This is to do a histogram for each
         # species, not necessary
       #  for sp in species_list:
        histogram = temp_df.hist()
        #plt.savefig(i + "_" + sp + "_" + "hist.png")
        plt.savefig(i + "_"  + "hist.png")
        plt.clf()

hist_output(attribute_list, df)

#plt.show()


