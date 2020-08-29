from model.contact import Contact


def test_edit_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(name="test_name"))
    app.contact.init_edition()
    app.contact.edit_fields(Contact(name="new_name", surname="new surname"))
    app.contact.submit_edition()


