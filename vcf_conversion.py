import pandas as pd
import re


def get_phone(vcard):
    phone_number = re.search('waid=\d+.*', vcard)
    if phone_number:
        phone_number = phone_number.group().split(':')[1]
        return re.sub('[-()+:]', '', phone_number)

    return None


def extract_name_and_number(contact_list):
    for contact in contact_list:
        lines = contact.split("\n")
        name = None
        phone = get_phone(contact)

        for line in lines:
            if line.split(":")[0] == 'FN':
                name = line.split(":")[1].strip(';')

        # if phone:
        name_arr.append(name)
        phone_arr.append(phone)


def get_contacts(file_path):
    with open(file_path, 'r', encoding="utf-8") as file:
        contacts = file.read().split("END:VCARD")
        contacts.pop()
        extract_name_and_number(contacts)


def convert_vcf_to_arr(file_path):
    print('Conversion Request Recieved')
    global name_arr
    global phone_arr
    name_arr = []
    phone_arr = []
    get_contacts(file_path)
    contact_arr = [name_arr, phone_arr]

    print('Contacts Converted')
    return contact_arr


if __name__ == '__main__':
    convert_vcf_to_df('contacts.vcf')
