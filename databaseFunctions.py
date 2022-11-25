import sqlite3


def create_table():  # Generate FLASHCARDS table. Set CardID, and Card front and back parameters for entries
    conn = sqlite3.connect('flashcards.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE FLASHCARDS ('
                   'CardID INTEGER PRIMARY KEY,'
                   'CardFront varchar(255),'
                   'CardBack varchar(255)'
                   ');')
    conn.close()


def delete_table():  # Delete flashcards table
    conn = sqlite3.connect('flashcards.db')
    cursor = conn.cursor()
    cursor.execute('DROP TABLE FLASHCARDS')
    conn.close()


def new_entry(card_front, card_back):  # Pass card front and card back from buttons module new_flashcard function
    # Input values into a new entry in the flashcards table
    card = [card_front, card_back]
    conn = sqlite3.connect('flashcards.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO FLASHCARDS (CardFront, CardBack) VALUES (?,?);", card)
    conn.commit()
    conn.close()


def delete_entry(card_id):  # Pass cards ID from buttons module delete_flashcard function
    # Input card ID is deleted from the flashcards table
    card = card_id
    conn = sqlite3.connect('flashcards.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM FLASHCARDS WHERE CardID = ?;", card)
    conn.commit()
    conn.close()


def retrieve_random_card():
    conn = sqlite3.connect('flashcards.db')
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM FLASHCARDS ORDER BY RANDOM() LIMIT 1;""")
    records = cursor.fetchall()
    correct_card = dict()
    for row in records:
        correct_card[0] = row[1]
        correct_card[1] = row[2]
    cursor.close()
    return correct_card


def retrieve_random_answer():
    card_back = ''
    conn = sqlite3.connect('flashcards.db')
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM FLASHCARDS ORDER BY RANDOM() LIMIT 3;""")
    records = cursor.fetchall()
    for row in records:
            card_back = row[2]
    conn.close()
    return card_back


