import requests
import pprint
import re
import csv


def get_mod_id(url, workshop_id):
    r = requests.get(url)
    x = re.findall("Mod ID: (.*)<\/", r.text)
    if x:  # Check if the list is not empty
        return x[0]
    else:
        return workshop_id  # Or return a default value or error message


# Prompt the user for a comma-separated list of workshop IDs
workshop_ids = input(
    "Enter a semi-colon separated list of workshop IDs: ").split(';')

modsList = []
for workshop_id in workshop_ids:
    workshop_id = workshop_id.strip()  # remove any leading/trailing whitespace
    url = f'https://steamcommunity.com/sharedfiles/filedetails/?id={workshop_id}'
    mod_id = get_mod_id(url, workshop_id)
    if len(mod_id) > 50:
        mod_id = 'ERROR_PLEASE_ADD_MANUALY'

    item = {"workshop_id": workshop_id, 'url': url, 'mod_id': mod_id}
    modsList.append(item)
    print(item)

# get csv
mods_info = ['mod_id', 'workshop_id', 'url']

with open('test.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=mods_info)
    writer.writeheader()
    writer.writerows(modsList)
