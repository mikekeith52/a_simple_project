
# the first two imports are common third-party libraries used by most data scientists and in most projects
import pandas as pd
import numpy as np

# I am treating the below import as if it were an internally developed module that is maintained by your org in one location but imported into most projects that the organization runs
from organization_internal_utils import db_connection as conn # this is an object that can be used to run sql queries

# below, I am importing a tuple of dates object from my config.py file. These dates will be reused in several locations but I am maintaining them and changing them in one location only
from config import dates

def get_data(query,conn):
	""" This function retrieves data from a database using a query and databaset connection.

	Args:
		query (str): The query to execute.
		conn (Connection): An object that can be used to run sql queries against the database you are wanting to retrieve data from.
	"""
	return pd.read_sql(query,conn)

def wrangle_data(data):
	""" This function cleans my data by pivotting it using a pandas pivot table.

	Args:
		data (DataFrame): The data to be wrangled.
	"""

	tbl = pd.pivot_table(
		data,
		index = 'col1', # the column values to place in the rows
		columns = ['col2','col3'], # the column values to place in the columns
		values = 'summed_numeric_col', # the column values to summarize
		aggfunc = 'sum', # the aggregating function to call
		margins = True, # whether or not you want a total column and row
		margins_name = 'Total', # what to call the total column and row
	)

	return df # returning this object means the results from our wrangling can then be passed to a subsequent function

def output_data(data,outpath):
	""" This function saves a dataframe to Excel in a given directory of the user's choosing.
	Usually, I use functions like these to save the results from several pulls/wranngling/pivots to several Excel

	Args:
		data (DataFrame): The data to save to Excel
		outpath (str): The path to save the data to. Absolute and relative directory paths both accepted.
	"""
	data.to_excel(outpath)

def main():
	query = open('query.sql').read() # reads the query.sql file in your directory as a string object
	modified_query = query.format(start = dates[0], end = dates[1]) # modifies the query by passing the start and end dates from config.py to the parts of the query that were curly bracketed in query.sql
	# I will use the query I wrote to get my data read into memory
	data = get_data(query = modfiied_query,conn = conn) # conn is imported on line 7 of this file
	# I use this function to clean/wrangle my raw dataset
	wrangled_data = wrangle_data(data=data)
	# I use this function to write the results as output_data_2024-01-01-2024-01-31.xlsx in the output directory
	output_data(data=wranged_data,outpath=f'./output/output_data_{dates[0]}-{dates[1]}.xlsx')

if __name__ == '__main__': # this line makes it so I only run this code when I want it run--it will not run if it is being imported into a separate directory
	main() # this line calls every function I wrote in the order I want them called