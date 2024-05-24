import pandas as pd
import re


def get_phone(vcard):
    phone_number = re.search('waid=\d+', vcard)
    if phone_number:
        return phone_number.group().split('=')[1]

    phone_number = re.search(':\+.*$', vcard).group()
    return re.sub('[-()+: ]', '', phone_number)


def extract_name_and_number(contact_list):
    for contact in contact_list:
        lines = contact.split("\n")
        name = None
        phone = get_phone(contact)

        for line in lines:
            if line.split(":")[0] == 'FN':
                name = line.split(":")[1].strip(';')

        name_arr.append(name)
        phone_arr.append(phone)


def get_contacts(file_path):
    with open(file_path, 'r', encoding="utf-8") as file:
        contacts = file.read().split("END:VCARD")
        contacts.pop()
        extract_name_and_number(contacts)


def convert_vcf_to_df(file_path):
    global name_arr
    global phone_arr
    name_arr = []
    phone_arr = []
    get_contacts(file_path)
    contact_dict = {'name': name_arr,
                    'phone': phone_arr}

    df = pd.DataFrame(contact_dict)
    return df


if __name__ == '__main__':
    convert_vcf_to_df('contacts.vcf')