import argparse
import sys

parser = argparse.ArgumentParser(description=
            """
            Cleans up an Android contacts file. If no optional arguments are
            provided, it removes duplicate contacts and keeps only the contact
            name and all the telephone numbers associated with that contact.
            Also, it removes a contact which does not contain any phone number.
            
            If you want to keep any other field other than the name and
            phone number, use optional arguments.
            """)

parser.add_argument('CONTACT', help='The android .vcf contacts file')

parser.add_argument('-p', '--photo',
                    help='keep photograph',
                    default=False, action='store_true')
parser.add_argument('-b', '--birthday',
                    help='keep birthday',
                    default=False, action='store_true')
parser.add_argument('-e', '--email',
                    help='keep email',
                    default=False, action='store_true')
parser.add_argument('-a', '--address',
                    help='keep address',
                    default=False, action='store_true')
parser.add_argument('-u', '--url',
                    help='keep URL',
                    default=False, action='store_true')

args = parser.parse_args()

# Set to check for duplicates
contact_set = set()

# Dictionary with name as key and the whole contact string as value
contact_dict = dict()

    
readfile = open(args.CONTACT)
writefile = open('out_'+args.CONTACT, 'w')
line = readfile.readline()

contact = ''
contact_name = ''

while line != '':

    # These lines anyways must exist
    if line.startswith("BEGIN:VCARD") or \
                line.startswith("VERSION") or \
                line.startswith("N") or \
                line.startswith("TEL"):
        contact += line

    if line.startswith("FN"):
        contact += line
        contact_name = line.partition(':')[2].lower()

    if line.startswith("PHOTO"):
        if args.photo:
            contact += line
        line = readfile.readline()
        while line.startswith(' ') or len(line) is 0:
            if args.photo:
                contact += line
            line = readfile.readline()

    if line.startswith("BDAY"):
        if args.birthday:
            contact += line
    if line.startswith("EMAIL"):
        if args.email:
            contact += line
    if line.startswith("ADR"):
        if args.address:
            contact += line
    if line.startswith("URL"):
        if args.url:
            contact += line


    if line.startswith("END:VCARD"):
        contact += line
        
        if contact.find("TEL") >= 0:
            if contact not in contact_set:
                contact_set.add(contact)
                contact_dict[contact_name] = contact
        contact = ''
        contact_name = ''
    
    line = readfile.readline()

for contact in sorted(contact_dict.iterkeys()):
    writefile.write(contact_dict[contact])
