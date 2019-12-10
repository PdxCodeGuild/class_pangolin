import pandas as pd 
import os

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
"""The pd.read_csv() function has over 30 optional parameters you can specify.  """
filename = "Players.csv"
nba_players = pd.read_csv(os.path.join(os.path.dirname(os.path.abspath(__file__)),filename))
# nba_players.shape
"""The .shape method on a pd object shows how large the Dataframe is.  It returns a tuple, with the first number being the number of rows and the second being the number of columns."""

print(nba_players.head())
"""The .head method on a pd object returns the first five rows and prints them in a table. """

"""To make pandas use the first column for the index instead of creating a new, you can specify with index_col"""

# nba_players = pd.read_csv(os.path.join(os.path.dirname(os.path.abspath(__file__)),filename), index_col=0)
# print(nba_players.head())


'''In pandas you can find columns of a DataFrame by calling the columns title in a square bracket, or with a period.  You can like these up with a following bracket for the index value to get a specific piece of data. '''
# print(nba_players['Player'])
# print(nba_players['Player'][420])

''' pandas indexing works in two ways.  The first is index-based selection. Selecting data based on its numerical position in the data.  '''

# print(nba_players.iloc[3921])
'''Both loc and iloc are row first, column second, which is different from native python.   '''

# print(nba_players.iloc[1766:1781, 1])
'''the list takes in a value for the row first, and a column second.  Each of these values can be a range by using a colon as above.  Above we are taking the first column of rows1 1776 to 1781.'''


''' negative numbers can also be passed, this starts by going from the bottom up, like a negative index in a list. '''

# print(nba_players.iloc[-1,-1])

'''The second paradigm for attribute selectio is the one followed by the loc operator : Label-Based selection.  In this paradigm its the data index value, not its position which matters.  '''

print(nba_players.loc[1, 'birth_state'])

'''iloc is conceptually simpler that loc because it ignores the datasets indices.  When we use iloc we treat the dataset like a big matrix. Though, loc can be used advantageously because you can call the value of the rows' column.'''
print(nba_players.loc[:3,['Player','born','college']])
'''fuck this example, look into .reindex() because .loc() messes with the value of a index if not all labels are present or something.