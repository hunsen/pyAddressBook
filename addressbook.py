_author__ = 'hunsen.lu@gmail.com'

from contact import *
import os
import pickle

class addressbook:
    def __init__(self):
        if not os.path.exists('addressbook.dat'):
            self.addressdict = {}
        else:
            datafile = open('addressbook.dat', 'rb')
            try:
                self.addressdict = pickle.load(datafile)
            except EOFError:
                self.addressdict = {}
            finally:
                datafile.close()

    def save(self):
        datafile = open('addressbook.dat', 'wb')
#        if object.__class__ == '__main__.contact':
#            self.addressdict.update({object.name : object})
        pickle.dump(self.addressdict, datafile)
        datafile.close()

    def addItem(self):
        name = ''
        while len(name.replace(' ', '')) < 1:
            name = input('input name:')
        gender = input('input gender:')
        phone = input('input phone:')
        email = input('input email:')
        address = input('input address:')
        group = input('input group:')
        ct = contact(name, gender, phone, email, address, group)
        self.addressdict.update({ct.name : ct})
        self.save()

    def deleteItem(self):
        ct = self.searchItem()
        if not ct == None:
            del self.addressdict[ct.name]
            self.save()

    def modifyItem(self):
        ct = self.searchItem()
        if not ct == None:
            del self.addressdict[ct.name]
            self.addItem()

    def searchItem(self):
        name = ''
        while len(name.replace(' ', '')) < 1:
            name = input('input name:')
        if name in self.addressdict.keys():
            ct = self.addressdict[name]
            print(contact.showInfo(ct))
            return ct
        else:
            print('No contact info about {0}'.format(name))
            return None

    def showmenu(self):
        print('     1. Add a new contact')
        print('     2. Delete a contact')
        print('     3. Modify a contact')
        print('     4. Search a contact')
        print('     q. Quit')
        c = input('Enter your choice:')
        if c == '1':
            self.addItem()
        elif c == '2':
            self.deleteItem()
        elif c == '3':
            self.modifyItem()
        elif c == '4':
            self.searchItem()
        elif c == 'q':
            exit()
        else:
            print('Input error')


if __name__ == '__main__':
    addrbook = addressbook()
    while True:
        addrbook.showmenu()

