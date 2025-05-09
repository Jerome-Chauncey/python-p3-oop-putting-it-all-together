#!/usr/bin/env python3

class Book:
    def __init__(self, title= "And Then There Were None", page_count= 272):
        self.title = title
        self.page_count = page_count

    @property
    def page_count(self):
        return self._page_count
    
    @page_count.setter
    def page_count(self, page_count):
        if isinstance(page_count, int):
            self._page_count = page_count
        else:
            print("page_count must be an integer")

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")


book = Book(page_count=10)
print(book.page_count)

book.turn_page()


    
        