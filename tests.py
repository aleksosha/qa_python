import pytest
from main import BooksCollector

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
        # словарь books-genre, который нам возвращает метод get_books_genre, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_add_new_book_duplicate(self):
        collector = BooksCollector()

        collector.add_new_book('1984')
        collector.add_new_book('1984')

        assert len(collector.get_books_genre()) == 1

    def test_add_new_book_add_book_name_less_than_41(self):
        collector = BooksCollector()

        collector.add_new_book('Волшебная гора')

        assert len(collector.get_books_genre()) == 1


    def test_add_new_book_add_book_name_more_than_41(self):
        collector = BooksCollector()

        collector.add_new_book('Необыкновенные приключения Робинзона Крузо')

        assert collector.get_books_genre() == {}


    def test_add_new_book_add_book_empty_name(self):
        collector = BooksCollector()

        collector.add_new_book('')

        assert collector.get_books_genre() == {}

    def test_set_book_genre_add_book_with_valid_genre(self):
        collector = BooksCollector()

        collector.add_new_book('1984')
        collector.set_book_genre('1984', 'Комедии')

        assert collector.get_books_genre() == collector.books_genre


    def test_set_book_genre_invalid_genre(self):
        collector = BooksCollector()

        collector.add_new_book('1984')
        collector.set_book_genre('1984', 'Поэзия')

        assert collector.get_books_genre()['1984'] == ''


    def test_get_book_genre(self):

        collector = BooksCollector()

        collector.add_new_book('1984')
        collector.set_book_genre('1984', 'Комедии')

        assert collector.get_book_genre('1984') == 'Комедии'


    @pytest.mark.parametrize("genre, books", [
        ('Фантастика', ['Над пропастью во ржи']),
        ('Комедии', ['1984', '451 градус по Фаренгейту']),
        ('Ужасы', [])
    ])
    def test_get_books_with_specific_genre(self, genre, books):
        collector = BooksCollector()

        for book in books:
            collector.add_new_book(book)
            collector.set_book_genre(book, genre)

        assert collector.get_books_with_specific_genre(genre) == books



    def test_get_books_for_children(self):
        collector = BooksCollector()

        collector.add_new_book('1984')
        collector.set_book_genre('1984', 'Комедии')

        collector.add_new_book('Азбука')
        collector.set_book_genre('Азбука', 'Ужасы')

        assert collector.get_books_for_children() == ['1984']



    def test_add_book_in_favorites(self):
        collector = BooksCollector()

        collector.add_new_book('1984')
        collector.add_book_in_favorites('1984')

        assert '1984' in collector.get_list_of_favorites_books()



    def test_add_book_in_favorites_duplicate(self):
        collector = BooksCollector()

        collector.add_new_book('1984')
        collector.add_book_in_favorites('1984')
        collector.add_book_in_favorites('1984')

        assert len(collector.get_list_of_favorites_books()) == 1



    def test_delete_book_from_favorites(self):
        collector = BooksCollector()

        collector.add_new_book('1984')
        collector.add_book_in_favorites('1984')
        collector.delete_book_from_favorites('1984')

        assert '1984' not in collector.get_list_of_favorites_books()



    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()

        collector.add_new_book('1984')
        collector.add_new_book('451 градус по Фаренгейту')

        collector.add_book_in_favorites('1984')
        collector.add_book_in_favorites('451 градус по Фаренгейту')

        assert collector.get_list_of_favorites_books() == ['1984', '451 градус по Фаренгейту']
