import random

import pytest

from model.contact import Contact


def test_delete_some_contact(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.contact.create(Contact(firstname="del_test"))
    with pytest.allure.step('Get contact list'):
        old_contacts = db.get_contact_list()
    with pytest.allure.step('Choice random contact in contact list'):
        contact = random.choice(old_contacts)
    with pytest.allure.step('Delete contact from addressbook'):
        app.contact.del_contact_by_id(contact.id)
    with pytest.allure.step('Get new contact list and compare to old contact list without removed contact'):
        new_contacts = db.get_contact_list()
        old_contacts.remove(contact)
        assert old_contacts == new_contacts
    if check_ui:
        assert sorted(db.get_contact_list(), key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                              key=Contact.id_or_max)


