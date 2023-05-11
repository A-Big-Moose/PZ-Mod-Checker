import requests
import pprint
import re
import csv
import tkinter as tk
from tkinter import messagebox


def get_mod_id(url, workshop_id):
    r = requests.get(url)
    x = re.findall("Mod ID: (.*)<\/", r.text)
    if x:  # Check if the list is not empty
        return x[0]
    else:
        # Show an error message
        messagebox.showerror(
            "Error", f"\033[91m {'Remove ''!'+workshop_id+'!'}\033[00m")
        return workshop_id  # Return the workshop_id in case of error


def process_workshop_ids():
    workshop_ids = entry.get().split(';')
    modsList = []
    for workshop_id in workshop_ids:
        workshop_id = workshop_id.strip()  # remove any leading/trailing whitespace
        url = f'https://steamcommunity.com/sharedfiles/filedetails/?id={workshop_id}'
        mod_id = get_mod_id(url, workshop_id)
        item = {"workshop_id": workshop_id, 'url': url, 'mod_id': mod_id}
        modsList.append(item)
        print(item)

    # get csv
    mods_info = ['mod_id', 'workshop_id', 'url']

    with open('test.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=mods_info)
        writer.writeheader()
        writer.writerows(modsList)


root = tk.Tk()

label = tk.Label(
    root, text="Enter a semi-colon separated list of workshop IDs:")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Process", command=process_workshop_ids)
button.pack()

root.mainloop()
