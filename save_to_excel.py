from openpyxl import load_workbook
from openpyxl.styles import Alignment

file_path = 'Leads New.xlsx'
workbook = load_workbook(filename=file_path)

worksheet = workbook.active

contacts = [['Adilson', 'Ana Paula', 'Ester Baos Irmã', 'Joãozinho', 'Jorginho', 'Mexicano'],
            ['5517991411223', '5511944645774', '12028204210', '558781714750', '819017531983', '5519988923626']]

first_empty_row = worksheet.max_row + 2

center_alignment = Alignment(horizontal='center', vertical='center')

for i in range(len(contacts[0])):
    name_cell = worksheet.cell(row=first_empty_row + i, column=1, value=contacts[0][i])
    phone_cell = worksheet.cell(row=first_empty_row + i, column=2, value=contacts[1][i])
    name_cell.alignment = center_alignment
    phone_cell.alignment = center_alignment

# Save the updated workbook
workbook.save(filename=file_path)

print("Data appended and saved successfully!")
