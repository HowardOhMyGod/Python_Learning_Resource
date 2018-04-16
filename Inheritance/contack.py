class ContactList(list):
    def search(self, name):
        match_contacts = []
        for contack in self:
            if name in contack.name:
                match_contacts.append(contack.name)

        return match_contacts


class Contact:
    contactList = ContactList()

    def __init__(self, name, age):
        self.name = name
        self.age = age

        self.contactList.append(self)

def test(**kwargs):
    print(kwargs['age'])


if __name__ == '__main__':
    c1 = Contact("Howard", 20)
    c2 = Contact("Howard Ho", 22)
    c3 = Contact("John", 18)

    print(Contact.contactList)
    print(Contact.contactList.search("Howard"))

    test(name=20, age=24)