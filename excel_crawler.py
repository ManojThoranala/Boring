"""/*H******************************************************************************************************************
* FILENAME : excel_crawler.py
*
* DESCRIPTION : The script shows how excel file can be read and written, using Pandas, xlrd Libraries (creating tables, editing Data Frame, Writting Df to Excel or CSV file)
*
* NOTES :
*
* AUTHOR :    Manoj Thoranala Manjunatha        
*
*H*/"""

# implementation using pandas

import pandas as pd

xlsx_file = "path to the excel file"
workbook = pd.ExcelFile(xlsx_file)

************************************************** #
sheets = workbook.sheet_names                      # gives the list of sheet names present in the excel file
sheet = sheets[0]                                  # sheet 0 selected. else for loop can be used to select required sheet
dataframe = workbook.parse(sheet_name=sheet)       # creating the dataframe of the contents present in the sheet 0
************************************************** # alternatively to consoldate all the sheet in one data vrame use below snippet instead of above 3 lines of code
for sheet in workbook.sheet_names:
    sheets.append(workbook.parse(sheet))
dataframe = pd.concat(sheets, sort=False)          # dataframe now contains contents of all sheets in the excel file
***************************************************
# df.values gives the list in list type outputs i.e contents of dataframe in one level nested list (lists inside list)

for value in df.values:
    values = list(value)
    for ele in values:
        if str(ele) == 'nan':                 # to skip the "not a number - nan (float type)" values that are usually found in tables. 
            continue
***************************************************
# alternatively list comrehension can be used to remove "nan" the inside the list 
#import math ---------------- INclude this line at the import section of file if using the below snippet
#values = (value for value in values if math.isna(value))

# also dataframe functions for dropping the nan values can also be used.....refer doc - https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.dropna.html
***************************************************     

xlsx_write_path = "path for the output excel file"
writer = pd.ExcelWriter(xlsx_write_path, engine='xlsxwriter')

