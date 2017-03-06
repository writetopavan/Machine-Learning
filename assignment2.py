import pandas as pd

# TODO: Load up the 'tutorial.csv' dataset
#
# .. your code here ..


csv_dataframe  = pd.read_csv('tutorial.csv', sep=',')
#xls_dataframe  = pd.read_excel("tq.xlsx", 'Sheet1', na_values=['NA', '?'])

# TODO: Print the results of the .describe() method
#
# .. your code here ..

#xls_dataframe.describe()
csv_dataframe.describe()
csv_dataframe.loc[2:4,'col3'] 

# TODO: Figure out which indexing method you need to
# use in order to index your dataframe with: [2:4,'col3']
# And print the results
#
# .. your code here ..

