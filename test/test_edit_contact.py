from random import randrange
from model.contact import Contact


def test_edit_contact(app, db, check_ui):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="edit_test"))
    old_contacts = db.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="new_name", lastname="new_surname")
    contact.id = old_contacts[index].id
    app.contact.edit(index, contact)
    new_contacts = db.get_contact_list()
    old_contacts[index] = contact
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(db.get_contact_list(), key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                              key=Contact.id_or_max)


