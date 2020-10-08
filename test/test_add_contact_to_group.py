import random
from model.contact import Contact
from fixture.orm import ORMFixture
from model.group import Group

orm = ORMFixture(host="localhost", name="addressbook", user="root", password="")


def test_add_contact_to_group(app, db):
    groups = db.get_group_list()
    contacts = db.get_contacts_list()
    if len(groups) == 0:
        app.group.create(Group(name='group_for_adding_contact_test'))
    if len(contacts) == 0:
        app.contact.create_contact(Contact(firstname='contact_for_adding_contact_to_group_test'))

    random_group = random.choice(groups)
    old_contacts_in_group = orm.get_contacts_in_group(random_group)
    contacts_not_in_group = []
    for contact in contacts:
        if contact not in old_contacts_in_group:
            contacts_not_in_group.append(contact)
    if len(contacts_not_in_group) != 0:
        random_contact = random.choice(contacts_not_in_group)
        app.contact.add_contact_by_id_in_group(random_contact, random_group)
        old_contacts_in_group.append(random_contact)
    else:
        new_contact = app.contact.create_contact(Contact(firstname='contact_for_adding_contact_to_group_test'))
        app.contact.add_contact_by_id_in_group(new_contact, random_group)
        old_contacts_in_group.append(new_contact)

    new_contacts_in_group = orm.get_contacts_in_group(random_group)
    assert sorted(old_contacts_in_group, key=Contact.id_or_max) == sorted(new_contacts_in_group, key=Contact.id_or_max)


