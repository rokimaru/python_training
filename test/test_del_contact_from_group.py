import random
from fixture.orm import ORMFixture
from model.contact import Contact

orm = ORMFixture(host="localhost", name="addressbook", user="root", password="")


def test_del_contact_in_group(app, db):
    random_contact = random.choice(db.get_contact_list())
    random_group = random.choice(db.get_group_list())
    old_contacts_in_group = orm.get_contacts_in_group(random_group)

    if random_contact in old_contacts_in_group:
        app.contact.del_contact_by_id_from_group(random_contact, random_group)

    else:
        app.contact.add_contact_by_id_in_group(random_contact, random_group)
        old_contacts_in_group = orm.get_contacts_in_group(random_group)
        app.contact.del_contact_by_id_from_group(random_contact, random_group)

    new_contacts_in_group = orm.get_contacts_in_group(random_group)
    old_contacts_in_group.remove(random_contact)
    assert sorted(old_contacts_in_group, key=Contact.id_or_max) == sorted(new_contacts_in_group, key=Contact.id_or_max)