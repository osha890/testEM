## Описание
Программа предоставляет функционал управления библиотекой. Пользователь может добавлять, удалять, искать книги, просматривать список всех книг и изменять их статус (например, "в наличии" или "выдана"). Данные о книгах сохраняются в CSV-файле `library.csv`.

---

## Классы и методы

### Класс `Book`
**Описание**: Представляет книгу в библиотеке.

#### Атрибуты:
- `id`: уникальный идентификатор книги (строка).
- `title`: название книги.
- `author`: автор книги.
- `year`: год издания книги.
- `status`: статус книги (`"в наличии"` или `"выдана"`).

#### Методы:
- `__str__`: Возвращает строковое представление книги в формате:
  ```
  [ID]: Название - Автор, Год, Статус
  ```

---

### Класс `Library`
**Описание**: Управляет коллекцией книг и взаимодействием с CSV-файлом.

#### Атрибуты:
- `file_name`: имя файла, где хранятся данные о книгах (`library.csv`).
- `books`: список объектов `Book`.

#### Методы:
1. **`load_books`**  
   Загружает книги из CSV-файла.  
   Возвращает: список объектов `Book`.

2. **`save_books`**  
   Сохраняет текущий список книг в CSV-файл.

3. **`add_book(title, author, year)`**  
   Добавляет книгу с указанными параметрами.  
   Генерирует уникальный `id` (первые 4 символа UUID).  

4. **`delete_book(del_id)`**  
   Удаляет книгу по `id`.  
   Возвращает: `True`, если книга была удалена, иначе `False`.

5. **`search_book`**  
   Осуществляет поиск книги по названию, автору или году.  
   Возвращает: список найденных книг.

6. **`search_by_title(keyword)`**  
   Поиск книг по ключевому слову в названии.  
   Возвращает: список найденных книг.

7. **`search_by_author(keyword)`**  
   Поиск книг по ключевому слову в имени автора.  
   Возвращает: список найденных книг.

8. **`search_by_year(year)`**  
   Поиск книг по году издания.  
   Возвращает: список найденных книг.

9. **`display_book`**  
   Выводит список всех книг в библиотеке.

10. **`change_satus(change_id)`**  
    Изменяет статус книги по `id`.  
    Статус может быть изменён на `"в наличии"` или `"выдана"`.  
    Возвращает: `True`, если статус был изменён, иначе `False`.

---

## Функция `main`
**Описание**: Основное меню программы, предоставляет взаимодействие с пользователем.  

#### Возможности:
1. Добавление книги.
2. Удаление книги.
3. Поиск книги (по названию, автору или году).
4. Просмотр всех книг.
5. Изменение статуса книги.
6. Выход из программы.

---

## Как использовать программу
1. Запустите файл main.py.
2. Следуйте инструкциям в текстовом меню для выполнения желаемых операций.
3. Все изменения сохраняются автоматически в файл `library.csv`.
4. Чтобы запустить тесты, перейдите в директорию testEM и используйте команду `python -m unittest discover -s tests`.

---

## Пример работы
### Добавление книги:
```
Введите название книги: Преступление и наказание
Введите автора книги: Фёдор Достоевский
Введите год издания книги: 1866
--Книга Преступление и наказание добавлена--
```

### Поиск книги:
```
1: Искать по названию
2: Искать по автору
3: Искать по году
q: Назад
Выберите вариант поиска: 1
Введите keyword для поиска: преступление
[1234]: Преступление и наказание - Фёдор Достоевский, 1866, в наличии
```

### Удаление книги:
```
Введите id книги для удаления (4 символа): 1234
--Книга с id 1234 удалена--
```

### Отображение всех книг
```
1: Добавить книгу
2: Удалить книгу
3: Найти книгу
4: Показать все
5: Сменить статус книги
q: Выход
Введите номер действия: 4
[ab12]: Гарри Поттер и философский камень - Джоан Роулинг, 1997, в наличии
[bc51]: Война и мир - Лев Толстой, 1869, выдана
[23a1]: Мастер и Маргарита - Михаил Булгаков, 1967, в наличии
```

### Изменение статуса книги
```
1: Добавить книгу
2: Удалить книгу
3: Найти книгу
4: Показать все
5: Сменить статус книги
q: Выход
Введите номер действия: 5
Введите id книги для изменения статуса (4 символа): abcd
1: в наличии
2: выдана
q: Назад
Введите номер статуса который хотите установить: 2
--Статус книги с id abcd изменен--
```
