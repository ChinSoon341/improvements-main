import re
import pandas as pd

def extract_tenders(text):
    tenders = re.split(r'\n(?=\d+\n)', text)[1:]
    tenders = [re.split(r'\n', tender.strip()) for tender in tenders[:10]]
    return tenders

file_path = r'C:\Users\chinsoont.BECKHOFF\Desktop\test\page1.txt'
with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read()

tenders_info = extract_tenders(content)
max_columns = max(len(tender) for tender in tenders_info)

columns = [f'Column_{i+1}' for i in range(max_columns)]
df = pd.DataFrame(tenders_info, columns=columns)

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
