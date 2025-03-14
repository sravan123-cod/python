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
        print(f"{name}:{address_book[name]}")
    else:
        print("contact not found.")

while True:
    print("/n1. add contact /n2. view contacts /n3.search contacts /n4.exit")
    choice=input("enter choice:")
    if choice=="1":
        name=input("enter name:")
        phone=input("enter phone:")
        email=input("enter email:")
        add_contact(name,phone ,email)
    elif choice=="2":
        view_contacts()
    elif choice=="3":
        name=input("enter your name yo search:")
        search_contact(name)
    elif choice=="4":
        print("exitung address book.")
        break
    else:
        print("invalid choice,try again.")