# Описание тестов для класса BooksCollector

## Тесты

### `test_add_new_book_add_two_books`

Этот тест проверяет, что метод `add_new_book` корректно добавляет две книги в коллекцию.

### `test_set_book_genre_undefined_name`

Этот тест проверяет, что метод `set_book_genre` не устанавливает жанр для книги с несуществующим именем.

### `test_set_book_genre_correct_genre`

Этот тест проверяет, что метод `set_book_genre` корректно устанавливает правильный жанр для книги.

### `test_get_book_genre_correct_name`

Этот тест проверяет, что метод `get_book_genre` возвращает правильный жанр для заданной книги.

### `test_get_books_with_specific_genre`

Этот тест проверяет, что метод `get_books_with_specific_genre` возвращает правильный список книг с определенным жанром.

### `test_get_books_for_children`

Этот тест проверяет, что метод `get_books_for_children` возвращает правильный список книг, подходящих для детей.

### `test_add_book_in_favorites`

Этот тест проверяет, что метод `add_book_in_favorites` корректно добавляет книгу в избранное.

### `test_delete_book_from_favorites`

Этот тест проверяет, что метод `delete_book_from_favorites` корректно удаляет книгу из избранного.

### `test_get_list_of_favorites_books`

Этот тест проверяет, что метод `get_list_of_favorites_books` возвращает правильный список избранных книг.
