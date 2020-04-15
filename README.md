# pands-project
##### Michael Alan Murphy-Quille
<br>
This repository contains the files **analysis.ipynb**, **analysis.html**, **analysis.py** and **summary.txt**.



## analysis.ipynb
This is the primary file of the project. It contains the report written in Jupyter Notebook along with the Python code written for the report and can be read directly from Github. Link:

[https://github.com/AlanQuille/pands-project/blob/master/analysis.ipynb](https://github.com/AlanQuille/pands-project/blob/master/analysis.ipynb)

**Note:** the table of contents (TOC) does not function from Github. Please open  **analysis.html** to read the project report which has a functioning TOC. Alternatively, one can use Jupyter Notebook to open **analysis.ipynb**.

## analysis.html
This is a html version of **analysis.ipynb**. It contains all the data (but not the functionality) from **analysis.ipynb**. Link:

[https://github.com/AlanQuille/pands-project/blob/master/analysis.html](https://github.com/AlanQuille/pands-project/blob/master/analysis.html)

## analysis.py
This is a Python file containing the data and the functionality from **analysis.ipynb**. This file is supplementary to **analysis.ipynb** and **analysis.html**, it is present to allow one to test how the code from **analysis.ipynb** generates the summary.txt file. This file is **not** the primary report file. Link:

[https://github.com/AlanQuille/pands-project/blob/master/analysis.py](https://github.com/AlanQuille/pands-project/blob/master/analysis.py)

## summary.txt
This contains data output from analysis.ipynb or analysis.py using the
**open**, **write** and **to_csv** functions (the latter from the **pandas** module). In particular, it contains:

1. Means for setosa, virginica and versicolor respectively
2. Medians for setosa, virginica and versicolor respectively
3. Percentage differences between medians and means for setosa, virginica and versicolor respectively.
4. Differences between means for versicolor/setosa, virginica/setosa and virginica/versicolor respectively.
5. Correlation matrices for setosa, virginica and versicolour respectively.




