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
#     3.2. [Read in Iris flower dataset from csv file](#32)
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
#     4.8 [Output data to summary.txt](#48)
#     
# 5. [Conclusions](#conclusions)
# 
# 6. [Bibliography](#bibliography)

# ## 1 Introduction <a name="introduction"></a>
# The purpose of this project is to analyse data describing variation in the structure of three species of Iris flowers. The dataset to be analysed is called the Iris flower data set.
# 
# The Iris Flower data set was introduced in 1936 in an article written by the statistician Ronald Fisher called "The Use of Multiple Measurements in Taxonomic problems. It is also called Anderson Iris Dataset after Edgar Anderson, the individual who collected the measurements of the flowers in the dataset. [1](#ref1)
# 
# The variation in the flowers is described by 4 attributes, namely sepal length, sepal width, petal length and petal width. The 3 species of flowers are setosa, versicolor and virginica. The 3 species of flower make up the 3 classes of the data, consisting of 50 data points each. [2](#ref2) [3](#ref3)
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
# The data is imported from the CSV file "iris.csv", obtained from the website [3](#ref3). First, the appropriate libraries are imported to import and display the data:

# ### 3.1 Import libraries <a name="31"></a>

# In[264]:


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


# ### 3.2 Read in Iris flower dataset from csv file <a name="32"></a>
# 
# The data is then set as a Pandas dataframe called **df**. This dataframe has the attributes **petal length**, **petal width**, **sepal length**, **sepal width** and the **species** of each flower collected in the sample. The data is loaded into the dataframe in the following cell:

# In[265]:


# df is the main dataframe that will be used.
df = pd.read_csv("iris.csv")


# The first 5 entries of the dataframe are shown in the following cell:

# In[266]:


# 5 entries in dataframe to show.
df.head()


# The number of null, N/A or blank entries must be determined to see if data is missing:

# In[267]:


# Find the null, blank or N/A entries and sum them.
df.isnull().sum()


# It can be seen that there are no null or blank entries so it can be assumed for this analysis that no data is missing.
# 
# The exploration phase of the analysis is described in the next section.

# ## 4 Exploration <a name="exploration"></a>
# The data is summarised using the **pairplot** functtion from the **seaborn** module:

# In[268]:


sns.pairplot(df, hue="species", markers=["o", "x", "D"])


# ... as can be seen from the graphs:
# 1. The distributions of the attributes for setosa, versicolor and virginica appear to approximate normal distributions. 
# 2. The average value for sepal length of virginica seems to be larger than for versicolor, which is larger than setosa.
# 3. The average value for sepal width of setosa seems to be larger than for virginica, which is slightly larger than for versicolor.
# 4. The average value for the petal length and width of virginica seems to be larger than for versicolor, which is much larger than setosa.
# 5. All the attributes seem to be positively correlated to varying degrees for all species of flower. 
# 6. Setosa seems to have weak positive correlations between its attributes except for one pair (sepal width and sepal length).
# 
# In order to definitely answer the questions shown in section 2, more rigorous analysis must be conducted. In particular, the average values of the attributes of the specices of the flower are calculated in the next section.

# ### 4.1 Average values of attributes: <a name="41"></a>
# The average values of the different species of Iris flower are calculated using the **mean** function:

# #### Setosa

# In[269]:


mean1 = df[df['species']=='setosa'].mean()
mean1


# #### Virginica

# In[270]:


mean2 = df[df['species']=='virginica'].mean()
mean2


# #### Versicolour

# In[271]:


mean3 = df[df['species']=='versicolor'].mean()
mean3


# #### Output to files
# The **output** class is declared to output this data (and all subsequent summary statistics) to **summary.txt**.

# In[272]:


# Declare class which outputs to summary files
# It outputs to summaryX.txt, where X is a
# number which indicates the order in which
# the file was output and after
# 5 instances of the class has been created
# it outputs summary.txt
class output: 
    
    # string indicates filename in 
    # summaryX.txt
    sum_string = "summary"
    
    # counter is a class variable which
    # is incremented every time an 
    # instance of the class is created.
    counter = 0
    
    # Tracks how many appends to 
    # summaryX.txt have been made
    append_count = 0
    
    # This is the constructor. 
    # it creates the heading 
    # for the summaryX.txt file
    # or it deletes all files and
    # creates a summary.txt file
    def __init__(self, heading_str):
        
        # create summaryX.txt with heading when
        # counter is less than 5
        if(output.counter < 5):
            
            # Increment class variable counter
            output.counter += 1
            
            # Instance variable output_string is "summaryX.txt"
            self.output_string = self.sum_string + str(output.counter)
            
            # Output to summaryX.txt
            with open(self.output_string +".txt", 'w') as f:
                f.write(heading_str)
                f.write("\n")
                f.write("\n")
        
        # Delete summaryX.txt files and create
        # summary.txt if fifth instances of the 
        # class has been created
        else:
            self.delete_summaries()
            self.create_summary()
    
    # This appends value (which could be means, medians etc)
    # to the preexisting summaryX.txt file
    def append_open(self, value): 
        
        with open(self.output_string + ".txt", 'a') as f:
            
            # Using pandas to_csv function, append (mode = 'a') to summaryX.txt
            f.write("\n")
            value.to_csv(self.output_string + ".txt", header=False, index=True, mode='a')
            
            # Increment append_count which indicates
            # how many appends have been made for 
            # this instance of the class
            output.append_count += 1
            
            # Add newline if three appends has been made
            if(output.append_count ==3):
                f.write("\n")
                output.append_count = 0
             
    # This deletes summary
    def delete_summaries(self):
        
        # This array opens the summary files and puts them
        # in the array data_array
        self.data_array = []
        
        # For loop goes from 1 to 5, or 2 to 6 etc. depending
        # on what counter was set to initially (if it was 
        # set to 0, it goes from 1 to 5)
        for i in range(output.counter - 4, output.counter + 1):
            
            # Open summaryX.txt and add to data_array
            fin = open("summary" + str(i) +".txt", "r")
            self.data_array.append(fin.read())
            fin.close()
            
            # Delete superfluous summary files after 
            # data is extracted from them
            os.remove("summary" + str(i) +".txt")
            
    # This code takes each summary file and combines it into one file
    def create_summary(self):
        # This code takes each summary file and combines it into one file
        # summary.txt
        
        # combined_data is all the data collected from
        # the summary files.
        self.combined_data = ""

        # This adds up all the data 
        # in data_array
        for i in self.data_array:
            self.combined_data += i
    
        # This outputs combined_data
        # to summary_txt
        fout = open("summary.txt", "w")
        fout.write(self.combined_data)
        fout.close()


# In[273]:


# An instance of the class output is created to output to summary1.txt
first_output = output("Means for setosa, virginica and versicolor respectively")

# Append to summary1.txt
first_output.append_open(mean1)
first_output.append_open(mean2)
first_output.append_open(mean3)


# Now the average values are calculated for each attribute for each species, the median values are calculated as follows:

# ### 4.2 Median values of attributes <a name="42"></a>

# The medians are calculated using the **median** function:

# #### Setosa

# In[274]:


median1 = df[df['species']=='setosa'].median()
median1


# #### Virginica

# In[275]:


median2 = df[df['species']=='virginica'].median()
median2


# #### Versicolour

# In[276]:


median3 = df[df['species']=='versicolor'].median()
median3


# #### Output to files

# In[277]:


# An instance of the class output is created to output to summary2.txt
second_output = output("Medians for setosa, virginica and versicolor respectively")

# Append to summary2.txt
second_output.append_open(median1)
second_output.append_open(median2)
second_output.append_open(median3)


# ### 4.3 Difference between medians and means <a name="43"></a>

# The difference between the means and the medians expressed as a percentage of the mean are calculated as follows:

# #### Setosa

# In[278]:


diff1 = df[df['species']=='setosa'].mean() - df[df['species']=='setosa'].median()
mean1 = df[df['species']=='setosa'].mean()
diff1 = 100*diff1/mean1
diff1


# #### Virginica

# In[279]:


diff2 = df[df['species']=='virginica'].mean() - df[df['species']=='virginica'].median()
mean2 = df[df['species']=='virginica'].mean()
diff2 = 100*diff2/mean2
diff2


# #### Versicolour

# In[280]:


diff3 = df[df['species']=='versicolor'].mean() - df[df['species']=='versicolor'].median()
mean3 = df[df['species']=='versicolor'].mean()
diff3 = 100*diff3/mean3
diff3


# #### Output to files

# In[281]:


# An instance of the class output is created to output to summary3.txt
third_output = output("Percentage differences between medians and means for setosa, virginica and versicolor respectively.")

# Append to summary3.txt
third_output.append_open(diff1)
third_output.append_open(diff2)
third_output.append_open(diff3)


# For most of the values, the difference between the mean and the median is small or neglible which indicates that the attributes  approximate the normal distribution (a perfect normal distribution would have the same value for mean and median) [4](#ref4). There is a -2% and -2.5% difference between the mean and median for versicolour and setosa petal length respectively which indicates that the distribution is slightly left-skewed (mean<median, left-skew) but still a good approximation to the normal distribution. For setosa petal width, there is an 18% difference between the mean and the median indicating a moderate skew to the right (mean>median, right-skew). This calls into question whether petal width for setosa is a good approximation to the normal distribution.
# 
# In order to rigorously test whether the attribute are normally distrbuted, the Shapiro-Wilk test is employed [5](#ref5)

# ### 4.4 Shapiro-Wilk test for normality <a name="44"></a>
# This test works by setting a cut-off value called alpha (in this case alpha=0.05). The test is performed on the data. If the p-value extracted from the test exceeds alpha, then we cannot reject the null hypothesis that the sample approximates a normal distribution. Otherwise, we can safely reject the null hypothesis and say the distribution is not normal.
# The test is conducted for the attributes of all species of Iris flower by writing an appropriate function:

# In[282]:


# Function to perform Shapiro-Wilk test for normality on attributes of flowers in data set
def shapiro_test(attribute, sp):
    
    # Cut off value
    alpha = 0.05
    
    # the attribute and species to be tested
    data = df[df['species']==sp][attribute]
    
    # Test statistic and p-value
    stat, p = shapiro(data)
    
    # Output results to screen
    print("test statistic: {}, p-value: {}".format(stat, p))
    
    # If p-value exceeds cut-off value
    if p > alpha:
        print("Null hypothesis is not rejected, sample approximates normal distribution")
    else:
        print("Null hypothesis is rejected, sample does not approximate normal distribution")


# #### Setosa

# In[283]:


shapiro_test("petal_length", "setosa")


# In[284]:


shapiro_test("petal_width", "setosa")


# In[285]:


shapiro_test("sepal_length", "setosa")


# In[286]:


shapiro_test("sepal_width", "setosa")


# #### Virginica

# In[287]:


shapiro_test("petal_length", "virginica")


# In[288]:


shapiro_test("petal_width", "virginica")


# In[289]:


shapiro_test("sepal_length", "virginica")


# In[290]:


shapiro_test("sepal_width", "virginica")


# #### Versicolour

# In[291]:


shapiro_test("petal_length", "versicolor")


# In[292]:


shapiro_test("petal_width", "versicolor")


# In[293]:


shapiro_test("sepal_length", "versicolor")


# In[294]:


shapiro_test("sepal_width", "versicolor")


# All but two datasets pass the test of normality, which is expected by the shape of the distributions in the plots shown at the beginning of this section. The only two datasets that fail the test of normality are the versicolor petal widths and the setosa petal widths. The setosa petal widths had a relatively large difference between the mean and the median (18%) so it is expected that they would fail the test for normality. The difference between the mean and the median for versicolor petal width was only 2% however, so it is surprising that that distribution fails the test of normality when other datasets with larger differences passed.
# 
# The difference between the means for different species of flower is calculated in the next section.

# ### 4.5 Difference between means <a name="45"></a>
# The difference between the means are calculated with the **mean** function:

# #### Versicolour and Setosa

# In[295]:


mnd1 = df[df['species']=='versicolor'].mean() - df[df['species']=='setosa'].mean() 
mnd1


# #### Virginica and setosa

# In[296]:


mnd2 = df[df['species']=='virginica'].mean() - df[df['species']=='setosa'].mean() 
mnd2 


# #### Virginica and versicolor

# In[297]:


mnd3 = df[df['species']=='virginica'].mean() - df[df['species']=='versicolor'].mean() 
mnd3


# #### Output to files

# In[298]:


# An instance of the class output is created to output to summary4.txt
fourth_output = output("Differences between means for versicolor/setosa, virginica/setosa and virginica/versicolor respectively.")

# Append to summary4.txt
fourth_output.append_open(mnd1)
fourth_output.append_open(mnd2)
fourth_output.append_open(mnd3)


# These results indicate that:
# 1. Versicolor has larger sepal length, petal length and petal width than setosa but smaller sepal width.
# 2. Virginica has larger sepal length, petal length and petal width than setosa but smaller sepal width
# 3. Virginica has larger sepal length, sepal width, petal length and petal width than versicolor.
# 
# These results are congruent with the pairplots. It must be determined if these difference are statistically significant i.e. whether these differences are due to sampling error or reflect real differences in the means. This is done by performing an independant samples t-test and is done in the next section:

# ### 4.6 Test for statistical significance <a name="46"></a>
# The appropriate test for significance for the difference between means between two independant groups is the independant t-test [6](#ref6). In order to conduct the t-test, it is necessary that the variances are homogeneous and that the dependant variable is normally distrbuted within each group. This technically means that the test is not appropriate for versicolor petal widths and the setosa petal widths as it was previously shown that they fail the Shapiro-Wilk test for normality. However, the independant t-test is robust to moderate violations of normality and homogenity (i.e. the samples having different variances) as long as:
# 
# 1. The sample sizes are the same. [7](#ref7)
# 2. The sample size of each group is greater than or equal to 30.
# 3. If the variance of one group is not more than 4 times larger than the variance of the other group.
# 
# Each and every attribute has 50 data points for each species of Iris flower so conditions 1 and 2 are met. Condition three is tested as follows:

# In[299]:


# Get standard deviations of all attributes for every species of flower
set_std = df[df['species']=='setosa'].drop(columns=['species']).std()
virg_std = df[df['species']=='virginica'].drop(columns=['species']).std()
vers_std = df[df['species']=='versicolor'].drop(columns=['species']).std()

# Get variances of all attributes for every species of flower = std^2
set_var = set_std**2
virg_var = virg_std**2
vers_var = vers_std**2

# Divide one by another to see how many times the variance of one group is larger than another


# #### Versicolor and setosa

# In[300]:


vers_var/set_var


# #### Virginica and setosa

# In[301]:


virg_var/set_var


# #### Virginica and versicolor

# In[302]:


virg_var/vers_var


# ... as can be seen from the results, there are several violations of the third condition. The difference between the variances of virginica and setosa petal lengths are 10 times, the difference between the petal widths of same are 6.5 times. The differences between virginica and versicolor petal length variances are 10, the differences between petal width variances for same are 6.5 times. The variance difference for the petal lengths of versicolor and setosa are 7.3 times. However, the Welch's t-test (which is like the independant t-test but for unequal variances) can still be used. As before, if the p-value of the test is less than the cut-off value (in this case 0.05) then we can reject the null hypothesis that the means are the same. This is done as follows:

# In[303]:


def ind_test(group1, group2):
    
     # Independant two sample t-test for difference between means of groups
     print ("Independent two sample t-test for groups with different means: ")
    
     # equal_var = False means that the Welch's t-test is used for samples with unequal variances
     print (stats.ttest_ind(group1, group2, equal_var = False))
    
     # Degrees of freedom
     print ("Degrees of freedom: ")
    
     # Degrees of freedom = size of group 1 + size of group 2 - 1
     print (len(group1) + len(group2) - 1)


# These tests are used to see if the difference between the means are statistically significant:

# In[304]:


# create three dataframes for each species without the species column
df1 = df[df['species']=='virginica'].drop(columns=['species'])
df2 = df[df['species']=='setosa'].drop(columns=['species'])
df3 = df[df['species']=='versicolor'].drop(columns=['species'])
# Perform independant t-test for different species for each and every attribute


# #### Versicolour and Setosa

# In[305]:


ind_test(df3, df2)


# #### Virginica and setosa

# In[306]:


ind_test(df1, df2)


# #### Virginica and versicolor

# In[307]:


ind_test(df1, df3)


# The results show that all the p-values are much less than 0.05 for all differences between the means for virginica, setosa and versicolor. This means that the null hypothesis that the means are the same for all 4 attributes (petal length, petal width, sepal length and sepal width) can be safely rejected.

# ### 4.7 Correlations between pairs of attributes <a name="47"></a>
# To determine how correlated (or related) the attributes of the species of flower are, Pearson's correlation coefficient is calculated. [8](#ref8) 
# 
# The calculations of the correlation coefficients are given as follows:

# #### Setosa

# In[308]:


corr1 = df[df['species']=='setosa'].corr(method="pearson")
corr1


# #### Virginica

# In[309]:


corr2 = df[df['species']=='virginica'].corr(method="pearson")
corr2


# #### Versicolour

# In[310]:


corr3 = df[df['species']=='versicolor'].corr(method="pearson")
corr3


# #### Output to files

# In[311]:


# An instance of the class output is created to output to summary5.txt
fifth_output = output("Correlation matrices for setosa, virginica and versicolour respectively.")

# Append to summary5.txt
fifth_output.append_open(corr1)
fifth_output.append_open(corr2)
fifth_output.append_open(corr3)


# These results indicate that:
# 1. Setosa's attributes are all positively correlated, as are virginica and versicolour
# 2. Setosa Sepal width and sepal length are highly correlated (r>0.7) [9](#ref9)
# 3. All other attributes for setosa are weakly correlated (r<0.5)
# 4. Virginica petal length and sepal length are highly correlated.
# 5. Virginica petal width and sepal width are moderately correlated (0.5<r<0.7) 
# 6. All other attributes for virginica are weakly correlated.
# 7. Versicolour petal length and sepal length are highly correlated.
# 8. Versiscolour petal width and petal length are highly correlated.
# 9. All other attributes for versicolour are moderately correlated.

# ### 4.8 Output data to summary.txt  <a name="48"></a>
# The summary files are combined into one file called "summary.txt" using the following method:

# In[312]:


# This creates an instance of the output class but it is the fifth
# instance so it deletes all previous summaryX.txt files
# and combines the data into summary.txt.
# An empty string is passed as an argument
# to the constructor because it has to take
# a string as an argument but will do nothing with it
final_output = output("")


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
# [3] Archive.ics.uci.edu, http://archive.ics.uci.edu/ml/datasets/iris, last accessed 15/04/2020 <a name="ref3"></a>
# 
# [4] Administration, U.S.F.. Fire Data Analysis Handbook; Second Edition.. Fema, 2004 <a name="ref4"></a>
# 
# [5] Surhone, L.M. et al. Shapiro-Wilk Test.. VDM Publishing, 2010. <a name="ref5"></a>
# 
# [6] Urdan, T.C.. Statistics in Plain English.. Lawrence Erlbaum Associates, 2005. <a name="ref6"></a>
# 
# [7] Pagano, R.R.. Understanding Statistics in the Behavioral Sciences.., 339, Cengage Learning, 2012. <a name="ref7"></a>
# 
# [8] Boslaugh, S.. Statistics in a Nutshell.. O'Reilly Media, Incorporated, 2012. <a name="ref8"></a>
# 
# [9] Mukaka, M M. “Statistics corner: A guide to appropriate use of correlation coefficient in medical research.” Malawi medical journal : the journal of Medical Association of Malawi vol. 24,3 (2012): 69-71. <a name="ref9"></a>
