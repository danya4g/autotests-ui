import pytest

@pytest.mark.smoke
def test_smoke_case():
    ...

@pytest.mark.regression
def test_regression_case():
    ...

@pytest.mark.smoke
class TestSuite:
    def test_smoke(self):
        ...

    def test_smoke2(self):
        ...
@pytest.mark.regression
class TestUserAuthentification:
    @pytest.mark.smoke
    def test_login(self):
        ...
    @pytest.mark.slow
    def test_password_reset(self):
        ...

    def test_logout(self):
        ...