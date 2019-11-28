import pandas as pd 

pd.DataFrame({'Yes':[50,21], 'No':[131,2]})

""" The pd.DataFram() constructor generates DataFrame objects  The syntax for declaring a new one is a dictionary whose keys are the column names.
A list of row labels used in a dataFrame is known as an index."""
pd.DataFrame({'Bob':['I liked it.','It was awful.'], 
            'Sue': ['Pretty good.','Bland.']},
            index=['Product A', 'Product B'])

"""A series is a sequence of data values. If a datafram is a table, a series is a list.  You can create one with just a list"""
pd.Series([1,2,3,4,5])
"""A series is a single column of a DataFrame.  You can assign column values to the series the same way as before using an index parameter. A series does not have a column name it only has one overal name."""
pd.Series([30,35,40], index=['2015 Sales', '2016 Sales', '2017 Sales'], name='Product A')
"""The series and the DataFrame are intimately related.  A DataFrame is like a bunch of Series 'glued together'"""


#Reading data files
