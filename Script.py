
import pandas as pd

# Load the Excel files
file1 = pd.read_excel('C:\Users\ananda\Downloads\VW_NPS_SEPTTIREPROMO_EM_T2_prod_091924')
file2 = pd.read_excel('C:\Users\ananda\Downloads\VW_NPS_SEPTTIREPROMO_EM_T2_prod_092024')
file3 = pd.read_excel('C:\Users\ananda\Downloads\VW_NPS_SEPTTIREPROMO_EM_T2_prod_092324')

# Concatenate the DataFrames
combined = pd.concat([file1, file2, file3], ignore_index=True)

# Save the combined DataFrame to a new Excel file
combined.to_excel('C:\Users\ananda\Downloads\VW_NPS_SEPTTIREPROMO_EM.csv', index=False)
