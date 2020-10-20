import re
import allure
from model.contact import Contact


def test_contact_conformity(app, db):
    with allure.step('Get sorted list of contacts from home page'):
        contacts_from_home_page = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    with allure.step('Get sorted list of contacts from database'):
        contacts_from_db = sorted(db.get_contact_list(), key=Contact.id_or_max)
    with allure.step('Assert if contacts on homepage equal to contacts in database'):
        for i in range(len(contacts_from_home_page)):
            assert contacts_from_home_page[i].firstname == clear_names(contacts_from_db[i].firstname)
            assert contacts_from_home_page[i].lastname == clear_names(contacts_from_db[i].lastname)
            assert contacts_from_home_page[i].address == contacts_from_db[i].address
            assert contacts_from_home_page[i].all_phones_from_home_page == merge_phones_like_on_home_page(
                contacts_from_db[i])
            assert contacts_from_home_page[i].all_emails_from_home_page == merge_emails_like_on_home_page(
                contacts_from_db[i])


def clear(s):
    return re.sub('[() -]', '', s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != '',
                            map(lambda x: clear(x), filter(lambda x: x is not None,
                                [contact.telephone_home, contact.telephone_mobile, contact.telephone_work,
                                 contact.telephone_home_secondary]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != '',
                            map(lambda x: clear(x), filter(lambda x: x is not None,
                                [contact.email1, contact.email2, contact.email3]))))


def clear_names(string):
    if string and string[-1] == " ":
        return string[0:-1]
    else:
        return string
