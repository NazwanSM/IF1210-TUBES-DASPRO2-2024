from src.load import getDataUser, loadData
from src.share import YesOrNo, clear, sleep

def login(dataUser) -> dict:
    dataSemuaUser = loadData("user")
    while True:
        clear()
        if isLogin(dataUser):
            print("Anda berhasil login dengan username", dataUser["Username"])
            sleep(3)
            return dataUser
        userName = input("Masukan username: ")
        if userName in dataSemuaUser["Username"]:
            for [i,_] in enumerate(dataSemuaUser["ID"]):
                if dataSemuaUser["Username"][i] == userName:
                    password = input("Masukan password: ")
                    if dataSemuaUser["Password"][i] == password:
                        userId = i+1
                        dataUser = getDataUser(userId)
                        break
                    else:
                        print("Password salah!")
                        sleep(2)
                        continue
        else: 
            print("Username tidak ditemukan")
            isExit = YesOrNo(input("Keluar (Y/N): "))
            if isExit:
                return dataUser

def isLogin(dataUser):
    return not(dataUser["ID"] == "")