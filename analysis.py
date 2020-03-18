# this imports pandas module to load in 
# dataframes for quick and easy reading and writing
# to external files and doing statistics on the dataset
import pandas as pd
# this library is base on matplotlib and allows for
# creation of neat statistical graphics
import seaborn as sns
# matplotlib.pyplot library for plotting of histograms 
# in this script
import matplotlib.pyplot as plt

# This attaches a nice looking grid to matplotlib plots
sns.set()

# This reads in the Iris Flower data set from iris.txt
df = pd.read_csv("iris.txt")

# This outputs a summary of statistics for the Iris Flower data set to 
# a file called summary.txt. The data in the file is separated by commas
# as in a .csv file
print(df.describe().to_csv("summary.txt", index=False))

# This creates histograms of the columns in the Iris Flower data set
# (not separated by species)
df.hist()

# This saves the result as histograms.png
plt.savefig("histograms.png")

# This creates scatter plots and histograms of the columns in the data set
# and the data is clearly demarcated by species using the hue and 
# markers options
sns.pairplot(df, hue="species", markers=["o", "x", "D"])

# This saves the result as pairplot_species.png
plt.savefig("pairplot_species.png")

# This shows the histograms (not separated by species) as Figure 1 
# and the pairplot (histograms + scatter plots separated by species)
# is shown as Figure 2
plt.show()





