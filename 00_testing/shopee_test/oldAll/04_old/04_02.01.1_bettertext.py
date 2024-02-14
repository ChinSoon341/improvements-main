import pandas as pd

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
    # Specify the paths
    input_excel_path = r'C:\Users\chinsoont.BECKHOFF\Desktop\Gebiz_Tender_Reader\unused\results.xlsx'
    output_excel_path = r'C:\Users\chinsoont.BECKHOFF\Desktop\Gebiz_Tender_Reader\main\processed_results.xlsx'

    # Process the Excel file
    process_excel(input_excel_path, output_excel_path)

    print("Processing completed.")
