class Book:
    def __init__(self,title,author,isbn):
        self.title=title
        self.author=author
        self.isbn=isbn
    def display(self):
        print(f"title:{self.title},author:{self.author},isbn:{self.isbn}")
n=int(input("no of books"))
books=[]
for i in range(n):
    title=input("title:")
    author=input("author:")
    isbn=input("isbn:")
    b=Book(title,author,isbn)
    books.append(b)
for b in books:
    b.display()
        