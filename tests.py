import pytest
from main import BooksCollector

@pytest.fixture
def collector():
    return BooksCollector()

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_set_book_genre(self, collector):
        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')
        assert collector.get_book_genre('Гарри Поттер') == 'Фантастика'

    @pytest.mark.parametrize('book_name,genre',[
        ['Гарри Поттер', 'Фантастика'],
        ['Вий', 'Фантастика'],
        ['Золушка', 'Мультфильмы'],
        ['Собака Баскервилий','Детективы']
    ])
    def test_set_book_genre_parametrized(self,collector, book_name, genre):
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_book_genre(book_name) == genre

    def test_get_books_with_specific_genre(self, collector):
        collector.add_new_book('Гарри Поттер')
        collector.add_new_book('Вий')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')
        collector.set_book_genre('Вий', 'Фантастика')
        assert collector.get_books_with_specific_genre('Фантастика') == ['Гарри Поттер', 'Вий']

    def test_get_books_for_children(self, collector):
        collector.add_new_book('Золушка')
        collector.add_new_book('Собака Баскервилий')
        collector.set_book_genre('Золушка', 'Мультфильмы')
        collector.set_book_genre('Собака Баскервилий', 'Детективы')
        assert collector.get_books_for_children() == ['Золушка']

    def test_add_book_in_favorites(self, collector):
        collector.add_new_book('Прислуга')
        collector.add_book_in_favorites('Прислуга')
        assert 'Прислуга' in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites(self, collector):
        collector.add_new_book('Прислуга')
        collector.add_book_in_favorites('Прислуга')
        collector.delete_book_from_favorites('Прислуга')
        assert 'Прислуга' not in collector.get_list_of_favorites_books()

    def test_get_list_of_favorites_books(self, collector):
        collector.add_new_book('Прислуга')
        collector.add_new_book('Как не сойти с ума')
        collector.add_book_in_favorites('Прислуга')
        collector.add_book_in_favorites('Как не сойти с ума')
        favorites = collector.get_list_of_favorites_books()
        assert 'Прислуга' in favorites
        assert 'Как не сойти с ума' in favorites

    def test_add_new_book_with_long_name(self, collector):
        long_name = 'А' * 41
        collector.add_new_book(long_name)
        assert long_name not in collector.get_books_genre()

    def test_set_genre_for_non_existing_book(self, collector):
        book_name = 'Книга, которой нет в списке'
        collector.set_book_genre(book_name, 'Фантастика')
        assert collector.get_book_genre(book_name) is None
        assert book_name not in collector.get_books_genre()
