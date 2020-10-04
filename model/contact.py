from sys import maxsize


class Contact:

    def __init__(self, firstname=None, middle_name=None, lastname=None, nickname=None, company=None, photo_url=None,
                 title=None, telephone_home=None, telephone_mobile = None, telephone_work=None, fax=None, email1=None,
                 email2=None, email3=None, homepage=None, bday=None, bmonth=None, byear=None,
                 aday=None, amonth=None, ayear=None, address=None, telephone_home_secondary=None, note=None, id=None,
                 all_phones_from_home_page=None, all_emails_from_home_page=None):
        self.firstname = firstname
        self.middle_name = middle_name
        self.lastname = lastname
        self.nickname = nickname
        self.company = company
        self.photo_url = photo_url
        self.title = title
        self.telephone_home = telephone_home
        self.telephone_mobile = telephone_mobile
        self.telephone_work = telephone_work
        self.fax = fax
        self.email1 = email1
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.aday = aday
        self.amonth = amonth
        self.ayear = ayear
        self.address = address
        self.telephone_home_secondary = telephone_home_secondary
        self.note = note
        self.id = id
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_emails_from_home_page = all_emails_from_home_page

    def __repr__(self):
        return '%s:%s:%s' % (self.id, self.firstname, self.lastname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) \
               and self.firstname == other.firstname and self.lastname == other.lastname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

