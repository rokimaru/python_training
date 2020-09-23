import json
import os
import random
import string
import getopt
import sys
from datetime import datetime
from model.contact import Contact


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


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
                     note=random_string('note ', 30)) for i in range(n)]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, 'w') as out:
    out.write(json.dumps(test_data, default=lambda x: x.__dict__, indent=2))