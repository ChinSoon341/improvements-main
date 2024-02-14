import pandas as pd
from openpyxl import load_workbook
from openpyxl.styles import Font

# Path to the input Excel file
input_excel_path = r'C:\Users\ADAM7\Desktop\Projects_demo\03_ocr\test.xlsx'

# Path to the output Excel file
output_excel_path = r'C:\Users\ADAM7\Desktop\Projects_demo\03_ocr\testtest.xlsx'

# Headers
headers = ["Lead Number", "Company", "Name", "Industry", "Interest", "Prepared by",
            "Category", "Product", "Etc"]

# Read the Excel file
data = pd.read_excel(input_excel_path, header=None)

# Assign headers to the DataFrame
data.columns = headers

# Save the DataFrame to a new Excel file with auto-adjusted column widths
with pd.ExcelWriter(output_excel_path, engine='openpyxl', mode='w') as writer:
    data.to_excel(writer, index=False)

    # Access the openpyxl workbook and worksheet objects
    workbook = writer.book
    worksheet = workbook.active

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

print(f"Data has been successfully read and saved with headers in {output_excel_path}.")
