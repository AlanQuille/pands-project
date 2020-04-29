# pands-project
##### Michael Alan Murphy-Quille
<br>
This repository contains the files analysis.ipynb, iris.csv, analysis.html, and summary.txt.

The read the report for this project, please open **analysis.html**. 

## analysis.ipynb
This is the primary file of the project. It contains the report written in Jupyter Notebook along with the Python code written for the report and can be read directly from Github. Link:

[https://github.com/AlanQuille/pands-project/blob/master/analysis.ipynb](https://github.com/AlanQuille/pands-project/blob/master/analysis.ipynb)

**Note:** the table of contents (TOC) does not function from Github. Please open  **analysis.html** to read the project report with a functioning TOC. Alternatively, one can use Jupyter Notebook to open **analysis.ipynb**.

Also, if Jupyter Notebook is used to run the code in this file, use Run All (or Run All Below from the very top of the file), otherwise the instances of the class **output** might not function correctly.

## analysis.html
This is a HTML version of **analysis.ipynb**. It contains all the data (but not the functionality) from **analysis.ipynb**. Link:

[https://github.com/AlanQuille/pands-project/blob/master/analysis.html](https://github.com/AlanQuille/pands-project/blob/master/analysis.html)

## summary.txt
This contains data output from analysis.ipynb using the class **output**, which uses the 
**open**, **write** and **to_csv** functions (the latter from the **pandas** module). In particular, it contains:

1. Means for setosa, virginica and versicolor respectively
2. Medians for setosa, virginica and versicolor respectively
3. Percentage differences between medians and means for setosa, virginica and versicolor respectively.
4. Differences between means for versicolor/setosa, virginica/setosa and virginica/versicolor respectively.
5. Correlation matrices for setosa, virginica and versicolour respectively.

## iris.csv
This contains the data for the Iris flower dataset. The reference for this data is present in the report (**analysis.ipynb** or **analysis.html**)

