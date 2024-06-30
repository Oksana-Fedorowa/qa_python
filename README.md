1.test_add_new_book_add_two_books: тестирует метод add_new_book 
Проверяет добавление двух книг, проверка, что в books_genre они были добавлены успешно.

2.test_set_book_genre:  тестирует метод set_book_genre.Тестирует установку жанра для одной книги и проверяет, 
что метод set_book_genre работает корректно.

3.test_set_book_genre_parametrized:также тестирует метод set_book_genre 
Параметризованный тест для проверки установки жанра различным книгам с разными жанрами.

4.test_get_books_with_specific_genre: тестирует метод get_books_with_specific_genre,
возвращающий список книг с определённым жанром.

5.test_get_books_for_children: тестирует метод get_books_for_children, 
возвращающий книги, подходящие для детей.


6.test_add_book_in_favorites: тестирует метод add_book_in_favorites, добавляющий книгу в избранное.

7.test_delete_book_from_favorites: тестирует метод delete_book_from_favorites, удаляющий книгу из избранного.

8.test_get_list_of_favorites_books: тестирует метод get_list_of_favorites_books, 
возвращающий список избранных книг.

9.test_add_new_book_with_long_name: тестирует метод add_new_book на обработку книг с длинным названием.

10.test_set_genre_for_non_existing_book: тестирует метод set_book_genre 
при попытке установить жанр для книги, которой нет в books_genre.