from main import BooksCollector
import pytest
class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert collector.books_genre == {'Гордость и предубеждение и зомби': '',
                                         'Что делать, если ваш кот хочет вас убить': ''}

    def test_set_book_genre_assign_genre_to_book(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        assert collector.get_book_genre('Гордость и предубеждение и зомби') == 'Ужасы'

    @pytest.mark.parametrize('book_name,book_genre', [
        ['Мертвые души', 'Ужасы'],
        ['Звёздные войны', 'Фантастика'],
        ['Шрек', 'Мультфильмы']
    ])
    def test_get_book_genre_(self, book_name, book_genre):
        collector = BooksCollector()

        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, book_genre)

        assert collector.get_book_genre(book_name) == book_genre

    def test_get_books_with_specific_genre_show_book_specific_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Капитанская дочка')
        collector.set_book_genre('Капитанская дочка', 'Мультфильмы')
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')

        assert collector.get_books_with_specific_genre('Мультфильмы') == ['Капитанская дочка']

    def test_get_books_genre_add_book_with_invalid_genre_and_show_book_genre_list(self):
        collector = BooksCollector()

        collector.add_new_book('Кот леопольд')
        collector.set_book_genre('Кот леопольд', 'Мелодрама')

        assert collector.get_books_genre() == {'Кот леопольд': ''}

    def test_get_books_for_children_get_list_of_children_books(self):
        collector = BooksCollector()

        collector.add_new_book('Капитанская дочка')
        collector.set_book_genre('Капитанская дочка', 'Мультфильмы')
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')

        assert collector.get_books_for_children() == ['Капитанская дочка']

    def test_add_book_in_favorites_add_book_to_favorites(self):
        collector = BooksCollector()

        collector.add_new_book('Звездные войны')
        collector.add_book_in_favorites('Звездные войны')

        assert collector.favorites == ['Звездные войны']

    def test_delete_book_from_favorites_delete_favorite_book(self):
        collector = BooksCollector()

        collector.add_new_book('Спокойной ночи малыши')
        collector.add_book_in_favorites('Спокойной ночи малыши')
        collector.delete_book_from_favorites('Спокойной ночи малыши')

        assert collector.favorites == []

    def test_get_list_of_favorites_books_get_list_of_favorite_books(self):
        collector = BooksCollector()

        collector.add_new_book('Ералаш')
        collector.add_book_in_favorites('Ералаш')

        assert collector.get_list_of_favorites_books() == ['Ералаш']
