"""
Протестируйте классы из модуля test_models_shop/models.py
"""
import pytest
from test_models_shop.models import Product, Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)


@pytest.fixture
def cart():
    return Cart()


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        # TODO напишите проверки на метод check_quantity
        assert product.check_quantity(999) is True  #
        assert product.check_quantity(1000) is True  #
        assert product.check_quantity(1001) is False  #

    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        product.buy(0)
        assert product.quantity == 1000
        product.buy(100)
        assert product.quantity == 900
        product.buy(900)
        assert product.quantity == 0

    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        try:
            product.buy(1001)
        except:
            ValueError
            print("\nВы заказали больше, чем есть на складе")


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """

    def test_add_product(self, cart, product):
        assert len(cart.products) == 0  # Проверка пустой корзины
        cart.add_product(product)
        assert cart.products[product] == 1  # Добавлен продукт в кол-ве 1 единицы. Ожидаем 1
        cart.add_product(product, 1)
        assert cart.products[product] == 2  # Добавлен продукт в кол-ве 1 единицы к уже существубщему товару. Ожидаем 2

    def test_remove_product(self, product, cart):
        cart.add_product(product, 2)
        cart.remove_product(product, 1)
        assert cart.products[product] == 1  # Удаление продукта из корзины, ожидаем 1
        cart.remove_product(product)
        assert len(cart.products) == 0  # Проверка что корзина пуста
        cart.add_product(product, 999)
        cart.remove_product(product, 1001)
        assert len(cart.products) == 0  # remove_count больше чем товара в корзине, ожидаем удаление всей позиции

    def test_clear(self, cart, product):
        cart.add_product(product, 700)
        cart.clear()
        assert len(cart.products) == 0

    def test_get_total_price(self, cart, product):
        cart.add_product(product, 100)
        assert cart.get_total_price() == 10000

    def test_buy_product(self, cart, product):
        cart.add_product(product, 100)
        cart.buy()
        assert len(cart.products) == 0

    def test_buy_product_more(self, cart, product):
        cart.add_product(product, 1001)
        with pytest.raises(ValueError):
            assert cart.buy()  # Покупка товара в кол-ве большем, чем товаров на складе
