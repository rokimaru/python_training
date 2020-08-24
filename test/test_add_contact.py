# -*- coding: utf-8 -*-
import pytest
from fixture.application import Application
from model.contact import Contact


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.init_contact_creation()
    app.fill_contact_form(Contact(name="test_name", middle_name="test_middle_name", surname="test_surname",
                           nickname="test_nickname", company="test_company", title="test_title",
                           telephone_home="79111111111", telephone_mobile="79222222222", telephone_work="", fax="",
                           email1="test@test.ru", email2="", email3="", homepage="test.com", bday="9",
                           bmonth="December", byear="1991", aday="1", amonth="May", ayear="2000", address="address",
                           home="home", note="test"))
    app.submit_contact_creation()
    app.return_to_home_page()
    app.logout()







