import unittest
from unittest.mock import patch
from ..main import Library
import os


class TestLibrary(unittest.TestCase):
    def setUp(self):
        """Настройка перед каждым тестом."""
        # Создаём временный тестовый файл
        self.test_file = "test_library.csv"
        Library.file_name = self.test_file
        self.library = Library()

    def tearDown(self):
        """Очистка после каждого теста."""
        # Удаляем тестовый файл после завершения тестов
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_add_book(self):                # ДОБАВЛЕНИЕ КНИГИ
        self.library.add_book("Test Book", "Test Author", "2024")
        self.assertEqual(len(self.library.books), 1)
        self.assertEqual(self.library.books[0].title, "Test Book")
        self.assertEqual(self.library.books[0].author, "Test Author")
        self.assertEqual(self.library.books[0].year, "2024")

    def test_delete_book(self):             # УДАЛЕНИЕ КНИГИ
        self.library.add_book("Book to Delete", "Author", "2024")
        book_id = self.library.books[0].id
        self.assertTrue(self.library.delete_book(book_id))
        self.assertEqual(len(self.library.books), 0)

    def test_delete_nonexistent_book(self):     # УДАЛЕНИЕ НЕСУЩЕСТВУЮЩЕЙ КНИГИ
        self.assertFalse(self.library.delete_book("1234"))

    def test_search_by_title(self):             # ПОИСК ПО НАЗВАНИЮ
        self.library.add_book("Find Me", "Author", "2024")
        self.library.add_book("Find Me Too", "Another Author", "2024")
        results = self.library.search_by_title("Me")
        self.assertEqual(len(results), 2)
        self.assertEqual(results[0].title, "Find Me")
        self.assertEqual(results[1].title, "Find Me Too")

    def test_search_by_author(self):            # ПОИСК ПО АВТОРУ
        self.library.add_book("Book1", "Author1", "2024")
        self.library.add_book("Book2", "Author2", "2024")
        results = self.library.search_by_author("Author1")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].author, "Author1")

    def test_search_by_year(self):              # ПОИСК ПО ГОДУ
        self.library.add_book("Book1", "Author1", "2024")
        self.library.add_book("Book2", "Author2", "2023")
        results = self.library.search_by_year("2024")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].year, "2024")

    def test_change_status(self):               # ИЗМЕНЕНИЕ СТАТУСА КНИГИ
        self.library.add_book("Test Book", "Test Author", "2024")
        book_id = self.library.books[0].id

        # Патчим input для подмены ввода
        with patch("builtins.input", side_effect=["2"]):
            self.assertTrue(self.library.change_satus(book_id))
            self.assertEqual(self.library.books[0].status, "выдана")

    def test_change_status_invalid_id(self):    # ИЗМЕНЕНИЕ СТАТУСА НЕСУЩЕСТВУЮЩЕЙ КНИГИ
        self.assertFalse(self.library.change_satus("1234"))

    def test_display_books(self):               # ОТОБРАЖЕНИЕ ВСЕХ КНИГ
        self.library.add_book("Book1", "Author1", "2024")
        self.library.add_book("Book2", "Author2", "2023")
        books_output = [str(book) for book in self.library.books]
        self.assertIn("Book1", books_output[0])
        self.assertIn("Book2", books_output[1])


if __name__ == "__main__":
    unittest.main()
