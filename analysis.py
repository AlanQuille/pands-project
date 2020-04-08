#!/usr/bin/env python
# coding: utf-8

# # Investigation of the Iris flower data set

# ## Table of contents
# 1. [Introduction](#introduction)
# 
# 2. [Questioning](#questioning)
# 
# 3. [Wrangling](#wrangling)
# 
#     3.1. [Import libraries](#31)
#     
#     3.2. [Read in Iris flower dataset from csv file](#33)
#     
# 4. [Exploration](#exploration)
#    
#     4.1 [Average values of attributes](#41)
#     
#     4.2 [Median values of attributes](#42)
#     
#     4.3 [Difference between medians and means](#43)
#     
#     4.4 [Shapiro-Wilk test for normality](#44)
#     
#     4.5 [Difference between means](#45)
#     
#     4.6 [Test for statistical significance ](#46)
#     
#     4.7 [Correlations between pairs of attributes](#47)
#     
#     4.8 [Summary.txt](#48)
#     
# 5. [Conclusions](#conclusions)
# 
# 6. [Bibliography](#bibliography)

# ## 1 Introduction <a name="introduction"></a>
# The purpose of this project is to analyse data describing variation in the structure of three species of Iris flowers. The dataset to be analysed is called the Iris flower data set.
# 
# The Iris Flower data set was introduced in 1936 in an article written by the statistician Ronald Fisher called "The Use of Multiple Measurements in Taxonomic problems. It is also called Anderson Iris Dataset after Edgar Anderson, the individual who collected the measurements of the flowers in the dataset. [1](#ref1)
# 
# The variation in the flowers is described by 4 attributes, namely sepal length, sepal width, petal length and petal width. The 3 species of flowers are setosa, versicolor and virginica. There are 50 data points for each species with 150 data points (or instances) in total. [2](#ref2)
# 
# It consists of 3 classes of 50 instances with 4 attributes, namely sepal and petal length and width. The 3 classes in question are species of iris flower and they are setosa, versicolor and viriginica. The attributes are length and width of the sepals and petals of the flowers. [3](#ref3)
# 
# The project will follow the standard data analytics procedure of questioning, wrangling, exploration and drawing conclusions. This report forms the final stage of this process (reporting).

# ## 2 Questioning <a name="questioning"></a>
# 
# In this analysis, the statistics of the attributes of the flowers will be studied to determine the relationships between them. In particular, these seven questions will be answered about the flowers:
# 
# 1. What are the average or mean values of the attributes for different species of Iris flower?
# 2. What are the median values of the attributes for different species of Iris flower?
# 3. Do they differ by a large margin? If so, what does that mean for the distributions of the attributes?
# 4. Are the attributes normally distributed?
# 5. What are the differences between average values of the attributes for different species of Iris Flower?
# 6. Are these differences statistically significant?
# 7. What is the correlation between the various attributes for different species of Iris flower?
# 
# To obtain the information, the data was first wrangled.

# ## 3 Wrangling <a name="wrangling"></a>
# The data is imported from the CSV file "iris.csv", obtained from the website. First, the appropriate libraries are imported to import and display the data:

# ### 3.1 Import libraries <a name="31"></a>

# In[1013]:


# Import pandas to import and display CSV data as dataframe
import pandas as pd
# Import and start seaborn to make plots look better
import seaborn as sns
sns.set()
# Import scipy library for tests for statistical significance
from scipy import stats
# Import pyplot for more plotting options
import matplotlib.pyplot as plt
# Import shapiro for Shapiro-Wilk test for normality
from scipy.stats import shapiro
# Import os for file removal
import os


# ### 3.2 Read in Iris flower dataset from csv file <a name="33"></a>
# 
# The data is then set as a Pandas dataframe called df. This dataframe has the attributes petal length, petal width, sepal length , sepal width and the species of each flower collected in the sample. The data is loaded into the dataframe in the following cell:

# In[1014]:


#df is the main dataframe that will be used.
df = pd.read_csv("iris.csv")
print(df)
print("\n")


# The first 5 entries of the dataframe are shown in the following cell:

# In[1015]:


print(df.head())
print("\n")


# The number of null, N/A or blank entries must be determined to see if data is missing:

# In[1016]:


#Find the null, blank or N/A entries and sum them.
print(df.isnull().sum())
print("\n")


# It can be seen that there are no null or blank entries so it can be assumed for this analysis that no data is missing.
# The exploration phase of the analysis is described in the next section.

# ## 4 Exploration <a name="exploration"></a>
# The data is summarised using the **pairplot** functtion from the **seaborn** module:

# In[1017]:


sns.pairplot(df, hue="species", markers=["o", "x", "D"])


# ... as can be seen from the graphs:
# 1. The distributions of the attributes for setosa, versicolor and virginica appear to approximate normal distributions. 
# 2. The average value for sepal length of virginica seems to be larger than for versicolor, which is larger than setosa.
# 3. The average value for sepal width of setosa seems to be larger than for versicolor, which is approximately equal to virginica.
# 4. The average value for the petal length and width of virginica seems to be larger than for versicolor, which is much larger than setosa.
# 5. All the attributes seem to be positively correlated to varying degrees for all species of flower. 
# 6. Setosa seems to have weak positive correlations between its attributes except for one pair (sepal width and sepal length).
# 
# In order to definitely answer the questions shown in section 2, more rigorous analysis must be conducted. In particular, the average values of the attributes of the specices of the flower are calculated in the next section.

# ### 4.1 Average values of attributes: <a name="41"></a>
# The average values of the different species of Iris flower are calculated using the **mean** function:

# #### Setosa

# In[1018]:


print(df[df['species']=='setosa'].mean())
print("\n")


# #### Virginica

# In[1019]:


print(df[df['species']=='virginica'].mean())
print("\n")


# #### Versicolour

# In[1020]:


print(df[df['species']=='versicolor'].mean())
print("\n")

# #### Output to files

# In[1021]:


# Output means to summary1.txt
with open("summary1.txt", 'w') as f:
    f.write("Means for setosa, virginica and versicolor respectively")
    f.write("\n")
    f.write("\n")


# In[1022]:


with open("summary1.txt", 'a') as f:
    f.write("\n")
    df[df['species']=='setosa'].mean().to_csv("summary1.txt", header=False, index=True, mode='a')

with open("summary1.txt", 'a') as f:
    f.write("\n")
    df[df['species']=='virginica'].mean().to_csv("summary1.txt", header=False, index=True, mode='a')

with open("summary1.txt", 'a') as f:
    f.write("\n")
    df[df['species']=='versicolor'].mean().to_csv("summary1.txt", header=False, index=True, mode='a')
    f.write("\n")


# Now the average values are calculated for each attribute for each species, the median and mode values can be calculated as follows:

# ### 4.2 Median values of attributes <a name="42"></a>

# The medians are calculated using the **median** function:

# #### Setosa

# In[1023]:


print(df[df['species']=='setosa'].median())
print("\n")


# #### Virginica

# In[1024]:


print(df[df['species']=='virginica'].median())
print("\n")


# #### Versicolour

# In[1025]:


print(df[df['species']=='versicolor'].median())
print("\n")


# #### Output to files

# In[1026]:


# Output medians to summary2.txt
with open("summary2.txt", 'w') as f:
    f.write("Medians for setosa, virginica and versicolor respectively")
    f.write("\n")
    f.write("\n")


# In[1027]:


with open("summary2.txt", 'a') as f:
    f.write("\n")
    df[df['species']=='setosa'].median().to_csv("summary2.txt", header=False, index=True, mode='a')

with open("summary2.txt", 'a') as f:
    f.write("\n")
    df[df['species']=='virginica'].median().to_csv("summary2.txt", header=False, index=True, mode='a')

with open("summary2.txt", 'a') as f:
    f.write("\n")
    df[df['species']=='versicolor'].median().to_csv("summary2.txt", header=False, index=True, mode='a')
    f.write("\n")


# ### 4.3 Difference between medians and means <a name="43"></a>

# The percentage difference between the means and the medians are calculated as follows:

# #### Setosa

# In[1028]:


diff1 = 100* (df[df['species']=='setosa'].mean() - df[df['species']=='setosa'].median())/(df[df['species']=='setosa'].mean())
print(diff1)


# #### Virginica

# In[1029]:


diff2 = 100* (df[df['species']=='virginica'].mean() - df[df['species']=='virginica'].median())/(df[df['species']=='virginica'].mean())
print(diff2)


# #### Versicolour

# In[1030]:


diff3 = 100* (df[df['species']=='versicolor'].mean() - df[df['species']=='versicolor'].median())/(df[df['species']=='versicolor'].mean())
print(diff3)


# #### Output to files

# In[1031]:


# Output differences between medians and means to summary3.txt
with open("summary3.txt", 'w') as f:
    f.write("Differences between medians and means for setosa, virginica and versicolor respectively.")
    f.write("\n")
    f.write("\n")


# In[1032]:


with open("summary3.txt", 'a') as f:
    f.write("\n")
    diff1.to_csv("summary3.txt", header=False, index=True, mode='a')

with open("summary3.txt", 'a') as f:
    f.write("\n")
    diff2.to_csv("summary3.txt", header=False, index=True, mode='a')

with open("summary3.txt", 'a') as f:
    f.write("\n")
    diff3.to_csv("summary3.txt", header=False, index=True, mode='a')
    f.write("\n")


# For most of the values, the difference between the mean and the median is small or neglible which indicates that the attributes  approximate the normal distribution (a perfect normal distribution would have the same value for mean and median). There is a -2% difference between the mean and median for versicolour and setosa petal length which indicates that the distribution is slightly left-skewed but still a good approximation to the normal distribution. For setosa petal width, there is an 18% difference between the mean and the median indicating a moderate skew to the right. This calls into question whether petal width for setosa is a good approximation to the normal distribution.
# 
# In order to rigorously test whether the attribute are normally distrbuted, the Shapiro-Wilk test is employed [4](#ref4)

# ### 4.4 Shapiro-Wilk test for normality <a name="44"></a>
# This test works by setting a cut-off value (in this case 0.05). The test is performed on the data. If the p-value extracted from the test exceeds alpha, then we cannot reject the null hypothesis that the sample approximates a normal or Gaussian distribution. Otherwise, we can safely reject the null hypothesis and say the distribution is not normal.
# The test is conducted for the attributes of all species of Iris flower by writing an appropriate function:

# In[1033]:


# Function to perform Shapiro-Wilk test for normality on attributes of flowers in data set
def shapiro_test(attribute, sp):
    alpha = 0.05
    data = df[df['species']==sp][attribute]
    stat, p = shapiro(data)
    print("test statistic: {}, p-value: {}".format(stat, p))
    if p > alpha:
        print("Null hypothesis is not rejected, sample approximates normal distribution")
    else:
        print("Null hypothesis is rejected, sample does not approximate normal distribution")
    print("\n")


# #### Setosa

# In[1034]:


shapiro_test("petal_length", "setosa")


# In[1035]:


shapiro_test("petal_width", "setosa")


# In[1036]:


shapiro_test("sepal_length", "setosa")


# In[1037]:


shapiro_test("sepal_width", "setosa")


# #### Virginica

# In[1038]:


shapiro_test("petal_length", "virginica")


# In[1039]:


shapiro_test("petal_width", "virginica")


# In[1040]:


shapiro_test("sepal_length", "virginica")


# In[1041]:


shapiro_test("sepal_width", "virginica")


# #### Versicolour

# In[1042]:


shapiro_test("petal_length", "versicolor")


# In[1043]:


shapiro_test("petal_width", "versicolor")


# In[1044]:


shapiro_test("sepal_length", "versicolor")


# In[1045]:


shapiro_test("sepal_width", "versicolor")


# All but two datasets pass the test of normality, which is expected by the shape of the distributions in the plots shown at the beginning of this section. The only two datasets that fail the test of normality are the versicolor petal widths and the setosa petal widths. The setosa petal widths had a relatively large difference between the mean and the median so it is expected that they would fail the test for normality. The difference between the mean and the median for versicolor petal width was only 2% however, so it is surprising that that distribution fails the test of normality when other datasets with larger differences passed.
# 
# It is also desirable to ascertain the difference between the means for each species of flower for each attribute. This is done in the following section.

# ### 4.5 Difference between means <a name="45"></a>
# The difference between the means are calculated with the **mean** function:

# In[1046]:


mnd1 = df[df['species']=='versicolor'].mean() - df[df['species']=='setosa'].mean() 
print(mnd1)


# In[1047]:


mnd2 = df[df['species']=='virginica'].mean() - df[df['species']=='setosa'].mean() 
print(mnd2) 


# In[1048]:


mnd3 = df[df['species']=='virginica'].mean() - df[df['species']=='versicolor'].mean() 
print(mnd3)


# #### Output to files

# In[1049]:


# Output differences between means to summary4.txt
with open("summary4.txt", 'w') as f:
    f.write("Differences between means for versicolor/setosa, virginica/setosa and virginica/versicolor respectively.")
    f.write("\n")
    f.write("\n")


# In[1050]:


with open("summary4.txt", 'a') as f:
    f.write("\n")
    mnd1.to_csv("summary4.txt", header=False, index=True, mode='a')

with open("summary4.txt", 'a') as f:
    f.write("\n")
    mnd2.to_csv("summary4.txt", header=False, index=True, mode='a')

with open("summary4.txt", 'a') as f:
    f.write("\n")
    mnd3.to_csv("summary4.txt", header=False, index=True, mode='a')
    f.write("\n")


# These results indicate that:
# 1. Versicolor has larger sepal length, petal length and petal width than setosa but smaller sepal width.
# 2. Virginica has larger sepal length, petal length and petal width than setosa but smaller sepal width
# 3. Virginica has larger sepal length, sepal width, petal length and petal width than versicolor.
# 
# It must be determined if these difference are statistically significant i.e. whether these differences are due to sampling error or reflect real differences in the means. This is done by performing an independant samples t-test and is done in the next section:

# ### 4.6 Test for statistical significance <a name="46"></a>
# The appropriate test for significance for the difference between means between two independant groups is the independant t-test [5](#ref5). In order to conduct the t-test, it is necessary that the variances are homogeneous and that the dependant variable is normally distrbuted within each group. This technically means that the test is not appropriate for versicolor petal widths and the setosa petal widths as it was previously shown that they fail the Shapiro-Wilk test for normality. However, the independant t-test is robust to moderate violations of normality and homogenity as long as:
# 
# 1. The sample sizes are the same. [6](#ref6)
# 2. The sample size of each group is greater than or equal to 30.
# 
# Each and every attribute has 50 data points for each species of Iris flower so both these conditions are met. Judging by the histograms at the beginning of section 4, the violations of normality for versicolor and setosa petal widths are small because the distributions physically resemble normal distributions. As such, the independant t-test will be conducted for every group.
# 
# The t-test produces test statistics and p-value. When the p-value is less than 0.05, than we can reject the null hypothesis that the means are equal. if it is greater than or equal to 0.05, than we cannot reject the null hypothesis that the means are the same.
# 
# The function to perform the test for two independant groups is defined as follows:

# In[1051]:


def ind_test(group1, group2):
     #Independant two sample t-test for difference between means of groups with difference variances
     print ("Independent two sample t-test for groups with different means: ")
     print (stats.ttest_ind(group1, group2, equal_var = False, nan_policy= 'omit'))
     #Degrees of freedom
     print ("Degrees of freedom: ")
     print (len(group1) + len(group2) - 1)


# For 3 independant groups, a one-way ANOVA table is generated. The code to generate the table is as follows:

# In[1052]:


def anova_table(group1, group2, group3):
    #One way AnoVA table
    print ("One way ANOVA table: ")
    print (stats.f_oneway(group1, group2, group3))
    #Degrees of freedom 1
    print ("Df1: ")
    print (len(group1)+len(group2)-1)
    #Degrees of freedom 2
    print ("Df2: ")
    print (len(group1) +len(group2)-2)
    print("\n")


# These tests are used to see if the difference between the means are statistically significant:

# In[1053]:


# create three dataframes for each species without the species column
df1 = df[df['species']=='virginica'].drop(columns=['species'])
df2 = df[df['species']=='setosa'].drop(columns=['species'])
df3 = df[df['species']=='versicolor'].drop(columns=['species'])
# Generate anova table for all 4 attributes at once
anova_table(df1, df2, df3)


# The results show that all the p-values are much less than 0.05. This means that the null hypothesis that the means are the same for all 4 attributes (petal length, petal width, sepal lengtha and sepal width) can be rejected.
# 
# Overall, several conclusions can be made from this report:

# ### 4.7 Correlations between pairs of attributes <a name="47"></a>
# To determine how correlated (or related) the attributes of the species of flower are, Pearson's correlation coefficient is calculated.[7](#ref7) 
# 
# The calculations of the correlation coefficients are given as follows:

# #### Setosa

# In[1054]:


corr1 = df[df['species']=='setosa'].corr(method="pearson")
print(corr1)
print("\n")


# #### Virginica

# In[1055]:


corr2 = df[df['species']=='virginica'].corr(method="pearson")
print(corr2)
print("\n")


# #### Versicolour

# In[1056]:


corr3 = df[df['species']=='versicolor'].corr(method="pearson")
print(corr3)
print("\n")


# #### Output to files

# In[1057]:


# Output correlation matrices to summary5.txt
with open("summary5.txt", 'w') as f:
    f.write("Correlation matrices for setosa, virginica and versicolour respectively.")
    f.write("\n")
    f.write("\n")


# In[1058]:


with open("summary5.txt", 'a') as f:
    f.write("\n")
    corr1.to_csv("summary5.txt", header=False, index=True, mode='a')

with open("summary5.txt", 'a') as f:
    f.write("\n")
    corr2.to_csv("summary5.txt", header=False, index=True, mode='a')

with open("summary5.txt", 'a') as f:
    f.write("\n")
    corr3.to_csv("summary5.txt", header=False, index=True, mode='a')
    f.write("\n")


# These results indicate that:
# 1. Setosa's attributes are all positively correlated, as are virginica and versicolour
# 2. Setosa Sepal width and sepal length are highly correlated (r>0.7) [8](#ref8)
# 3. All other attributes for setosa are weakly correlated (r<0.5)
# 4. Virginica petal length and sepal length are highly correlated.
# 5. Virginica petal width and sepal width are moderately correlated (0.5<r<0.7) 
# 6. All other attributes for virginica are weakly correlated.
# 7. Versicolour petal length and sepal length are highly correlated.
# 8. Versiscolour petal width and petal length are highly correlated.
# 9. All other attributes for versicolour are moderately correlated.

# ### 4.8 Summary.txt  <a name="48"></a>
# The summary files are combined into one file called "summary.txt" using the following method:

# In[1059]:


# This code takes each summary file and combines it into one file
# summary.txt

data_array = []

# This array opens the summary files and puts them
# in the array data_array
for i in range(1, 6):
    fin = open("summary" + str(i) +".txt", "r")
    data_array.append(fin.read())
    fin.close()
    # Delete superfluous summary files after 
    # data is extracted from them
    os.remove("summary" + str(i) +".txt")

# combined_data is all the data collected from
# the summary files.
combined_data = ""

# This adds up all the data 
# in data_array
for i in data_array:
    combined_data += i
    
# This outputs combined_data
# to summary_txt
fout = open("summary.txt", "w")
fout.write(combined_data)
fout.close()


# ## 5 Conclusions  <a name="conclusions"></a>
# The following conclusions can be made from the preceding data analysis:
# 
# 1. What the average or mean values are for each attribute for each species of flower.
# 2. What the median values are for each attribute for each species of flower.
# 3. The difference between the mean and the median values is mostly small or negligble except setosa petal width which has a moderate difference between its mean and median.
# 4. All but two of the attributes for each species is flower is normally distributed (the two datasets that fail the test for normality are versicolor petal widths and setosa petal widths)
# 5. What the difference between the means are for each species of flower.
# 6. The differences between the means are statistically significant and unlikely to be due to sampling error.
# 7. What the correlations are for each pair of attribute for each species of flower.
# 
# Further study can be done using machine learning. In particular, a classification algorithm such as decision trees can be used to predict the species of flower based on this dataset.

# ## 6 Bibliography <a name="bibliography"></a>

# [1] Bari, A. et al. Predictive Analytics For Dummies.. Wiley, 2016. <a name="ref1"></a>
# 
# [2] Nelli, F.. Python Data Analytics: Data Analysis and Science using pandas, matplotlib and the Python Programming Language.. Apress, 2015. <a name="ref2"></a>
# 
# [3] Archive.ics.uci.edu, http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data <a name="ref3"></a>
# 
# [4] Surhone, L.M. et al. Shapiro-Wilk Test.. VDM Publishing, 2010. <a name="ref4"></a>
# 
# [5] Urdan, T.C.. Statistics in Plain English.. Lawrence Erlbaum Associates, 2005. <a name="ref5"></a>
# 
# [6] Pagano, R.R.. Understanding Statistics in the Behavioral Sciences.., 339, Cengage Learning, 2012. <a name="ref6"></a>
# 
# [7] Boslaugh, S.. Statistics in a Nutshell.. O'Reilly Media, Incorporated, 2012. <a name="ref7"></a>
# 
# [8] Mukaka, M M. “Statistics corner: A guide to appropriate use of correlation coefficient in medical research.” Malawi medical journal : the journal of Medical Association of Malawi vol. 24,3 (2012): 69-71. <a name="ref8"></a>
