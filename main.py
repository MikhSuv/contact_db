import sqlite3


def create_database():
    """
    Создает базу данных и таблицу 'contacts'.
    """
    try:
        # Создаем подключение к базе данных (или создаем новую, если она не существует)
        conn = sqlite3.connect('contacts.db')

        # Создаем курсор для выполнения SQL-запросов
        cursor = conn.cursor()

        # Создаем таблицу 'contacts'
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS contacts (
                id INTEGER PRIMARY KEY,
                first_name TEXT,
                last_name TEXT,
                phone_number TEXT,
                email TEXT
            )
        ''')

        # Закрываем соединение
        conn.close()

        print("База данных 'contacts.db' успешно создана.")
    except sqlite3.Error as e:
        print(f"Ошибка при создании базы данных: {e}")

def add_contact(first_name: str, last_name: str, phone_number: str, email: str) -> None:
    """
    Добавляет новый контакт в базу данных.
    """
    try:
        conn = sqlite3.connect('contacts.db')
        cursor = conn.cursor()

        # Вставляем данные контакта в таблицу
        cursor.execute('''
            INSERT INTO contacts (first_name, last_name, phone_number, email)
            VALUES (?, ?, ?, ?)
        ''', (first_name, last_name, phone_number, email))

        # Сохраняем изменения
        conn.commit()
        conn.close()

        print(f"Контакт {first_name} {last_name} успешно добавлен.")
    except sqlite3.Error as e:
        print(f"Ошибка при добавлении контакта: {e}")

def view_contacts():
    """
    Выводит список всех контактов.
    """
    try:
        conn = sqlite3.connect('contacts.db')
        cursor = conn.cursor()

        # Получаем все контакты из таблицы
        cursor.execute('SELECT * FROM contacts')
        contacts = cursor.fetchall()

        # Выводим список контактов
        for contact in contacts:
            print(contact)

        conn.close()
    except sqlite3.Error as e:
        print(f"Ошибка при просмотре контактов: {e}")

def get_phone_number(first_name: str, last_name:str) -> None | str:
    try:
        conn = sqlite3.connect("contacts.db")
        cursor = conn.cursor()
        # Выполняем SQL-запрос для получения номера телефона
        cursor.execute('SELECT phone_number FROM contacts WHERE first_name=? AND last_name=?',
                       (first_name, last_name))
        result = cursor.fetchone()
        conn.close()
        if result:
            return result[0]  # Возвращаем номер телефона
        else:
            return None  # Контакт не найден
    except sqlite3.Error as e:
        print(f"Ошибка при получении номера телефона: {e}")
        return None


def delete_contact_by_id(contact_id:str) -> None:
    try:
        conn = sqlite3.connect("contacts.db")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM contacts WHERE id = ?", (contact_id))
        
        conn.commit()
        conn.close()
        print(f"Контакт с id {contact_id} успешно удален.")
    except sqlite3.Error as e:
        print(f"Ошибка при удалении контакта: {e}")

def clear_table():
    try:
        # Создаем подключение к базе данных
        conn = sqlite3.connect('contacts.db')
        cursor = conn.cursor()

        # Выполняем SQL-запрос для удаления всех записей из таблицы
        cursor.execute('DELETE FROM contacts')

        # Сохраняем изменения
        conn.commit()
        conn.close()

        print("Все записи в таблице успешно удалены.")
    except sqlite3.Error as e:
        print(f"Ошибка при очистке таблицы: {e}")


if __name__ == "__main__":
    create_database()
    act = int(input("""Что вы хотите сделать?
                        1 : записать новый контакт
                        2 : вывести все контакты
                        3 : по имени и фамилии достать номер телефона
                        4 : удалить контакт оп id
                        5 : очистить базу данных\n"""))
    match act:
        case 2:
            view_contacts()
        case 1:
            first_name = input("Введите имя \n")
            last_name = input("Введите фамилию \n")
            phone_number = input("Введите номер телефона \n")
            email = input("Введите email \n")
            add_contact(first_name, last_name, phone_number, email)
        case 3:
            first_name = input("Введите имя \n")
            last_name = input("Введите фамилию \n")
            phone_number = get_phone_number(first_name, last_name)
            if phone_number:
                print(f"Номер телефона: {phone_number}")
            else:
                print("Контакт не найден.")
        case 4:
            id = input("введите id \n")
            delete_contact_by_id(id)
        case 5:
            clear_table()


