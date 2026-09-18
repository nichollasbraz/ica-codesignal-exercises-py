class Library():

    def __init__(self):
        self.readers = {}
        self.borrows = {}
        self.books = {}

        self.borrow_counter = 0
        

    def create_reader(self, reader_id : str = None, timestamp : int = 0) -> bool:
        if reader_id is None or reader_id == "":
            return False

        if reader_id not in self.readers:
            self.readers[reader_id] = {
                "timestamp": timestamp,
                "fines": 0
            }
            self.borrows[reader_id] = []
            return True
        else:
            return False


    def add_book(self, book_id : str = None, title : str = None, qty : int = 0) -> bool:
        if book_id is None or title is None:
            return False
        if book_id == "" or title == "":
            return False
        if qty <= 0:
            return False

        if book_id not in self.books:
            self.books[book_id] = {
                "title": title,
                "qty": qty
            }
            return True
        else:
            self.books[book_id]["qty"] += qty
            return True
        

    def borrow_book(self, reader_id : str = None, book_id : str = None, timestamp : int = 0) -> bool:
        if reader_id is None or book_id is None:
            return False
        if reader_id == "" or book_id == "":
            return False
        if reader_id not in self.readers or book_id not in self.books:
            return False
        else:
            for borrow in self.borrows:
                if borrow["book_id"] == book_id and borrow["returned at"] == None:
                    return False 
                else:
                    self.books[book_id]["qty"] -= 1

                    self.borrow_counter += 1

                    self.borrows[reader_id].append({
                            "book_id": book_id,
                            "borrowed at": timestamp,
                            "returned at": None,
                            "id": self.borrow_counter
                    })
                    return True
            else:
                return False
            