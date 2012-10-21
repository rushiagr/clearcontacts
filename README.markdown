# Clear Contacts


Program cleans the .vcf Android contacts file.

Deletes all the contacts without any phone number.

Useful if your contact list is cluttered with contacts synced from Facebook and GMail accounts.

Help text:

    
    usage: contactsManager.py [-h] [-p] [-b] [-e] [-a] [-u] CONTACT
    
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
    
