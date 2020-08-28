# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.init_creation()
    app.group.edit_fields(Group(name="test", header="test", footer="test"))
    app.group.submit_creation()
    app.session.logout()


def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.init_creation()
    app.group.edit_fields(Group(name="", header="", footer=""))
    app.group.submit_creation()
    app.session.logout()
