from model.contact import Contact


def test_edit_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(name="test_name"))
    app.contact.edit(Contact(name="new_name"))



