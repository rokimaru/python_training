import time
import re

from selenium.webdriver.support.select import Select

from model.contact import Contact


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
        self.change_field_value("home", contact.telephone_home_secondary)
        self.change_field_value("notes", contact.note)

    def upload_photo(self):
        wd = self.app.wd
        wd.find_element_by_name("photo").clear()
        wd.find_element_by_name("photo").send_keys("C:\\photo.jpg")

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            if field_name in ["bday", "bmonth", "aday", "amonth"]:
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
        self.return_to_home_page()
        self.contact_cache = None

    def init_edition_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_css_selector("[title*='Edit']")[index].click()

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name('entry')[index]
        cell = row.find_elements_by_tag_name('td')[7]
        cell.find_element_by_tag_name('a').click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name('entry')[index]
        cell = row.find_elements_by_tag_name('td')[6]
        cell.find_element_by_tag_name('a').click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        name = wd.find_element_by_name('firstname').get_attribute('value')
        surname = wd.find_element_by_name('lastname').get_attribute('value')
        id = wd.find_element_by_name('id').get_attribute('value')
        telephone_home = wd.find_element_by_name('home').get_attribute('value')
        telephone_work = wd.find_element_by_name('work').get_attribute('value')
        telephone_mobile = wd.find_element_by_name('mobile').get_attribute('value')
        telephone_home_secondary = wd.find_element_by_name('phone2').get_attribute('value')
        email1 = wd.find_element_by_name('email').get_attribute('value')
        email2 = wd.find_element_by_name('email2').get_attribute('value')
        email3 = wd.find_element_by_name('email3').get_attribute('value')
        address = wd.find_element_by_name('address').get_attribute('value')
        return Contact(name=name, surname=surname, id=id, telephone_home=telephone_home,
                       telephone_mobile=telephone_mobile, telephone_work=telephone_work,
                       telephone_home_secondary=telephone_home_secondary, email1=email1,
                       email2=email2, email3=email3, address=address)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id('content').text
        telephone_home = re.search('H: (.*)', text).group(1)
        telephone_work = re.search('W: (.*)', text).group(1)
        telephone_mobile = re.search('M: (.*)', text).group(1)
        telephone_home_secondary = re.search('P: (.*)', text).group(1)
        return Contact(telephone_home=telephone_home, telephone_mobile=telephone_mobile,
                       telephone_work=telephone_work, telephone_home_secondary=telephone_home_secondary)

    def submit_edition(self):
        wd = self.app.wd
        wd.find_element_by_name("update").click()
        self.return_to_home_page()
        self.contact_cache = None

    def create(self, contact):
        self.init_creation()
        self.edit_fields(contact)
        self.submit_creation()

    def edit(self, index, new_contact_data):
        self.init_edition_by_index(index)
        self.edit_fields(new_contact_data)
        self.submit_edition()

    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    def del_contact_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_elements_by_name("selected[]")[index].click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.return_to_home_page()
        wd.find_element_by_css_selector("div.msgbox")
        self.contact_cache = None

    def del_contact_by_id(self, id):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_id(id)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.return_to_home_page()
        wd.find_element_by_css_selector("div.msgbox")
        self.contact_cache = None

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def del_first_contact(self):
        self.del_contact_by_index(0)

    def return_to_home_page(self):
        wd = self.app.wd
        if not (wd.current_url == "http://localhost/addressbook/"):
            wd.find_element_by_link_text("home page").click()

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contact_cache = []
            for row in wd.find_elements_by_name('entry'):
                cells = row.find_elements_by_tag_name("td")
                contact_id = cells[0].find_element_by_tag_name('input').get_attribute("value")
                surname = cells[1].text
                name = cells[2].text
                address = cells[3].text
                all_emails = cells[4].text
                all_phones = cells[5].text
                self.contact_cache.append(Contact(name=name, surname=surname, id=contact_id, address=address,
                                                  all_emails_from_home_page=all_emails,
                                                  all_phones_from_home_page=all_phones))
        return list(self.contact_cache)
