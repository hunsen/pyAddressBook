__author__ = 'hunsen.lu@gmail.com'

class contact:
    def __init__(self, name, gender, phone, email, address, group):
        self.name = name
        self.gender = gender
        self.phone = phone
        self.email = email
        self.address = address
        self.group = group

    def showInfo(self):
        title = 'Name\tGender\tPhone Number\tE-mail\t\tAddress\t\tGroup\n' + \
                '----------------------------------------------------------------------\n'
        info =  '{0}\t{1}\t{2}\t{3}\t{4}\t{5}\n'.format(self.name, self.gender,
                                                        self.phone, self.email,
                                                        self.address, self.group)
        return title + info


#ct = contact('Hunsen Lu', 'M', '18201821811', 'hunsen.lu@gmail.com',
#             "Liziyuan Mansion NO.98, Zhennan Road 710", 'Friend')
#print(ct.showInfo())
#print(ct.__class__)