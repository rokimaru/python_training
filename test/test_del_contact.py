from fixture.application import Application

def test_delete_first_contact(app):
    app.contact.test_delete_first_contact()
    app.return_to_home_page()


