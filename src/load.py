from src.share import split, search, display, loadingmsg, find_path, sleep
import os
import argparse

def read_csv(nama_folder, cnt_kolom, nama_file):
    with open(os.path.join(nama_folder, nama_file)) as file:
        # Inisialisasi sebuah variabel bertipe tabel kosong yang akan memuat data dari csv
        res = []
        for line in file:
            items = split(line, cnt_kolom) # parse CSV
            res.append(items) # masukkan baris hasil parsing ke tabel res
        return res

# FUNGSI LOAD
def load():
    parser = argparse.ArgumentParser()
    parser.add_argument("nama_folder", type=str)
    args = parser.parse_args()
    
    nama_folder = args.nama_folder
    if find_path(nama_folder) == "":
        print("Folder " + nama_folder + " tidak ditemukan.")
        exit()
    else:
        loadingmsg("Loading")
        print()
        print('{:^120s}'.format("*" * 120))
        print('{:^120s}'.format("Selamat Datang di.."))
        print("""
                                            O O O    W       W   CCCC      AAA
                                           O     O   W       W   C        A   A
                                           O     O    W  W  W    C       AAAAAAA
                                           O     O    W  W  W    C      A       A
                                            O O O       W W      CCCC  A         A
        """)
        print('{:^120s}'.format("*" * 120))
        sleep()
        print()
    # Masukkan hasil parsing csv ke dalam array
    [dataSemuaUser, dataMonster, dataMonsterShop, dataItemShop] = loadData()
    return [dataSemuaUser, dataMonster, dataMonsterShop, dataItemShop]

def readcsvData(fileName:str) -> list[list[str]]:
    with open(f'data\\{fileName}.csv', 'r') as file:
        hasil:list = []
        for line in file:
            row = list(split(line, ";"))
            hasil.append(row)
        value = []
        for data in enumerate(hasil[0]):
            temp = [hasil[int(j)][data[0]] for j in range(len(hasil))]
            value.append(temp)
        return value

def readcsvInvent(fileName:str, userId:int=None) -> list[list[str]]:
    with open (f"data\\{fileName}.csv", "r") as file:
        hasil:list = []
        for line in file:
            row = list(split(line, ";"))
            hasil.append(row)
        data = []
        if userId is None:
            for barang in hasil:
                data.append([barang[0], barang[1], barang[2]])
            return data[1:]
        else:
            invent = search(0, str(userId), hasil)
            for barang in invent:
                data.append([barang[1], barang[2]])
            return data

def monster() -> dict:
    data = readcsvData("monster")
    monster = {
        "ID":data[0][1:],
        "Type": data[1][1:],
        "ATK_power":data[2][1:],
        "DEF_power":data[3][1:],
        "HP": data[4][1:]
    }
    return monster

def monsterShop() -> dict:
    data = readcsvData("monster_shop")
    monsterShop = {
        "MonsterID":data[0][1:],
        "Stock": data[1][1:],
        "Price":data[2][1:]
    }
    return monsterShop

def user(userId:int = None) -> dict:
    data = readcsvData("user")
    user = {
        "ID":data[0][1:],
        "Username": data[1][1:],
        "Password":data[2][1:],
        "Role":data[3][1:],
        "OC": data[4][1:]
    }
    if userId is not None:
        user = {
            "ID":data[0][userId],
            "Username": data[1][userId],
            "Password":data[2][userId],
            "Role":data[3][userId],
            "OC": data[4][userId]
        }
    return user

def itemShop() -> dict:
    data = readcsvData("item_shop")
    itemShop = {
        "Type":data[0][1:],
        "Stock": data[1][1:],
        "Price":data[2][1:]
    }
    return itemShop

def monsterInventory(userId:int) -> dict:
    data = readcsvInvent("monster_inventory", userId)
    monsterInventory:dict = {
        "MonsterID": [barang[0] for barang in data],
        "Level": [barang[1] for barang in data]
    }
    return monsterInventory

def potionInventory(userId:int) -> dict:
    data = readcsvInvent("item_inventory", userId)
    typeList = []
    quantityList = []
    potionInventory:dict = {
        "Type": typeList,
        "Quantity": quantityList
    }
    for barang in data:
        if barang[0] != "Monster Ball":
            typeList.append(barang[0])
            quantityList.append(barang[1])
    return potionInventory

def ballInventory(userId:int) -> dict:
    data = readcsvInvent("item_inventory", userId)
    quantity = 0
    for barang in data:
        if barang[0] == "Monster Ball":
            quantity = int(barang[1])
    ballInventory:dict = {
        "Ball": quantity
    }
    return ballInventory

def loadData(data:str=None, userId:int=None) -> dict:
    if data is None:
        return[user(), monster(), monsterShop(), itemShop()]
    else:
        if data == "monster":
            return monster()
        elif data == "monster_shop":
            return monsterShop()
        elif data == "user":
            return user(userId)
        elif data == "item_shop":
            return itemShop()

def loadInvent(userId:int, data:str=None) -> dict:
    if data is None:
        return[monsterInventory(userId), potionInventory(userId), ballInventory(userId)]
    else:
        if data == "monster":
            return monsterInventory(userId)
        elif data == "potion":
            return potionInventory(userId)
        elif data == "ball":
            return ballInventory(userId)

def getDataUser(userId:int) -> dict:
    data = loadData("user")
    hasil = {
        "ID": userId,
        "Username": data["Username"][userId-1],
        "Password": data["Password"][userId-1],
        "Role": data["Role"][userId-1],
        "OC": data["OC"][userId-1]
    }
    return hasil

def getBall(userId:int) -> dict:
    data = loadInvent(userId, "ball")
    return data

def showDict(data:dict):
    arr = []
    text = ""
    for i in data:
        arr.append([i, data[i]])
    for [category, value] in arr:
        space = 8 - len(category)
        row = f"{category}" + space * " " + ": " + str(value)
        text += f"""{row}
"""
    display(text[:-1])

if __name__ == "__main__":
    ...
