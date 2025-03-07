address_book={}
def add_contact(name,phone,email):
    address_book[name]={"phone":phone,"Email":email}
    print(f"contact{name}added.")
def view_contacts():
    if not address_book:
        print("address book is empty.")
    else:
        for name,details in address_book.items():
            print(f"{name}:{details}")
def search_contact(name):
    if name in address_book:
        print(f"{name}:{address-book[name]}")
    else:
        print("contact not found.")