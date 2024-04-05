class Book():
    def __init__(self, title, author, IBSN, is_checked_out=False):
        self.title = title
        self.author = author
        self.IBSN = IBSN
        self.is_checked_out = is_checked_out

    def check_out(self):
        if self.is_checked_out == True:
            print('This boook is already checked out!')
        else: 
            self.is_checked_out = True

    def return_book(self):
        if self.is_checked_out == True:
            self.is_checked_out = False
            print('The book has been returned')
        else: 
            print('This book can not be returned, you don\'t have it checked out')

book1 = Book('The Lord of the Rings', 'Stephen Speilberg', 18695718)
book1.check_out()
print(book1.author)
print(book1.is_checked_out)
book1.return_book()
print(book1.is_checked_out)
    
        