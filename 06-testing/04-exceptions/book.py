

class Book:
    def __init__(self, title, isbn):
        self.__title = None
        self.__isbn = None

        self.title = title
        self.isbn = isbn

    @property
    def title(self):
        return self.__title
    
    @title.setter
    def title(self, value):
        if not value:
            raise RuntimeError("Title must not be empty")
        self.__title = value

    @property
    def isbn(self):
        return self.__isbn
    
    @isbn.setter
    def isbn(self, value):
        if not self.is_valid_isbn(value):
            raise RuntimeError("Invalid ISBN number")
        self.__isbn = value
    
    
    def is_valid_isbn(self, isbn):
        # Remove any dashes or spaces
        isbn_digits = "".join(filter(str.isdigit, isbn))
        if len(isbn_digits) != 13:
            return False
        
        # Calculate checksum
        total = 0
        for i, digit in enumerate(isbn_digits):
            digit = int(digit)
            if i % 2 == 0: # even index (0-based), odd position (1-based)
                total += digit
            else: # odd index (0-based), even position (1-based)
                total += digit * 3
        return total % 10 == 0
    