import csv
import uuid
from typing import List


class Book:
    def __init__(self, id, title, author, year, status):
        self.id = id
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def __str__(self):
        return f"[{self.id}]: {self.title} - {self.author}, {self.year}, {self.status}"


class Library:
    file_name = "library.csv"

    def load_books(self) -> List[Book]:                            # ЗАГРУЗКА КНИГ ИЗ БАЗЫ ДАННЫХ
        books = []
        try:
            with open(file=self.file_name, mode='r', encoding='utf-8') as file:
                reader = csv.reader(file)
                for row in reader:
                    try:
                        books.append(Book(*row))
                    except TypeError:
                        pass    # Некорректные строки игнорируются
        except FileNotFoundError:
            pass
        return books

    def __init__(self):
        self.books = self.load_books()

    def save_books(self):
        with open(file=self.file_name, mode='w', encoding='utf-8', newline='') as file:
            writer = csv.writer(file)
            for book in self.books:
                writer.writerow([book.id, book.title, book.author, book.year, book.status])

    # =========== ОСНОВНЫЕ ФУНКЦИИ ===========

    def add_book(self, title: str, author: str, year: str):     # ДОБАВЛЕНИЕ КНИГИ
        self.books.append(Book(str(uuid.uuid4())[:4], title, author, year, 'в наличии'))
        self.save_books()
        print(f"--Книга {title} добавлена--")

    def delete_book(self, del_id: str) -> bool:                 # УДАЛЕНИЕ КНИГИ
        deleted = False
        for book in self.books:
            if del_id == book.id:
                self.books.remove(book)
                deleted = True
                break
        self.save_books()
        return deleted

    def search_book(self) -> List[Book]:                        # ПОИСК КНИГИ
        while True:
            print("1: Искать по названию")
            print("2: Искать по автору")
            print("3: Искать по году")
            print("q: Назад")
            choice = input("Выберите вариант поиска: ").strip()

            if choice == '1':
                keyword = input("Введите keyword для поиска: ").strip()
                return self.search_by_title(keyword)
            elif choice == '2':
                keyword = input("Введите keyword для поиска: ").strip()
                return self.search_by_author(keyword)
            elif choice == '3':
                year = input("Введите год для поиска: ").strip()
                return self.search_by_year(year)
            elif choice == 'q':
                break
            else:
                print("--Ошибка ввода, попробуйте еще раз--")

    def search_by_title(self, keyword: str) -> List[Book]:      # ПОИСК КНИГИ ПО НАЗВАНИЮ
        return [book for book in self.books if keyword.lower() in book.title.lower()]

    def search_by_author(self, keyword: str) -> List[Book]:     # ПОИСК КНИГИ ПО АВТОРУ
        return [book for book in self.books if keyword.lower() in book.author.lower()]

    def search_by_year(self, year: str) -> List[Book]:          # ПОИСК КНИГИ ПО ГОДУ
        return [book for book in self.books if year == book.year]

    def display_book(self):                                     # ОТОБРАЖЕНИЕ ВСЕХ КНИГ
        if self.books:
            for book in self.books:
                print(book)
        else:
            print("--Библиотека пуста--")

    def change_satus(self, change_id: str) -> bool:             # ИЗМЕНЕНИЙ СТАТУСА
        changed = False
        for book in self.books:
            if change_id == book.id:
                while True:
                    print("1: в наличии")
                    print("2: выдана")
                    print("q: Назад")
                    choice = input("Введите номер статуса который хотите установить: ").strip()
                    if choice == '1':
                        book.status = 'в наличии'
                        changed = True
                        self.save_books()
                        break
                    elif choice == '2':
                        book.status = 'выдана'
                        changed = True
                        self.save_books()
                        break
                    elif choice == 'q':
                        break
                    else:
                        print("--Ошибка ввода, попробуйте еще раз--")
        return changed


def main():
    library = Library()

    while True:
        print("1: Добавить книгу")
        print("2: Удалить книгу")
        print("3: Найти книгу")
        print("4: Показать все")
        print("5: Сменить статус книги")
        print("q: Выход")
        choice = input("Введите номер действия: ").strip()

        if choice == '1':
            title = input("Введите название книги: ")
            author = input("Введите автора книги: ")
            year = input("Введите год издания книги: ")
            library.add_book(title, author, year)
        elif choice == '2':
            del_id = input("Введите id книги для удаоения(4 символа): ").strip()
            if library.delete_book(del_id):
                print(f"--Книга с id {del_id} удалена--")
            else:
                print(f"--Книга с id {del_id} не найдена--")
        elif choice == '3':
            books = library.search_book()
            if books:
                for book in books:
                    print(book)
            else:
                print("--Ничего не найдено--")
        elif choice == '4':
            library.display_book()
        elif choice == '5':
            change_id = input("Введите id книги для изменения статуса(4 символа): ").strip()
            if library.change_satus(change_id):
                print(f"--Статус книги с id {change_id} изменен--")
            else:
                print(f"--Книга с id {change_id} не найдена--")
        elif choice == 'q':
            break
        else:
            print("--Ошибка ввода, попробуйте еще раз--")


if __name__ == "__main__":
    main()
