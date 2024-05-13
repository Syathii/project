import csv

def load_users_from_csv():
    users = []
    with open("users.csv", "r") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            users.append(row)
    return users

def login_user():
    name_id = input("Enter username: ")
    pass_id = input("Enter password: ")
    return name_id, pass_id

def find_user(users, name_id, pass_id):
    for user in users:
        if user["name_id"] == name_id and user["pass_id"] == pass_id:
            return user
    return None

def main():
    print("Welcome to User Login")
    users = load_users_from_csv()
    while True:
        name_id, pass_id = login_user()
        user = find_user(users, name_id, pass_id)
        if user:
            print("Login successful!")
            print("Welcome,", user["name_id"])
            break
        else:
            print("Incorrect username or password. Please try again.")

if __name__ == "__main__":
    main()