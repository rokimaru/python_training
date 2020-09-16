# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(name="test_name", middle_name="test_middle_name", surname="test_surname",
                      nickname="test_nickname", company="test_company", title="test_title",
                      telephone_home="79111111111", telephone_mobile="79222222222", telephone_work="",
                      fax="",
                      email1="test@test.ru", email2="", email3="", homepage="test.com", bday="9",
                      bmonth="December", byear="1991", aday="1", amonth="May", ayear="2000",
                      address="address",
                      telephone_home_secondary="home", note="test")
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == app.contact.count()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)









