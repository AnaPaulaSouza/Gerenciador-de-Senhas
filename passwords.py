import _sqlite3

MASTER_PASSWORD = "123456"

senha = input("Insira sua senha master: ")
if senha != MASTER_PASSWORD:
    print("Senha inválida! Encerrando ...")
    exit()

conn = _sqlite3.connect('passwords.db')

cursor = conn.cursor()

cursor.execute( '''
CREATE TABLE IF NOT EXISTS users (
    service TEXT NOT NULL,
    username TEXT NOT NULL,
    password TEXT NOT NULL
);
''')

def menu():
    print("***************************************")
    print("*     i : inserir nova senha          *")
    print("*     l : listas serviços salvos      *")
    print("*     r : recuperar uma senha         *")
    print("*     s : sair                        *")
    print("***************************************")

def get_pasword(service):
    cursor.execute(f'''
        SELECT username, password FROM users
        WHERE service = '{service}'
    ''')

    if cursor.rowcount == 0:
        print("Serviço não cadastrado (use '1' para verificar os serviços).")
    else:
        for user in cursor.fetchall():
            print(user)

def insert_password(service, username, password):
    cursor.execute(f'''
        INSERT INTO users (service, username, password)
        VALUES ('{service}', '{username}', '{password}')
    ''')
    conn.commit()

def show_service():
    cursor.execute('''
        SELECT service FROM users;
    ''')
    for service in cursor.fetchall():
        print(service)

while True:
    menu()
    op = input("O que deseja fazer? ")
    if op not in ['l', 'i', 'r', 's']:
        print("Opção inválida!")
        continue

    if op == 's':
        break

    if op == 'i':
        service = input('Qual o nome do serviço? ')
        username = input('Qual o nome de usuário? ')
        password = input('Qual a senha? ')
        insert_password(service, senha, password)

    if op == 'l':
        show_service()

    if op == 'r':
        service = input('Qual o serviço para qual quer a senha? ')
        get_pasword(service)


conn.close()
