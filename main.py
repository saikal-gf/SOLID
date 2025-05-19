
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class BookPrinter:
    def print_book(self, book: Book):
        print(f"Книга: {book.title} | Автор: {book.author}")

class BookSaver:
    def save_to_file(self, book: Book):
        print(f"Сохраняем книгу: {book.title} в файл")



class Discount:
    def apply(self, price):
        raise NotImplementedError

class NoDiscount(Discount):
    def apply(self, price):
        return price

class StudentDiscount(Discount):
    def apply(self, price):
        return price * 0.9

class SeniorDiscount(Discount):
    def apply(self, price):
        return price * 0.85


class Shape:
    def area(self):
        raise NotImplementedError

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side


class Scanner:
    def scan(self):
        print("Сканирование...")

class Printer:
    def print(self):
        print("Печать...")

class MultiFunctionDevice(Scanner, Printer):
    pass

class SimplePrinter(Printer):
    pass


class DataStorage:
    def write(self, data):
        raise NotImplementedError

class FileStorage(DataStorage):
    def write(self, data):
        print(f"Запись в файл: {data}")

class DatabaseStorage(DataStorage):
    def write(self, data):
        print(f"Запись в базу данных: {data}")

class DataManager:
    def __init__(self, storage: DataStorage):
        self.storage = storage

    def save(self, data):
        self.storage.write(data)

if __name__ == "__main__":
   
    b = Book("1984", "Дж. Оруэлл")
    printer = BookPrinter()
    saver = BookSaver()
    printer.print_book(b)
    saver.save_to_file(b)

    
    discounts = [NoDiscount(), StudentDiscount(), SeniorDiscount()]
    price = 1000
    for d in discounts:
        print(f"Цена со скидкой: {d.apply(price)}")

    
    shapes = [Rectangle(10, 5), Square(7)]
    mfd.print()

    printer = SimplePrinter()
    printer.print()

    
    file_manager = DataManager(FileStorage())
    db_manager = DataManager(DatabaseStorage())
    file_manager.save("лог-файл")
    db_manager.save("запись в БД")
