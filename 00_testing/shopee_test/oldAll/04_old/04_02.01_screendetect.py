import pandas as pd
import re

# File paths
input_excel_path = r'C:\Users\ADAM7\Desktop\Projects_demo\04_gebizReport\results.xlsx' #repla
output_excel_path_multiple_sup = r'C:\Users\ADAM7\Desktop\Projects_demo\04_gebizReport\temp\exc\f_mulSup.xlsx'
output_excel_path_awarded_to = r'C:\Users\ADAM7\Desktop\Projects_demo\04_gebizReport\temp\exc\f_inVal_to.xlsx'

# Read the Excel file
df = pd.read_excel(input_excel_path)

# Filter rows where "Awarded To" column contains "Multiple Suppliers" or "Awarded to"
filtered_df = df[df['Awarded To'].str.lower().isin(['multiple suppliers', 'awarded to'])].copy()  # Copy the subset to avoid SettingWithCopyWarning

# Extract numbers from the "Tender Number" column using regular expressions
filtered_df['Extracted Tender Numbers'] = filtered_df['Tender Number'].apply(lambda x: re.search(r'\b(\w+\d+)\b', str(x)).group(1) if pd.notnull(x) else '')

# Create separate columns for "Multiple Suppliers" and "Awarded To"
filtered_df['Multiple Suppliers Flag'] = filtered_df['Awarded To'].str.lower() == 'multiple suppliers'
filtered_df['Awarded To Flag'] = filtered_df['Awarded To'].str.lower() == 'awarded to'

# Sort the DataFrame by "Awarded To" and "Multiple Suppliers" columns
sorted_df = filtered_df.sort_values(by=['Awarded To Flag', 'Multiple Suppliers Flag'])

# Create DataFrames for "Multiple Suppliers" and "Awarded To"
output_df_multiple_sup = pd.DataFrame({
    'Multiple Suppliers': sorted_df[sorted_df['Multiple Suppliers Flag']]['Extracted Tender Numbers']
})
output_df_awarded_to = pd.DataFrame({
    'Awarded To': sorted_df[sorted_df['Awarded To Flag']]['Extracted Tender Numbers']
})

# Write the output DataFrames to Excel files
output_df_multiple_sup.to_excel(output_excel_path_multiple_sup, index=False)
output_df_awarded_to.to_excel(output_excel_path_awarded_to, index=False)

print("Extraction complete. Data saved to:", output_excel_path_multiple_sup, "and", output_excel_path_awarded_to)
