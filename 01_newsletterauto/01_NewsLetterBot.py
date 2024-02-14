import pandas as pd
from openpyxl import load_workbook
from openpyxl.styles import Font

# Path to the master data Excel file
master_data_path = r'C:\Users\ADAM7\Desktop\Projects_demo\01_newsletter\master.xlsx'

# Load master_data dataframe
master_data = pd.read_excel(master_data_path)

# List of consolidated data files
consolidated_files = [
    r'C:\Users\ADAM7\Desktop\Projects_demo\01_newsletter\event1.xlsx',
    r'C:\Users\ADAM7\Desktop\Projects_demo\01_newsletter\event2.xlsx',  # Add the path to info02_t.xlsx
    # Add more paths if you have additional consolidated data files
]

# Create an empty DataFrame to store consolidated data
consolidated_data = pd.DataFrame()

# Loop through consolidated files and append data to consolidated_data
for file_path in consolidated_files:
    df = pd.read_excel(file_path)
    df = df.rename(columns={' Job title': 'Position'})
    df = df[['Company', 'Name', 'Position', 'Email', 'Phone']]
    
    # Add a single quote (`) to phone numbers that are not already formatted
    df['Phone'] = df['Phone'].apply(lambda x: f"'{x}" if isinstance(x, str) and not x.startswith("'") else x)
    
    consolidated_data = pd.concat([consolidated_data, df], ignore_index=True)

# Merge master_data and consolidated_data
merged_data = pd.concat([master_data, consolidated_data], ignore_index=True)

# Remove duplicates in the merged data
merged_data.drop_duplicates(subset=['Company', 'Name', 'Position', 'Email', 'Phone'], inplace=True)

# Save the merged_data dataframe to a new Excel file with formatting
output_excel_path = r'C:\Users\ADAM7\Desktop\Projects_demo\01_newsletter\output\Master_Newsletter_final.xlsx'

# Create a new Excel workbook
with pd.ExcelWriter(output_excel_path, engine='openpyxl', mode='w') as writer:
    merged_data.to_excel(writer, sheet_name='Sheet1', index=False)

    # Access the openpyxl workbook and worksheet objects
    workbook = writer.book
    worksheet = workbook['Sheet1']

    # Auto-adjust column width
    for column in worksheet.columns:
        max_length = 0
        column_letter = column[0].column_letter
        for cell in column:
            try:
                if len(str(cell.value)) > max_length:
                    max_length = len(str(cell.value))
            except:
                pass
        adjusted_width = (max_length + 2)
        worksheet.column_dimensions[column_letter].width = adjusted_width

    # Style the header row for better readability
    header_style = Font(bold=True)
    for cell in worksheet['1']:
        cell.font = header_style

print(f"Updated file saved as {output_excel_path}")
