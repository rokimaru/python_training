import random
import re


def test_contact_conformity(app):
    list_of_contacts = app.contact.get_contact_list()
    random_contact = random.choice(list_of_contacts)
    index_of_random_contact = app.contact.get_contact_list().index(random_contact)
    contact_from_home_page = random_contact
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index_of_random_contact)
    assert contact_from_home_page.name == contact_from_edit_page.name
    assert contact_from_home_page.surname == contact_from_edit_page.surname
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)


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
