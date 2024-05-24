import pandas as pd
from openpyxl import load_workbook

contacts = {
    'nome': ['Adilson', 'Ana Paula', 'Ester Baos Irmã', 'Joãozinho', 'Jorginho', 'Mexicano'],
    'phone': ['5517991411223', '5511944645774', '12028204210', '558781714750', '819017531983', '5519988923626']
}

new_contacts = pd.DataFrame(contacts)

file_path = 'Pasta.xlsx'

# leads = pd.read_excel(file_path, sheet_name='Planilha1', engine='openpyxl')
# writer = pd.ExcelWriter('Pasta.xlsx', engine='openpyxl')
# startrow = leads.index[-1] + 2
# new_contacts.to_excel(writer, startrow=startrow, index=False)


odf1 = pd.read_excel(file_path, sheet_name='Planilha1', engine='openpyxl')
last_row_index = odf1.index[-1] + 1
print(last_row_index)
# odf = pd.read_excel('Pasta.xlsx')
#
# print(odf)
