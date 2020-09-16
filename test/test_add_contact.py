# -*- coding: utf-8 -*-
from datetime import datetime

import pytest
import random
import string

from model.contact import Contact


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation
    return prefix + ''.join([random.choice(symbols) for _ in range(random.randrange(maxlen))])


def random_telephone_number():
    symbols = string.digits + '(' + ')' + '-' + ' ' + '+'
    return ''.join(random.choice(symbols) for _ in range(10))


def random_email():
    timestamp = datetime.now().strftime("%d%m%y%H%M%S")
    symbols = string.ascii_letters + string.digits
    return timestamp + '@' + ''.join([random.choice(symbols) for _ in range(random.randrange(5, 10))]) + '.com'


def random_month():
    return random.choice(['December', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
                          'September', 'November'])


def random_day():
    return str(random.choice(range(1, 32)))


def random_year():
    return str(random.choice(range(1900, 2020)))


test_data = [Contact(name=random_string('name ', 10), middle_name=random_string('middle_name ', 10),
                     surname=random_string('surname', 10), nickname=random_string('test_nickname ', 10),
                     company=random_string('test_company ', 10), title=random_string('test_title ', 10),
                     telephone_home=random_telephone_number(), telephone_mobile=random_telephone_number(),
                     telephone_work=random_telephone_number(), fax=random_telephone_number(),
                     email1=random_email(), email2=random_email(), email3=random_email(),
                     homepage=random_string('homepage', 10), bday=random_day(), bmonth=random_month(),
                     byear=random_year(), aday=random_day(), amonth=random_month(), ayear=random_year(),
                     address=random_string('address ', 30), telephone_home_secondary=random_telephone_number(),
                     note=random_string('note ', 30)) for i in range(1)]


@pytest.mark.parametrize("contact", test_data, ids=[repr(x) for x in test_data])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == app.contact.count()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)









