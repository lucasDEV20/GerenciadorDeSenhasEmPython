import sqlite3

MASTER_PASSWORD = "123456"
# classe

conn = sqlite3.connect('passwords.db')

cursor = conn.cursor()

cursor.execute('''

CREATE TABLE IF NOT EXISTS users(
    service TEXT NOT NULL,
    username TEXT NOT NULL,
    passaword TEXT NOT NULL
);
''')


def menu():
    print("********************************")
    print(" i : inseir nova senha          ")
    print(" l : listar serviços salvos     ")
    print(" r : recuperar uma senha        ")
    print(" s : sair                       ")
    print("********************************")

    while True:
        menu()
        op = input("o que deseja fazer ?")
        if op not in ['1', 'i', 'r', 's']:
            print("opçao invalida!")
            continue

        if op == 's':
            break


conn.close()
