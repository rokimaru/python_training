import re
import allure


def test_phones_on_home_page(app):
    with allure.step('Get contacts from homepage'):
        contact_from_home_page = app.contact.get_contact_list()[0]
    with allure.step('Get contacts from edit page and check if they are equal to contacts from homepage'):
        contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
        assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)


def test_phones_on_contact_view_page(app):
    with allure.step('Get contacts from viewpage'):
        contact_from_view_page = app.contact.get_contact_from_view_page(0)
    with allure.step('Get contacts from edit page and check if they are equal to contacts from viewpage'):
        contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
        assert contact_from_view_page.telephone_home == contact_from_edit_page.telephone_home
        assert contact_from_view_page.telephone_mobile == contact_from_edit_page.telephone_mobile
        assert contact_from_view_page.telephone_work == contact_from_edit_page.telephone_work
        assert contact_from_view_page.telephone_home_secondary == contact_from_edit_page.telephone_home_secondary


def clear(s):
    return re.sub('[() -]', '', s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != '',
                            map(lambda x: clear(x), filter(lambda x: x is not None, 
                                [contact.telephone_home, contact.telephone_mobile, contact.telephone_work,
                                 contact.telephone_home_secondary]))))
