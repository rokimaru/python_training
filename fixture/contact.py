import time

from selenium.webdriver.support.select import Select


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def init_creation(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def edit_fields(self, contact):
        self.change_field_value("firstname", contact.name)
        self.change_field_value("middlename", contact.middle_name)
        self.change_field_value("lastname", contact.surname)
        self.change_field_value("nickname", contact.nickname)
        self.upload_photo()
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.telephone_home)
        self.change_field_value("mobile", contact.telephone_mobile)
        self.change_field_value("work", contact.telephone_work)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email", contact.email1)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("homepage", contact.homepage)
        self.change_field_value("bday", contact.bday)
        self.change_field_value("bmonth", contact.bmonth)
        self.change_field_value("byear", contact.byear)
        self.change_field_value("aday", contact.aday)
        self.change_field_value("amonth", contact.amonth)
        self.change_field_value("ayear", contact.ayear)
        self.change_field_value("home", contact.home)
        self.change_field_value("notes", contact.note)

    def upload_photo(self):
        wd = self.app.wd
        wd.find_element_by_name("photo").clear()
        wd.find_element_by_name("photo").send_keys("C:\photo.jpg")

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            if field_name in ["bday", "bmonth", "byear", "aday", "amonth", "ayear"]:
                wd.find_element_by_name(field_name).click()
                Select(wd.find_element_by_name(field_name)).select_by_visible_text(text)
                wd.find_element_by_name(field_name).click()
            else:
                wd.find_element_by_name(field_name).click()
                wd.find_element_by_name(field_name).clear()
                wd.find_element_by_name(field_name).send_keys(text)

    def submit_creation(self):
        wd = self.app.wd
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.app.return_to_home_page()

    def init_edition(self):
        wd = self.app.wd
        wd.find_element_by_xpath("/html/body/div/div[4]/form[2]/table/tbody/tr[2]/td[8]/a/img").click()

    def submit_edition(self):
        wd = self.app.wd
        wd.find_element_by_name("update").click()
        self.app.return_to_home_page()

    def create(self, contact):
        self.init_creation()
        self.edit_fields(contact)
        self.submit_creation()

    def edit(self, new_contact_data):
        self.init_edition()
        time.sleep(2)
        self.edit_fields(new_contact_data)
        time.sleep(2)
        self.submit_edition()

    def count(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    def del_first_contact(self):
        wd = self.app.wd
        self.open_home_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()

    def open_home_page(self):
        wd = self.app.wd
        if not (wd.current_url == "http://localhost/addressbook/"):
            wd.get("http://localhost/addressbook/")

    def return_to_home_page(self):
        wd = self.app.wd
        if not (wd.current_url == "http://localhost/addressbook/"):
            wd.find_element_by_link_text("home page").click()
