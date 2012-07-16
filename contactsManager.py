#! /usr/bin/env python

# Program cleans the .vcf android contacts file.

# Deletes all the contacts without any phone number. Deletes all the fields of a contact except the name and telephone field.

# Useful if your contact list is cluttered with contacts synced from facebook and gmail accounts.

# Simply select 'Import from SD card' in your phone after transferring the generated outputContacts.vcf file to your phone SD card.

import sys

if len(sys.argv) <= 1 or len(sys.argv) > 2:
    print "Usage: contactsManager.py <contact_file_name>"
    sys.exit()

# holding a contact
class contact:
    value = ''
    pass

# address book
book = []

    
f = open(sys.argv[1])

line = f.readline()
w = open("outputContacts.vcf", 'w')

c = contact()

while line != '':
    if line.startswith("BEGIN:VCARD"):
        c.value += line
        line = f.readline()
    if line.startswith("VERSION") or line.startswith("TEL") or line.startswith("N") or line.startswith("FN"):
        c.value += line
        line = f.readline()
    if line.startswith("EMAIL") or line.startswith("URL") or line.startswith("ADR") or line.startswith('BDAY'):
        line = f.readline()
    if line.startswith("END:VCARD"):
        c.value += line
        line = f.readline()
        book.append(c)
        del c
        c = contact()
    if line.startswith("PHOTO"):
        while not line.startswith("END:VCARD"):
            line = f.readline()
        c.value += line
        line = f.readline()
        if c.value.find("TEL") >= 0:
            book.append(c)
        del c
        c = contact()

for i in book:
    if i.value.find("TEL") >= 0:
            w.write(i.value)
    
print "Cleaned contacts saved in 'outputContacts.vcf' file.\n"
