from src.login import login, isLogin
from src.logout import logout
from src.register import register_manager
from src.share import pilihanValid, sleep, displayBar, clear, YesOrNo

# MENU AND HELP
# sebelum login
def beforeLogin():
    print("=========== HELP ===========")
    print("Kamu belum login sebagai role apapun. Silahkan login terlebih dahulu.")
    print("         1. Login   : Masuk ke dalam akun yang sudah terdaftar")
    print("         2. Register: Membuat akun baru")
    print("         3. Exit    : Keluar dari game")
    print("")
    print("Footnote:")
    print("         1. Untuk menggunakan aplikasi, silahkan masukkan nama fungsi yang terdaftar")
    print("         2. Jangan lupa untuk memasukkan input yang valid")

def afterLogin(role, dataUser):
    if role == 'agent':
        displayBar("MAIN MENU")
        print(f"""Halo Agent {dataUser["Username"]}. Kamu memasuki command HELP. Kamu memilih jalan yang benar, semoga kamu tidak sesat kemudian. Berikut adalah hal-hal yang dapat kamu lakukan sekarang:
    1. Logout  : Keluar dari akun yang sedang digunakan
    2. Bermain : Memasuki peta kota
    3. Save    : Menyimpan data saat ini
    4. Exit    : Keluar dari game""")
        choice = pilihanValid(input("<///> Pilih perintah (1/2/3/4) "), ["1", "2", "3", "4"])
        isLogout = False
        if choice == "1":
            isSave = logout(dataUser)
            isLogout = True
            isExit = YesOrNo(input("Exit (Y/N): "))
            sleep(2)
            if isSave:
                return [2, isExit, isLogout]
            else: 
                return [0, isExit, isLogout]
        elif choice == "2":
            return [1, False, isLogout]
        elif choice == "3":
            return [2, False, isLogout]
        else:
            isSave = YesOrNo(input("Ingin melakukan save ? (Y/N): "))
            if isSave:
                return[2, True, isLogout]
            else:
                return [0, True, isLogout]
    elif role == 'admin':
        displayBar("MENU")
        print("Selamat datang, Admin. Berikut adalah hal-hal yang dapat kamu lakukan:")
        print("1. Logout   : Keluar dari akun yang sedang digunakan")            
        print("2. Shop     : Melakukan manajemen pada SHOP sebagai tempat jual beli peralatan Agent")
        print("3. Monster  : Menambahkan Monster baru")
        print("4. Exit     : Keluar dari game")
        choice = pilihanValid(input("<///> Pilih perintah (1/2/3) "), ["1", "2", "3", "4"])
        isLogout = False
        if choice == '1':
            isSave = logout(dataUser)
            isLogout = True
            isExit = YesOrNo(input("Exit (Y/N): "))
            sleep(2)
            if isSave:
                return [2, isExit, isLogout]
            else: 
                return [0, isExit, isLogout]
        elif choice == '2':
            return [1, False, isLogout]
        elif choice == '3':
            return [3, False, isLogout]
        else:
            isSave = YesOrNo(input("Ingin melakukan save ? (Y/N): "))
            if isSave:
                return[2, True, isLogout]
            return [0, True, isLogout]


def menu(dataUser:dict):
    kondisi = 0
    isExit = False
    while kondisi == 0:
        clear()
        if not isLogin(dataUser):
            beforeLogin()
            choice = pilihanValid(input("Masukkan pilihan (1/2/3): "), ["1", "2", "3"])
            if choice == '1':
                dataUser = login(dataUser)
            elif choice == '2':
                register_manager()
            else:
                isSave = YesOrNo(input("Ingin melakukan save ? (Y/N): "))
                if isSave:
                    return[2, True, True, dataUser]
                return [0, True, True, dataUser]
        else:
            user_role = dataUser["Role"]
            [kondisi, isExit, isLogout] = afterLogin(user_role, dataUser)
        if isExit:
            break
    return [kondisi, isExit, isLogout, dataUser]