from src.load import load, loadInvent
from src.battle import battle
from src.arena import arena
from src.peta import peta
from src.jackpot import jackpot
from src.lab import laboratory
from src.potion import getPotion, updatePotionUser, updatePotionInvent
from src.share import sleep, display
from src.inventory import inventory
from src.shopMng import shop_management
from src.monsterMng import monsterManagement
from src.shop import shop
from src.save import save, updateUser, updateItem, updateMonster
from src.exit import exit
from src.menuHelp import menu

def agent(lokasiUser, dataUser, dataMonster, dataMonsterShop, dataItemShop, potionUser, monsterUser, ballUser, potionInvent):
    changePotionInvent = True
    while True:
        if changePotionInvent:
            updatePotionInvent(potionUser, potionInvent)
        updatePotionUser(potionUser, potionInvent)
        [aksi, lokasiUser] = peta(lokasi=lokasiUser)
        if aksi == "M":
            break
        elif aksi == "B":
            changePotionInvent = True
            isMenang = battle(dataUser, potionUser, monsterUser, ballUser)
            if not isMenang:
                print("Sedang respawn...")
                sleep()
                lokasiUser = (0,0)
        elif aksi == "AM":
            changePotionInvent = True
            display("Anda terkena serangan tiba tiba, bersiaplah !!!")
            sleep()
            isMenang = battle(dataUser, potionUser, monsterUser, ballUser, ambush=True)
            if not isMenang:
                print("Sedang respawn...")
                sleep()
                lokasiUser = (0,0)
        elif aksi == "LA":
            laboratory(userId, dataUser, monsterUser)
        elif aksi == "I":
            inventory(dataUser, monsterUser, potionUser, ballUser)
        elif aksi == "J":
            jackpot(dataUser, dataMonster, monsterUser)
        elif aksi == "A":
            changePotionInvent = True
            arena(dataUser, potionUser, monsterUser)
        elif aksi == "S":
            shop(dataUser, dataMonsterShop, dataItemShop, potionInvent, dataMonster, monsterUser, ballUser)
            changePotionInvent = False
    print(potionUser, potionInvent, monsterUser)
    input()

# Pertama masuk
kondisi = 1
dataUser = {
    "ID": "",
    "Username": "",
    "Password": "",
    "Role": "",
    "OC": ""
}

[dataSemuaUser, dataMonster, dataMonsterShop, dataItemShop] = load()
[kondisi, isExit, isLogout, dataUser] = menu(dataUser)
userId = dataUser["ID"]
[monsterUser, potionInvent, ballUser] = loadInvent(userId)
potionUser = getPotion(userId)
itemList = [itemType for itemType in dataItemShop["Type"]] 
#Loop main
while kondisi != 0:
    if isExit and kondisi == 0:
        break
    if dataUser["Role"] == "admin":
        if kondisi == 1:
            shop_management(dataMonsterShop, dataItemShop, dataMonster, itemList)
        elif kondisi == 2:
            itemInvent = updateItem(potionInvent, ballUser, userId)
            monsterInvent = updateMonster(monsterUser, userId)
            updateUser(dataUser, dataSemuaUser)
            save(dataSemuaUser, dataMonster, dataMonsterShop, monsterInvent, dataItemShop, itemInvent)
            if isExit:
                break
            if isLogout:
                for colomn in dataUser:
                    dataUser[colomn] = ""
            [dataSemuaUser, dataMonster, dataMonsterShop, dataItemShop] = load()
            userId = dataUser["ID"]
            [monsterUser, potionInvent, ballUser] = loadInvent(userId)
            potionUser = getPotion(userId)
            itemList = [itemType for itemType in dataItemShop["Type"]]
        elif kondisi == 3:
            monsterManagement(dataMonster)
    else:
        userId = dataUser["ID"]
        if kondisi == 1:
            lokasiUser = (0,0)
            agent(lokasiUser, dataUser, dataMonster, dataMonsterShop, dataItemShop, potionUser, monsterUser, ballUser, potionInvent)
        elif kondisi == 2:
            if dataUser["ID"] == "":
                print("Anda belum login, tidak ada data yang bisa disimpan")
                break
            else :
                itemInvent = updateItem(potionInvent, ballUser, userId)
                monsterInvent = updateMonster(monsterUser, userId)
                updateUser(dataUser, dataSemuaUser)
                save(dataSemuaUser, dataMonster, dataMonsterShop, monsterInvent, dataItemShop, itemInvent)
                if isExit:
                    break
                if isLogout:
                    for colomn in dataUser:
                        dataUser[colomn] = ""
                [dataSemuaUser, dataMonster, dataMonsterShop, dataItemShop] = load()
                userId = dataUser["ID"]
                [monsterUser, potionInvent, ballUser] = loadInvent(userId)
                potionUser = getPotion(userId)
    [kondisi, isExit, isLogout, dataUser] = menu(dataUser)
exit()