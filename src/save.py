import os
from src.share import my_len, find_path, loadingmsg
from src.load import readcsvInvent

def write_csv (nama_folder, arr_file, nama_file):
    path_folder = find_path(nama_folder)
    # path_folder akan mengembalikan "" jika tidak nama_folder tidak ditemukan
    if(path_folder==""): # jika nama_folder tidak ditemukan
        path_folder = os.path.join(os.getcwd(), nama_folder)
        os.makedirs(path_folder) # buat folder tersebut
    path_file = os.path.join(path_folder, nama_file) 
    if (os.path.exists(path_file)): # jika file sudah ada dalam folder
        f = open(path_file, "w+") # overwrite
        for [i, colomn] in enumerate(arr_file):
            f.write(str(colomn))
            if (i != my_len(arr_file)-1):
                    f.write(";")
        f.write("\n")
        temp = [i for i in arr_file]
        colomn = temp[0]
        for i in range(len(arr_file[colomn])):
            for [j, colomn] in enumerate(arr_file):
                f.write(str(arr_file[colomn][i]))
                if (j != my_len(arr_file)-1):
                    f.write(";")
            f.write("\n")
        f.close()
    else: # jika file belum ada
        f = open(path_file, "x") # buat file tersebut
        for i in range (my_len (arr_file)):
            for j in range (my_len (arr_file[i])):
                f.write(str(arr_file[i][j]))
                if (j!=my_len(arr_file[i])-2):
                    f.write(";")
            f.write("\n")
        f.close()

# tes fungsi write_csv
# arr = [[0 for j in range (2)] for i in range (4)]
# nama_folder = input()
# arr = [["game", "user_id"],["12", "2"]]
# write_csv(nama_folder, arr, nama_file)

# Fungsi save
def save (user, monster, monster_shop, monster_inventory, item_shop, item_inventory):
    os.system('cls' if os.name=='nt' else 'clear')
    nama_folder = input("Masukkan nama folder penyimpanan: ")
    loadingmsg("Saving")
    write_csv (nama_folder, item_inventory, "item_inventory.csv")
    write_csv (nama_folder, item_shop, "item_shop.csv")
    write_csv (nama_folder, monster_inventory, "monster_inventory.csv")
    write_csv (nama_folder, monster_shop, "monster_shop.csv")
    write_csv (nama_folder, monster, "monster.csv")
    write_csv (nama_folder, user, "user.csv")


    print("Data telah tersimpan pada folder", nama_folder)

def updateUser(dataUser:dict, dataSemuaUser:dict):
    userId = str(dataUser["ID"])
    userName = dataUser["Username"]
    password = dataUser["Password"]
    role = dataUser["Role"]
    oc = dataUser["OC"]
    if userId not in dataSemuaUser["ID"]:
        dataSemuaUser["ID"].append(userId)
        dataSemuaUser["Username"].append(userName)
        dataSemuaUser["Password"].append(password)
        dataSemuaUser["Role"].append(role)
        dataSemuaUser["OC"].append(oc)
    else:
        index = int(userId)-1
        dataSemuaUser["Username"][index] = userName
        dataSemuaUser["Password"][index] = password
        dataSemuaUser["Role"][index] = role
        dataSemuaUser["OC"][index] = oc

def updateItem(potionInvent:dict, ballUser:dict, userId:int):
    invent = readcsvInvent("item_inventory")
    listUser = []
    listType = []
    listQuantity = []
    for barang in invent:
        listUser.append(barang[0])
        listType.append(barang[1])
        listQuantity.append(barang[2])
    itemUser = potionInvent
    itemUser["Type"].append("Monster Ball")  
    itemUser["Quantity"].append(str(ballUser["Ball"]))
    addBall = False
    for [i, id] in enumerate(listUser):
        if id == str(userId):
            for [j, typeItem] in enumerate(itemUser["Type"]):
                if listType[i] == "Monster Ball":
                    addBall = True
                if listType[i] == typeItem:
                    listQuantity[i] = itemUser["Quantity"][j]
                    break
    if not addBall:
        listUser.append(str(userId))
        listType.append("Monster Ball")
        listQuantity.append(str(ballUser["Ball"]))
    itemInvent = {
        "UserID"  : listUser,
        "Type" : listType,
        "Quantity" : listQuantity
    }
    return itemInvent

def updateMonster(monsterUser:dict, userId:int):
    invent = readcsvInvent("monster_inventory")
    listUser = []
    listMonster = []
    listLevel = []
    monsterInvent = [] #list untuk menampung monster user yang ada di database
    for barang in invent:
        listUser.append(barang[0])
        listMonster.append(barang[1])
        listLevel.append(barang[2])
    for [i, id] in enumerate(listUser):
        if id == str(userId):
            monsterInvent.append(listMonster[i])
    for [i, id] in enumerate(listUser):
        if id == str(userId):
            for [j, monsterID] in enumerate(monsterUser["MonsterID"]):
                if monsterID not in monsterInvent:
                    listUser.append(id)
                    listMonster.append(monsterID)
                    listLevel.append(monsterUser["Level"][j])
                    monsterInvent.append(monsterID)
                    break
                if listMonster[i] == monsterID:
                    listLevel[i] = monsterUser["Level"][j]
    monsterInvent = {
        "UserID" : listUser,
        "MonsterID": listMonster,
        "Level": listLevel
    }
    return monsterInvent
