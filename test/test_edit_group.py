from model.group import Group


def test_edit_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(name="edit test", header="edit test", footer="edit test"))
    app.session.logout()

