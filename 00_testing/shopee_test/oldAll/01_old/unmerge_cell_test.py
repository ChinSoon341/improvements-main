import pandas as pd
from openpyxl import load_workbook

# Load consolidated data
consolidated_data_path = r'C:\Users\chinsoont.BECKHOFF\Downloads\00_newsletter_case\testing_excels\trial\info01_t.xlsx'
consolidated_data = pd.read_excel(consolidated_data_path)

# Identify and handle merged cells in the "Company" column
merged_cells = []
for idx, value in enumerate(consolidated_data['Company']):
    if isinstance(value, str):
        if '\n' in value:  # Check for newline character indicating merged cell
            merged_cells.append(idx)

# Unmerge cells and fill data into both respective cells
for idx in merged_cells:
    company_values = consolidated_data.loc[idx, 'Company'].split('\n')
    consolidated_data.at[idx, 'Company'] = company_values[0]  # Update the original cell

    # Create a new row for each additional value in the merged cell
    for additional_value in company_values[1:]:
        new_row = consolidated_data.loc[idx].copy()
        new_row['Company'] = additional_value
        consolidated_data = pd.concat([consolidated_data, new_row.to_frame().transpose()], ignore_index=True)

# Save the modified consolidated data
consolidated_data.to_excel(r'C:\Users\chinsoont.BECKHOFF\Downloads\00_newsletter_case\testing_excels\trial\info01_t.xlsx', index=False)
