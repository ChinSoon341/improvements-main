import re
import pandas as pd
import os

def extract_tenders(text):
    tenders = re.split(r'\n(?=\d+\n)', text)[1:]
    tenders = [re.split(r'\n', tender.strip()) for tender in tenders[:10]]
    return tenders

# Path to the folder containing page files (page1.txt, page2.txt, ..., page10.txt)
folder_path = r'C:\Users\ADAM7\Desktop\Projects_demo\04_gebizReport\temp'

# Initialize an empty list to store DataFrames for each page
dfs = []

# Loop through pages 1 to 10
for page_num in range(1, 11):
    # Construct the file path for each page
    file_path = os.path.join(folder_path, f'p{page_num}.txt')

    # Read the content of the page
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Extract tenders information
    tenders_info = extract_tenders(content)
    max_columns = max(len(tender) for tender in tenders_info)

    # Create DataFrame for the current page
    columns = [f'Column_{i+1}' for i in range(max_columns)]
    df = pd.DataFrame(tenders_info, columns=columns)

    # Remove specific columns and rename others
    column_rename_mapping = {
        'Column_1': 'Number',
        'Column_2': 'Tender Number',
        'Column_3': 'Status',
        'Column_4': 'Description',
        'Column_6': 'Agency',
        'Column_8': 'Published',
        'Column_10': 'Procurement Category',
        'Column_12': 'Closed Date',
        'Column_13': 'Closed Time',
        'Column_16': 'Awarded To',
        'Column_18': 'Award Value',
        'Column_20': 'Awarded Date'
    }

    # Remove and rename columns
    df = df[column_rename_mapping.keys()].rename(columns=column_rename_mapping)

    # Append the DataFrame to the list
    dfs.append(df)

# Concatenate all DataFrames into a single DataFrame
final_df = pd.concat(dfs, ignore_index=True)

# Define the new file path for the final Excel file
excel_file_path = r'C:\Users\ADAM7\Desktop\Projects_demo\04_gebizReport\temp\exc\r1_main.xlsx'

# Create a Pandas Excel writer using XlsxWriter as the engine.
with pd.ExcelWriter(excel_file_path, engine='xlsxwriter') as writer:
    final_df.to_excel(writer, sheet_name='Sheet1', index=False)

    # Get the xlsxwriter workbook and worksheet objects.
    workbook = writer.book
    worksheet = writer.sheets['Sheet1']

    # Add an Excel table and apply the autofilter.
    worksheet.add_table(0, 0, final_df.shape[0], final_df.shape[1] - 1, {'columns': [{'header': col} for col in final_df.columns]})

    # Autofit the column widths.
    for i, col in enumerate(final_df.columns):
        max_len = max(final_df[col].astype(str).apply(len).max(), len(col))
        worksheet.set_column(i, i, max_len)

#2. flag multiple supplier or invalid inputs

output_excel_path_multiple_sup = r'C:\Users\ADAM7\Desktop\Projects_demo\04_gebizReport\temp\exc\flags\f_mulSup.xlsx'
output_excel_path_awarded_to = r'C:\Users\ADAM7\Desktop\Projects_demo\04_gebizReport\temp\exc\flags\f_inVal_to.xlsx'

# Read the Excel file
df = pd.read_excel(excel_file_path)

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


print(f"Excel file saved at: {excel_file_path}")


#3. remove all the entries in the main r1_main.xlsx
def process_excel(input_path, output_path):
    # Read the Excel file
    df = pd.read_excel(input_path)

    # Rearrange columns
    columns_order = ['Tender Number', 'Description', 'Agency', 'Published', 'Procurement Category', 'Awarded To', 'Award Value', 'Awarded Date']
    df = df[columns_order]

    # Remove rows with "Awarded to" or "Multiple Suppliers" in the "Awarded To" column
    df = df[~df['Awarded To'].str.contains('Awarded to|Multiple Suppliers', case=False, na=False)]

    # Save the processed DataFrame to a new Excel file
    df.to_excel(output_path, index=False)

if __name__ == "__main__":

    output_excel_path = r'C:\Users\ADAM7\Desktop\Projects_demo\04_gebizReport\temp\exc\r1_main_removed.xlsx'

    # Process the Excel file
    process_excel(excel_file_path, output_excel_path)
    
    print("Processing completed.")
