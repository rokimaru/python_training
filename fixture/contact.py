import time

from selenium.webdriver.support.select import Select


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def init_creation(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def edit_fields(self, contact):
        wd = self.app.wd
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
        # # birthday
        # wd.find_element_by_name("bday").click()
        # Select(wd.find_element_by_name("bday")).select_by_visible_text(contact.bday)
        # wd.find_element_by_name("bday").click()
        # wd.find_element_by_name("bmonth").click()
        # Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contact.bmonth)
        # wd.find_element_by_name("bmonth").click()
        # wd.find_element_by_name("byear").click()
        # wd.find_element_by_name("byear").clear()
        # wd.find_element_by_name("byear").send_keys(contact.byear)
        # # anniversary
        # wd.find_element_by_name("aday").click()
        # Select(wd.find_element_by_name("aday")).select_by_visible_text(contact.aday)
        # wd.find_element_by_name("aday").click()
        # wd.find_element_by_name("amonth").click()
        # Select(wd.find_element_by_name("amonth")).select_by_visible_text(contact.amonth)
        # wd.find_element_by_name("amonth").click()
        # wd.find_element_by_name("ayear").click()
        # wd.find_element_by_name("ayear").clear()
        self.change_date_value("bday", contact.bday)
        self.change_date_value("bmonth", contact.bmonth)
        self.change_date_value("byear", contact.byear)
        self.change_date_value("aday", contact.aday)
        self.change_date_value("amonth", contact.amonth)
        self.change_date_value("ayear", contact.ayear)
        self.change_field_value("home", contact.home)
        self.change_field_value("notes", contact.note)

    def upload_photo(self):
        wd = self.app.wd
        wd.find_element_by_name("photo").clear()
        wd.find_element_by_name("photo").send_keys("C:\photo.jpg")

    def change_date_value(self, field_name, value):
        wd = self.app.wd
        if value is not None:
            wd.find_element_by_name(field_name).click()
            Select(wd.find_element_by_name(field_name)).select_by_visible_text(value)
            wd.find_element_by_name(field_name).click()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
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
        self.app.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    def del_first_contact(self):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
