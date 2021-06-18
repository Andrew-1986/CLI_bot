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
