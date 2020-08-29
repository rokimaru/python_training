from model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(name="del_test"))
    app.contact.del_first_contact()



