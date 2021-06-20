from datetime import datetime, timedelta
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
7. Show birthday list
8. Exit
'''


class User(object):

    def __init__(self, name=None, address=None, phone=None, mail=None, birthday=None):
        self.name = name
        self.address = address
        self.phone = phone
        self.mail = mail
        self.birthday = birthday

    def __iter__(self):
        return self

    def __next__(self):
        try:
            item = self.birthday
        except AttributeError:
            raise StopIteration
        return item

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

    def add(self):
        name, address, phone, mail, birthday = self.getdetails()
        if name not in self.persons:
            self.persons[name] = User(name, address, phone, mail, birthday)
        else:
            print("Contact already present.")

    def search(self):
        name = input("Enter the name: ")
        if name in self.persons:
            print(self.persons[name])
        else:
            print("Contact not found.")

    def update(self):
        name = input("Enter the name: ")
        if name in self.persons:
            print("Found. Enter new details.")
            name, address, phone, mail, birthday = self.getdetails()
            self.persons[name].__init__(name, address, phone, mail, birthday)
            print("Successfully updated.")
        else:
            print("Contact not found.")

    def delete(self):
        name = input("Enter the name to delete: ")
        if name in self.persons:
            del self.persons[name]
            print("Deleted the contact.")
        else:
            print("Contact not found in the app.")

    def getdetails(self):
        name = input("Name: ")
        address = input("Address: ")
        phone = input("Phone:")
        mail = input("Mail: ")
        birthday = input("Birthday: ")
        return name, address, phone, mail, birthday

    def birthday_list(self):
        days = int(input('enter the number: '))
        tomorrow = datetime.now() + timedelta(days=days)
        tomorrow_formatted = tomorrow.strftime('%d.%m.%Y')
        for names in self.persons.keys():
            if tomorrow_formatted in self.persons[names]:
                print(names)
