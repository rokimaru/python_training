from model.group import Group


def test_edit_group(app):
    app.session.login(username="admin", password="secret")
    app.group.init_edition()
    app.group.edit_fields(Group(name="edit test", header="edit test", footer="edit test"))
    app.group.submit_edition()
    app.session.logout()

