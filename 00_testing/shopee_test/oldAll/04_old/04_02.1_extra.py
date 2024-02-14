import pandas as pd

# Define the file path
file_path = r'C:\Users\chinsoont.BECKHOFF\Desktop\test\page1.xlsx'

# Read the Excel file
df = pd.read_excel(file_path)

# Remove columns 'Column_5' and 'Column_7' if they exist
df = df.drop(['Column_5', 'Column_7', 'Column_9', 'Column_15', 'Column_17', 'Column_19'], axis=1, errors='ignore')

# Keep only the first 14 columns
df = df.iloc[:, :14]

# Rename specific columns
column_rename_mapping = {
    'Column_1': 'Number',
    'Column_2': 'Tender Number',
    'Column_3': 'Status',
    'Column_4': 'Description',
    'Column_6': 'Agency',
    'Column_8': 'Published',
    'Column_10': 'Procurement Category',
    'Column_11': None,  # Removing Column_11
    'Column_12': 'Closed Date',
    'Column_13': 'Closed Time',
    'Column_14': None,  # Removing Column_14
    'Column_16': 'Awarded To',
    'Column_18': 'Award Value',
    'Column_20': 'Awarded Date'
}

# Remove and rename columns
df = df.drop(columns=[col for col, new_name in column_rename_mapping.items() if new_name is None])
df = df.rename(columns={col: new_name for col, new_name in column_rename_mapping.items() if new_name is not None})

# Define the new file path
excel_file_path = r'C:\Users\chinsoont.BECKHOFF\Desktop\test\page1.xlsx'

# Create a Pandas Excel writer using XlsxWriter as the engine.
with pd.ExcelWriter(excel_file_path, engine='xlsxwriter') as writer:
    df.to_excel(writer, sheet_name='Sheet1', index=False)

    # Get the xlsxwriter workbook and worksheet objects.
    workbook = writer.book
    worksheet = writer.sheets['Sheet1']

    # Add an Excel table and apply the autofilter.
    worksheet.add_table(0, 0, df.shape[0], df.shape[1] - 1, {'columns': [{'header': col} for col in df.columns]})
    
    # Autofit the column widths.
    for i, col in enumerate(df.columns):
        max_len = max(df[col].astype(str).apply(len).max(), len(col))
        worksheet.set_column(i, i, max_len)

print(f"Excel file saved at: {excel_file_path}")

