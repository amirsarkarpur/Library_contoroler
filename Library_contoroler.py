import sqlite3

db = sqlite3.connect("data.db")
cur = db.cursor()

cur.execute(
    """CREATE TABLE IF NOT EXISTS authors (
        id INTEGER PRIMARY KEY,
        name VARCHAR 
    )"""
)

cur.execute(
    """CREATE TABLE IF NOT EXISTS  books(
        id INTEGER PRIMARY KEY,
        name VARCHAR,
        author_id INTEGER,
        enrollment_date VARCHAR,
        author_name VARCHAR,
        FOREIGN KEY (author_id) REFERENCES authors (id)
        
    )"""
)

cur.execute(
    """CREATE TABLE IF NOT EXISTS  members(
        id INTEGER PRIMARY KEY,
        name VARCHAR
    )"""
)



db.commit()

class Book :

   def insert(self):
       name_book = input("name book : ")
       author_id = input("author id : ")
       enrollment_date = input("enrollment date : ")
       
       try:
            cur.execute(
                        """ SELECT name FROM authors WHERE id =? """,(author_id)
                )
            author = cur.fetchone()
            author_name = author[0]
            
            db.commit()

            cur.execute(
                    """INSERT INTO books(name,author_id,enrollment_date,author_name) VALUES(?,?,?,?)""",(name_book,author_id,enrollment_date,author_name)                                       
                )
            
            db.commit()
       except:
           print("not fond author , plaese chek author id in author list and tray again")

           cur.execute(" SELECT * FROM authors")
           rows = cur.fetchall()
           for row in rows:
                print("\nauthor list\n")
                print(row)
                print("\n\n")

           cur.execute("DELETE FROM books WHERE id =?",(name_book,))
           db.commit()
            
   def Edit(self) :
        
        id = input(" enter book_id for Edit :\n")
        new_name = input(" enter new name for Edit :\n")
        new_author_id = input(" enter new author_id for Edit :\n")
        new_enrollment_date = input(" enter new enrollment_date for Edit :\n")

        cur.execute(
            """ SELECT name FROM books WHERE id =? """,(id,)
        )
        author = cur.fetchone()
        book_name = author[0]
        
        cur.execute(
            "UPDATE books SET name=? , author_id=? , enrollment_date=? WHERE id =?",(new_name,new_author_id,new_enrollment_date,id)
        )
        db.commit()

        cur.execute("DELETE FROM vaset WHERE book_name =?",(book_name,))

        db.commit()

        try:
            cur.execute(
                        """ SELECT name FROM authors WHERE id =? """,(new_author_id)
                )
            author = cur.fetchone()
            author_name = author[0]

            cur.execute(
                    """INSERT INTO vaset(author_name,book_name) VALUES(?,?)""",(author_name,new_name)                                       
                )
            
            db.commit()

        except:
           
           print("not fond author , plaese chek author id in author list and tray again")

           cur.execute(" SELECT * FROM authors")
           rows = cur.fetchall()
           for row in rows:
                print("\nauthor list\n")
                print(row)
                print("\n\n")       
 
   def Delete(self):

        id = input(" enter book id for deleted : \n")

        cur.execute("DELETE FROM books WHERE id =?",(id,))
        db.commit()

   def View(self):

        cur.execute(" SELECT * FROM books")
        rows = cur.fetchall()
        for row in rows:
            print("\n\n")
            print(row)
            print("\n\n")

class Author :

    def insert(self) :

        name_author = input("name author : ")
 
        cur.execute(
            """INSERT INTO authors(name) VALUES(?)""",(name_author,)                                       
        )
        db.commit()

    def Edit(self):
        
        id = input(" enter author_id for Edit :\n")
        new_name = input(" enter new name for Edit :\n")

        cur.execute(
            "UPDATE authors SET name=? WHERE id =?",(new_name,id)
        )

    def Delete(self):

        id = input(" enter auther id for deleted : \n")

        cur.execute("DELETE FROM authors WHERE id =?",(id,))
        db.commit()

        cur.execute("DELETE FROM books WHERE author_id =?",(id,))
        db.commit()

    def View(self):

        cur.execute(" SELECT * FROM authors")
        rows = cur.fetchall()
        for row in rows:
            print("\n\n")
            print(row)
            print("\n\n")


class Member :

    def insert(self) :

        name_member = input("name member : ")
 
        cur.execute(
            """INSERT INTO members(name) VALUES(?)""",(name_member,)                                       
        )
        db.commit()

    def Edit(self):
        
        id = input(" enter member_id for Edit :\n")
        new_name = input(" enter new name for Edit :\n")

        cur.execute(
            "UPDATE members SET name=? WHERE id =?",(new_name,id)
        )

    def Delete(self):

        id = input(" enter member id for deleted : \n")

        cur.execute("DELETE FROM members WHERE id =?",(id,))
        db.commit()

    def View(self):

        cur.execute(" SELECT * FROM members")
        rows = cur.fetchall()
        for row in rows:
            print("\n\n")
            print(row)
            print("\n\n")

class Library :

    
    def insert(self) :
       
        print("peres \n 1 to book \n 2 to author  \n 3 to member")
        cheker = input()
        try:

            if cheker == "1" :

                vaset = Book()
                vaset.insert()

            elif cheker == "2" :

                vaset = Author()
                vaset.insert()

            elif cheker == "3" :

                vaset = Member()
                vaset.insert()
        except:
            print("check the number input , Please pay attention to the help notes!! ")

    def Edite(self):

        try:
            print("peres \n 1 to book \n 2 to author  \n 3 to member")
            cheker = input()

            if cheker == "1" :

                vaset = Book()
                vaset.Edit()

            elif cheker == "2" :

                vaset = Author()
                vaset.Edit()

            elif cheker == "3" :

                vaset = Member()
                vaset.Edit()

        except:
            print("check the number input , Please pay attention to the help notes!! ")

    def Delete(self):

        try:
            print("peres \n 1 to book \n 2 to author  \n 3 to member")
            cheker = input()

            if cheker == "1" :

                vaset = Book()
                vaset.Delete()

            elif cheker == "2" :

                vaset = Author()
                vaset.Delete()

            elif cheker == "3" :

                vaset = Member()
                vaset.Delete()
        except:
            print("check the number input , Please pay attention to the help notes!! ")

    def View(self):

        try:

            print("peres \n 1 to book \n 2 to author  \n 3 to member")
            cheker = input()

            if cheker == "1" :

                vaset = Book()
                vaset.View()

            elif cheker == "2" :

                vaset = Author()
                vaset.View()

            elif cheker == "3" :

                vaset = Member()
                vaset.View()

        except:
            print("check the number input , Please pay attention to the help notes!! ")


start= Library()

while True :

    cheker = input("peres \n 1 to added \n 2 to Edit \n 3 to Delete \n 4 to View \n 0 to Exit \n")

    try:
        if cheker == "1" :
            start.insert()

        elif cheker == '2' :
            start.Edite()

        elif cheker == '3' :
            start.Delete()

        elif cheker == '4' :
            start.View()

        elif cheker == '0' :
            break

    except:
        print("check the number input , Please pay attention to the help notes!! ")


db.close()