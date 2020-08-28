import pytest
from fixture.application import Application


@pytest.fixture(scope="session")
def app(request):
    fixture = Application()
    fixture.session.login(username="admin", password="secret")

    def fin():
        fixture.session.login()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture
