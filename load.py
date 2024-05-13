import csv

def load_users_from_csv(csv_file):
    users = []
    with open(csv_file, "r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            users.append(row)
    return users

def main():
    csv_file = "users.csv"
    users = load_users_from_csv(csv_file)
    print("User data loaded successfully:")
    for user in users:
        print(user)

if __name__ == "__main__":
    main()