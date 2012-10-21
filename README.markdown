# Clear Contacts
## Cleans up Android contacts file.

usage: `contactsManager.py [-h] [-p] [-b] [-e] [-a] [-u] CONTACT`

Cleans up an Android contacts file and saves the new file with prefix 'out_'.
If no optional arguments are provided, it removes duplicate contacts and keeps
only the contact name and all the telephone numbers associated with that
contact. Also, it removes a contact which does not contain any phone number.
If you want to keep any other field other than the name and phone number, use
optional arguments.

positional arguments:
  CONTACT         The android .vcf contacts file

optional arguments:
  -h, --help      show this help message and exit
  -p, --photo     keep photograph
  -b, --birthday  keep birthday
  -e, --email     keep email
  -a, --address   keep address
  -u, --url       keep URL



# Contacter

Program cleans the .vcf android contacts file.

Deletes all the contacts without any phone number. Deletes all the fields of a contact except the name and telephone field.

Useful if your contact list is cluttered with contacts synced from facebook and gmail accounts.

Simply select 'Import from SD card' in your phone after transferring the generated outputContacts.vcf file to your phone SD card.

To execute:
    `$ python contactManager.py <contacts_file.vcf>`
