
import pytest


# -------------------------------------------------------------------
# Используем функциональный подход.
# Выносим логику в отдельные функции или фикстуры
# -------------------------------------------------------------------


@pytest.fixture
def users():
    pass


@pytest.fixture
def workers(users):
    pass


def test_workers_are_adults_v2(workers):
    pass
