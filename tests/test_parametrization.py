import pytest
from _pytest.fixtures import SubRequest

@pytest.mark.parametrize('number', [1, 2, 3, 4])
def test_numbers(number: int):
    print(f"number: {number}")
    assert number > 0

@pytest.mark.parametrize('number, expected', [(1, 1) , (2, 4), (3, 9)])
def test_several_numbers(number: int, expected: int):
    assert number ** 2 == expected

@pytest.mark.parametrize('os', ["macos", "linux", "windows", "debian"])
@pytest.mark.parametrize('browser', ["chromium", "webkit", "firefox"])
def test_browser(os: str, browser: str):
    assert len(os + browser) > 0

@pytest.fixture(params=["chromium", "webkit", "firefox"])
def browser(request):
    return request.param

def test_open_browser(browser: str):
    print(f"Running test on browser: {browser}")

@pytest.mark.parametrize('user', ["Masha", "Katya"])
class TestOperations:
    @pytest.mark.parametrize('account', ["Credit card", "Debit card"])
    def test_user_with_operations(self, user: str, account: str):
        print(f"user with operations: {user}")

    def test_user_without_operations(self, user: str):
        print(f"user without operations: {user}")


users = {
    "70000000021": 'User with money on bank account',
    "70000000022": 'User without money on bank account',
    "70000000023": 'User with operations on bank account'
}


@pytest.mark.parametrize('phone_number', users.keys(),
                         ids=lambda phone_number: f"{phone_number}: {users[phone_number]}")
def test_identifiers(phone_number: str):
    print(f"phone number: {phone_number}")
