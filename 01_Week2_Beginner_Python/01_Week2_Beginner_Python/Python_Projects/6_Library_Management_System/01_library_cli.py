#Library Management System
#add a book
#borrow a book
#return a borrow book
#search book by functionality
#check over due from today date
import json
from datetime import datetime, date

class LibraryManager:
    def __init__(self, file_path):
        self.file_path = file_path
        self.books = []
        self.loadBooks()
        
    def loadBooks(self):
        try:
            with open(self.file_path,'r', encoding='utf-8') as file:
                self.books = json.load(file)
        except:
            self.books = []
    
    def save_book_logs(self):
        with open(self.file_path,'w', encoding='utf-8') as file:
            json.dump(self.books, file, indent=4)
            
    def addBbook(self, title, author, isbn):
        try:
            id = len(self.books) + 1
            new_book = {'id':id,
                        'title':title,
                        'author': author,
                        'ISBN': isbn,
                        'availability': 'available',
                        'borrowed_by': None,
                        'borrow_date': None,
                        'due_date': None
                        }

            if any(new_book['ISBN'] == book['ISBN'] for book in self.books):
                found = True 
                print("Book with this ISBN number already exist. ISBN should be unique")
            else:
                self.books.append(new_book)
                self.save_book_logs()
                print('✅ Book is Borrowed')
                
        except Exception as e:
            print(f'❌ Error while adding a booking {e}')
        
    def borrowBook(self, book_name):
        today_date_str = date.today().strftime('%Y-%m-%d')
        try:
            book_found = None
            for book in self.books:
                if book['title'] == book_name:
                    book_found = book   #--> both book_founf and book reference to same object(dictionary)
                    break
            
            if book_found:  #(agar book mil gaye)
                if(book_found['availability'] == 'Borrowed'):
                        print("This Book is already Borrowed by someone")
                        return
                borrower_name = str(input("Enter Your Name For borrowing the book : ")).capitalize()
                due_date_str = str(input('Enter due date(YYYY-MM-DD) for borrowing a book  : '))
                if due_date_str>=today_date_str:
                        book_found['due_date'] = due_date_str
                        book_found['availability'] = 'Borrowed'
                        book_found['borrowed_by'] = borrower_name
                        book_found['borrow_date'] = today_date_str
                        self.save_book_logs()
                        print('✅ Book is Borrowed')
                        self.save_book_logs()
                else:
                        print("Due Date must be greater than or equal to borrow Date")
            else:
                print("This Book is not available in our Library")
        except ValueError:
            print('❌ Invalid date format! Please use YYYY-MM-DD')
        except KeyError as e:
            print(f"❌ Missing key in book record: {e}")
        except Exception as e:
            print(f'Error while borrowing book: {e}')
    
    def returnBooks(self, book_name):
        today_obj = date.today()
        try:
            book_return = None
            for book in self.books:
                if(book['title'] == book_name and book['availability'] == 'Borrowed'):    #book is available
                    book_return = book
                    break
                
            if not book_return:
                print('This book is not in our library, nor have we lent it to anyone.')
                return
        
            borrower_name = str(input("Enter Book Borrower Name : "))
            if(book_return['borrowed_by'] != borrower_name):
                print("Wrong Borrower Name, Enter Correct Name!")
                return
            
            due_date = datetime.strptime(book['due_date'], '%Y-%m-%d').date()
            if(today_obj > due_date):
                days_late = (today_obj - due_date).days
                print(f'⚠ Late Return Notice: This book was due on {due_date}. {days_late} days late')

            book['availability'] = 'Available'
            book['borrowed_by'] = None
            book['borrow_date'] = None
            book['due_date'] = None
            self.save_book_logs()
            print('✅ Book returned successfully.')
            
        except ValueError:
            print("❌ Invalid date format in book record!")
        except KeyError as e:
            print(f"❌ Missing key in book record: {e}")
        except Exception as e:
            print(f"❌ Error while returning book: {e}")
    
    def searchBookbyTitle(self, title):
        try:
            book_found = [book for book in self.books if book['title'] == title]
            if book_found:
                print('This Book is available in Library')
            else:
                print('This book is not available right now!')
        except Exception as e:
            print(f"❌ Error while searching book: {e}")

    def overDueBooks(self):
        today_obj = date.today()
        try:
            overdue_books = []
            for book in self.books:
                if book['due_date'] is not None:
                    due_date = datetime.strptime(book['due_date'], "%Y-%m-%d").date()
                    if(due_date < today_obj):
                        days_late = (today_obj - due_date).days
                        overdue_books.append({
                            'title': book['title'],
                            'borrowed_by': book['borrowed_by'],
                            'due_date': book['due_date'],
                            'days_late': days_late
                        })
            if not overdue_books:
                print("No overdue Books Today")
            else:
                print("\n📚 Overdue Books:")
                for book in overdue_books:
                    print(f"Title       : {book['title']}")
                    print(f"Borrowed by : {book['borrowed_by']}")
                    print(f"Due date   : {book['due_date']}")
                    print(f"Days late  : {book['days_late']} days")
                    print("-" * 30)
        except ValueError:
            print("❌ Invalid date format in book record!")
        except KeyError as e:
            print(f"❌ Missing key in book record: {e}")
        except Exception as e:
            print(f"❌ Error while fetching overdue books: {e}")
    
    def run(self):
        while True:
            print("\n📚 Library Management System")
            print("1. Add New Book")
            print("2. Borrow Book")
            print("3. Return Book")
            print("4. Search Book by Title")
            print("5. View Overdue Books")
            print("6. Exit")
            print("-" * 30)

            choice = input("Enter choice (1-6): ").strip()
            if choice == '1':
                t = input("Title: ").strip()
                a = input("Author: ").strip()
                i = input("ISBN: ").strip()
                self.addBbook(t, a, i)
            elif choice == '2':
                t = input("Book title to borrow: ").strip()
                self.borrowBook(t)
            elif choice == '3':
                t = input("Book title to return: ").strip()
                self.returnBooks(t)
            elif choice == '4':
                t = input("Book title to search: ").strip()
                self.searchBookbyTitle(t)
            elif choice == '5':
                self.overDueBooks()
            elif choice == '6':
                print("👋 Goodbye!")
                break
            else:
                print("❌ Invalid choice.")

if __name__ == '__main__':
    manager = LibraryManager("6_Library_Management_System\library_books.json")
    manager.run()
    

    

            
    
    
        


    

        
        
    
            
            
            
            
            
    
    
    
                    
                    
                    
                    
                
                
        
        
        
    
    
    