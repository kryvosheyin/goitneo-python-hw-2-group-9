from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value):
        if len(value) == 10 and value.isdigit():
            self.value = value
        else:
            raise ValueError("Invalid phone number format.")


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def find_index(self, search_phone):
        for index, phone in enumerate(self.phones):
            if search_phone == str(phone):
                return index
        return None

    def find_phone(self, search_phone):
        if self.find_index(search_phone) is not None:
            return search_phone
        return f"Not able to find the {search_phone} in the address book"

    def edit_phone(self, search_phone, new_phone):
        index = self.find_index(search_phone)
        if index is not None:
            self.phones[index] = Phone(new_phone)

    def remove_phone(self, search_phone):
        index = self.find_index(search_phone)
        if index is not None:
            self.phones.pop(index)
        return self.phones

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {';' .join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, record_name):
        return self.data.get(record_name, "Contact not found")

    def delete(self, record_name):
        self.data.pop(record_name, None)


# Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")
john_record.add_phone("5656565656")
john_record.add_phone("7878787878")
john_record.remove_phone("5656565656")

# Додавання запису John до адресної книги
book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Виведення всіх записів у книзі
for name, record in book.data.items():
    print(record)

# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")

print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

# Видалення запису Jane
book.delete("Jane")
