import pytest

@pytest.fixture(autouse=True)
def send_analytycs_data():
    print("Отправляем данные в сервис аналитики")

@pytest.fixture(scope="session")
def settings():
    print("Инициализируем отправку настроек")

@pytest.fixture(scope="class")
def user():
    print("Создаем данные польщователя 1 раз на тестовый класс")

@pytest.fixture(scope="function")
def browser():
    print("Инициализируем браузер")

class TestUserFlow:
    def test_user_login(self, settings):
        ...

    def test_user_can_create_course(self, user):
        ...

    def test_user_can_add_course(self, browser):
        ...