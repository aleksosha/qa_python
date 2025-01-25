Набор юнит-тестов для проверки методов класса BooksCollector

Тесты:
1. test_add_new_book_add_two_books 
Проверяет добавление двух новых книг
2. test_set_book_genre_add_book_with_valid_genre
Проверяет добавление книги с жанром, который присутствует в списке genre
3. test_set_book_genre_invalid_genre
Проверяет добавление книги с жанром, который отсутствует в списке genre
4. test_get_book_genre
Проверяет добавление жанра в список
5. test_get_books_with_specific_genre
Проверяет получение книг с различными жанрами
6. test_get_books_for_children
Проверяет добавление книг с жанрами, подходящими для детей
7. test_add_book_in_favorites
Проверяет добавление книги в список favorites 
8. test_add_book_in_favorites_duplicate
Проверяет дублирование книг при добавлении в список favorites
9. test_delete_book_from_favorites
Проверяет удаление книг из списка favorites
10. test_get_list_of_favorites_books
Проверяет получение книг из списка favorites

Добавленные тесты после замечаний:
1. test_add_new_book_duplicate
Проверяет добавление дублирующихся книг 
2. test_add_new_book_add_book_name_less_than_41_symbols
Проверяет добавление книги с названием меньше 41 символов
3. test_add_new_book_add_book_name_more_than_41_symbols
Проверяет добавление книги с названием больше 41 символом
4. test_add_new_book_add_book_empty_name
Проверяет добавление книги без названия