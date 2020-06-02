import mysql.connector as mycon
import names 
import uuid
import random 

author_names = []
genres = ["Comedy", "Action", "Fantasy", "Literature", "Science", "Informational", "Cook-Book", "Romance", "Sci-Fi", "Thriller", "Adventure", "Fiction", "Crime"]
types = ["Novella", "Storybook", "Informational", "Magazine"]

for iter in range(0, 20): 
    author_names.append(names.get_full_name())

def create_table_book(): 
    con= mycon.connect(host="localhost",user="root",password="saumya", database="school")
    str1="CREATE TABLE book (uuid varchar(255), name varchar (255), author varchar (255), genre varchar (255), type varchar (255), issued_by varchar (255))"
    cur=con.cursor()
    cur.execute(str1)
    print("table created successfully")
    con.close()
try: 
    create_table_book()

except Exception as e:
    print("Never Mind ")

finally: 
    connection = mycon.connect(host="localhost",user="root",password="saumya", database="school")
    cursor = connection.cursor()

    for iter in range(0, 100):
        book_name = "book_" + str(iter)
        id = uuid.uuid4()
        converted = str(id)
        uuid_val = converted
        author_name = random.choice(author_names)
        genre = random.choice(genres)
        type = random.choice(types)
        q = "Insert into book (uuid, name, author, genre, type, issued_by) VALUES (%s, %s, %s, %s, %s, %s)" 
        values = (uuid_val, book_name, author_name, genre, type, "")
        cursor.execute(q, values)
        connection.commit()

    print("records inserted successfully ")
    connection.close()