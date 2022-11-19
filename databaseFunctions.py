import sqlite3


def create_table():
    conn = sqlite3.connect('flashcards.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE FLASHCARDS ('
                   'CardID INTEGER PRIMARY KEY,'
                   'CardFront varchar(255),'
                   'CardBack varchar(255)'
                   ');')
    conn.close()


def delete_table():
    conn = sqlite3.connect('flashcards.db')
    cursor = conn.cursor()
    cursor.execute('DROP TABLE FLASHCARDS')
    conn.close()


def new_entry(card_front, card_back):
    card = [card_front, card_back]
    conn = sqlite3.connect('flashcards.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO FLASHCARDS (CardFront, CardBack) VALUES (?,?);", card)
    conn.commit()
    conn.close()


def delete_entry(card_id):
    card = card_id
    conn = sqlite3.connect('flashcards.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM FLASHCARDS WHERE CardID = ?;", card)
    conn.commit()
    conn.close()
