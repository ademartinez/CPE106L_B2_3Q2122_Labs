import sqlite3

#Owner Table
try:

    conn = sqlite3.connect('solmaris_condominium_db')
    cursor = conn.cursor()

    print('\nColumns in OWNER Table:')
    data = cursor.execute()
    for column in data.description:
        print(column[0])
    print('\n Data in OWNER Table')
    data.cursor.execute('''SELECT * FROM OWNER''')
    for row in data:
        print(row)
    conn.commit()
    conn.close()

except sqlite3.Error as error:
    print("Error while connecting!")

finally:
    if conn:
        conn.close()
        print("\n Connection closed.")


