from datetime import datetime
import pickle
import re
import os

UI = '''
1. Add new contact
2. View contacts
3. Search contact
4. Update contact
5. Delete contact
6. Reset all
7. Exit
'''


class User(object):

    def __init__(self, name=None, address=None, phone=None, mail=None, birthday=None):
        self.name = name
        self.address = address
        self.phone = phone
        self.mail = mail
        self.birthday = birthday

    def __str__(self):
        return "{} {:>15} {:>15} {:>24} {:>15}".format(self.name, self.address, self.phone, self.mail, self.birthday)


class Application(object):

    def __init__(self, database):
        self.database = database
        self.persons = {}
        if not os.path.exists(self.database):
            file_pointer = open(self.database, 'wb')
            pickle.dump({}, file_pointer)
            file_pointer.close()
        else:
            with open(self.database, 'rb') as person_list:
                self.persons = pickle.load(person_list)

    def delete(self):
        name = input("Enter the name to delete: ")
        if name in self.persons:
            del self.persons[name]
            print("Deleted the contact.")
        else:
            print("Contact not found in the app.")
