# EECS 731 - Introduction to Data Science 
## Topic: To be, or not to be

###### Classy Shakespeare plays and players:

1. Set up a data science project structure in a new git repository in your GitHub account
2. Download the Shakespeare plays dataset from https://www.kaggle.com/kingburrito666/shakespeare-plays
3. Load the data set into panda data frames
4. Formulate one or two ideas on how feature engineering would help the data set to establish additional value using exploratory data analysis
5. Build one or more classification models to determine the player using the other columns as features
6. Document your process and results
7. Commit your notebook, source code, visualizations and other supporting files to the git repository in GitHub
_____________________________________________________________________________________________________________

- Shakespeare Plays Dataset was downloaded and Pandas dataframe was used to read the data, find under **_/data_**
Related Notebook - **_Shakespeare_Plays.ipynb_** under **_/notebooks_**

- Using Feature Engineering I could analyze the distribution of number of players corresponding to a particular Play: 
Relevant histogram report for sample play **_“Henry IV”_** is **_Player in Play.png_** under **_/reports_**

- Classification Model used - _Decision Tree_. All the process and details have been committed in the Jupyter Notebook **_“Classification Model_DecisionTrees.ipynb”_** under **_/notebooks_**. The Accuracy score is around 42%
