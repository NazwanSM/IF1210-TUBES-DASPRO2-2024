from src.login import isLogin
from src.share import YesOrNo

def logout(dataUser:dict):
    if not isLogin(dataUser):
        print("Logout gagal!")
        print("Anda belum login sebagai user")
    else:

        save = YesOrNo(input("Apa anda ingin menyimpan file sebelum logout ? (Y/N): "))
        print("Logout berhasil")
        if save:
            return True
        else: 
            for colomn in dataUser:
                dataUser[colomn] = ""
            print("Anda tidak melakukan penyimpanan file. Perubahan tidak tersimpan.")
            return False