from cryptography.fernet import Fernet

def load_key():
    file = open("key.key","rb")
    key=file.read()
    file.close()
    return key

master_pwd=input("type your master password : ")

# def write_key():
#     key = Fernet.generate_key()
#     with open("key.key","wb") as keyFile:
#         keyFile.write(key)

# write_key()




key = load_key() + master_pwd.encode()
fer = Fernet(key)


def view():
    with open("password.txt", "r") as f:
        for l in f.readlines():
            data = l.rstrip()
            user , passw = data.split("|")
            print(f"user: {user} | password: {fer.decrypt(passw.encode()).decode()}")
def add():
    name = input("account name: ")
    pwd = input("account password: ")

    with open("password.txt", "a") as f:
        f.write(f"{name} | {fer.encrypt(pwd.encode()).decode()} \n")

while True:
    mode = input("would you want to add a new password or view an existing password (view , add)? , q to quit ").lower()
    if mode == "q":
        break
    if mode == "add":
        add()
    if mode == "view":
        view()