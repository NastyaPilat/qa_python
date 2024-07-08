from main import BooksCollector
import pytest


class TestBooksCollector:
  
    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(collector.get_books_genre()) == 2

    def test_set_book_genre_undefined_name(self):
        collector = BooksCollector()
        name = '_'
        collector.set_book_genre(name, 'Фантастика')

        assert name not in collector.books_genre

    def test_set_book_genre_correct_genre(self):
        collector = BooksCollector()
        name = 'Гордость и предубеждение и зомби'
        collector.add_new_book(name)
        collector.set_book_genre(name, 'Ужасы')

        assert collector.get_book_genre(name) == 'Ужасы'

    def test_get_book_genre_correct_name(self):
        collector = BooksCollector()
        name = 'Что делать, если ваш кот хочет вас убить'
        expected_genre = 'Комедии'
        collector.add_new_book(name)
        collector.set_book_genre(name, expected_genre)

        assert collector.get_book_genre(name) == expected_genre

    @pytest.mark.parametrize("genre, expected_books", [
        ('Фантастика', ['Book1', 'Book3']),
        ('Ужасы', ['Book2']),
        ('Мультфильмы', []),
        ('Комедии', ['Book4']),
    ])
    def test_get_books_with_specific_genre(self, genre, expected_books):
        collector = BooksCollector()
        collector.add_new_book('Book1')
        collector.add_new_book('Book2')
        collector.add_new_book('Book3')
        collector.add_new_book('Book4')
        collector.set_book_genre('Book1', 'Фантастика')
        collector.set_book_genre('Book2', 'Ужасы')
        collector.set_book_genre('Book3', 'Фантастика')
        collector.set_book_genre('Book4', 'Комедии')

        assert collector.get_books_with_specific_genre(genre) == expected_books

    def test_get_books_for_children(self):
        collector = BooksCollector()
        collector.add_new_book('Book1')
        collector.add_new_book('Book2')
        collector.set_book_genre('Book1', 'Фантастика')
        collector.set_book_genre('Book2', 'Мультфильмы')

        assert collector.get_books_for_children() == ['Book1', 'Book2']

    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Book1')
        collector.add_book_in_favorites('Book1')

        assert collector.get_list_of_favorites_books() == ['Book1']

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Book1')
        collector.add_book_in_favorites('Book1')
        collector.delete_book_from_favorites('Book1')

        assert collector.get_list_of_favorites_books() == []

    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()
        collector.add_new_book('Book1')
        collector.add_new_book('Book2')
        collector.add_book_in_favorites('Book1')
        collector.add_book_in_favorites('Book2')

        assert collector.get_list_of_favorites_books() == ['Book1', 'Book2']

    