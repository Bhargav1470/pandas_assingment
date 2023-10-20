import pandas as pd
import numpy as np

columns_to_consider=['Timeperiod', 'Reporting_Year', 'Contribution_Type', 'Contribution_Subtype', 'Tactic', 'SubTactic',
 'Brand','Sub-Brand', 'Campaign_Name', 'Campaign_Start_Date', 'Campaign_End_Date', 'Quarter', 'Unit_Size',
 '_06s', '_15s', '_30s', '_60s', 'Reair', 'Tactical_Media_Target', 'Broad_Target', 'Driver', 'Insignificant',
 'LBS','Direct LBS', 'Halo LBS', 'Impressions', 'Profit_Per_LBS', 'GSV_Per_LBS', 'Production_Costs',
 'Media_Costs','Total_Spend', 'Margin_Dollars', 'GSV_Dollars', 'Trade_Subsidization_Rate', 'FSI_Face_Value',
 'FSI_Shared_vs_Solo', 'FSI_Unit_requirement', 'Equity or Innovation', 'Category', 'Shopper Retailer',
 'Shopper Event', 'Tent Pole Event', 'Channel', 'SM Classification', 'Line Lookup', 'Model',
 'Tent Pole Execution', 'Shopper Execution']

df = pd.read_excel("/home/sigmoid/Downloads/sample.xlsx",sheet_name="Master_Dataset",usecols=columns_to_consider)


selected_columns1 = ['_15s', '_30s','_60s', 'Driver', 'LBS', 'Direct LBS', 'Halo LBS', 'Impressions','Profit_Per_LBS', 'GSV_Per_LBS','Production_Costs', 'Media_Costs', 'Total_Spend', 'Margin_Dollars', 'GSV_Dollars', 'Line Lookup']
cols_float= df[selected_columns1]
cols_float=cols_float.apply(pd.to_numeric, errors='coerce')
print(cols_float.dtypes)

selected_columns2 =['_06s','Timeperiod', 'Reporting_Year', 'Contribution_Type', 'Contribution_Subtype', 'Tactic', 'SubTactic',
 'Brand','Sub-Brand', 'Campaign_Name', 'Quarter', 'Unit_Size', 'Reair', 'Tactical_Media_Target','Broad_Target', 'Insignificant','Direct LBS', 'Trade_Subsidization_Rate', 'FSI_Face_Value',
 'FSI_Shared_vs_Solo', 'FSI_Unit_requirement', 'Equity or Innovation', 'Category', 'Shopper Retailer',
 'Shopper Event', 'Tent Pole Event', 'Channel', 'SM Classification', 'Model','Tent Pole Execution', 'Shopper Execution']
cols_string= df[selected_columns2]
cols_string=cols_string.astype(str)
print(cols_string.dtypes)

selected_columns3 =['Campaign_Start_Date', 'Campaign_End_Date']
cols_date= df[selected_columns3]
cols_date= cols_date.apply(pd.to_datetime , errors='coerce')
print(cols_date.dtypes)




############################## Task 2 ####################################

df['Insignificant'] = df['Insignificant'].replace(['x', np.nan],['Y','N'])

# print(df['Insignificant'])
df['Tent Pole Execution'] = df['Tent Pole Execution'].replace(['X', np.nan],['Y','N'])


df[selected_columns1]=df[selected_columns1].fillna(0)
# print(df[selected_columns1])

df[selected_columns2]=df[selected_columns2].fillna('')
print(df[selected_columns2])

df.to_csv('output.csv', index=False)
