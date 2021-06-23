import pytest


@pytest.fixture(scope='function')
def get_driver(request):
    print('driver init')
    driver = 'mydriver'  # init
    request.cls.driver = driver
    yield
    driver = None  # deinit


class TestUserDriver1:

    @pytest.mark.usefixtures('get_driver')
    def test_existent(self):
        assert self.driver == 'mydriver'


class TestUserDriver2:

    def test_existent(self, get_driver):
        assert self.driver == 'mydriver'
