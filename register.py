import csv
import datetime

def register_user():
    name_id = input("Masukkan username: ")
    pass_id = input("Masukkan password: ")
    oc_id = input("Masukkanan OC: ")
    # Generating a unique User ID based on current timestamp
    user_id = int(datetime.datetime.now().timestamp())
    registration_date = datetime.datetime.now().strftime("%Y-%m-%d")
    user_data = [user_id, name_id, pass_id, oc_id, registration_date]
    return user_data

def save_user_to_csv(user_data):
    with open("users.csv", "a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(user_data)
    print("Pendaftaran akun berhasil!")
    print("Selamat datang agent! Mari kita mengalahkan Dr. Asep Spakbor dengan Charizard!")

def main():
    print("Selamat datang pengguna baru")
    while True:
        choice = input("Apakah anda ingin mendaftar? (yes/no): ").lower()
        if choice == "yes":
            user_data = register_user()
            save_user_to_csv(user_data)
        elif choice == "no":
            print("Exiting...")
            break
        else:
            print("Pengguna, name_id, sudah terpakai", "silahkan gunakan username lain! Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    main()