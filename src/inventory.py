from src.battle import showStat
from src.share import clear, display, pilihanValid, YesOrNo, displayBar
from src.monster import get_stats, level


def inventory(dataUser:dict, monsterUser:dict, potionUser:dict, monsterBall:dict[int]):
    while True: 
        clear()
        # membaca data inventory dan menyimpan ke bentuk string dan dictionary
        [inventMonsterUser, dataStatMonster] = monsterInventory(monsterUser) 
        [inventPotionUser, dataStatPotion] = potionInventory(potionUser)
        inventBall:str = ballInventory(monsterBall)
        # penggabungan list monster dan potion
        for i in inventPotionUser:
            inventMonsterUser.append(i)
        if monsterBall["Ball"] != 0:
            inventMonsterUser.append(inventBall)
        invent = inventMonsterUser
        # Menampilkan hasil ke terminal
        displayBar("User Info")
        print(
f"""User ID : {dataUser["ID"]}
Nama    : {dataUser["Username"]}
OC      : {dataUser["OC"]}""")
        displayBar("Inventory List")
        for barang in enumerate(invent):
            print(f"{barang[0]+1}. {barang[1]}")
        nomor:int = len(invent) + 1
        print(f"{nomor}. Keluar")
        # Memilih aksi
        print("Ketikkan id untuk menampilkan item")
        pilihan = int(pilihanValid(input("<///> : "), [str(i) for i in range(1, nomor+1)]))
        clear()
        if pilihan == nomor: # keluar
            break
        elif invent[pilihan-1][:12] == "Monster Ball":
            print("Monster Ball")
            print(f"Quantity  : {monsterBall["Ball"]}") 
        elif invent[pilihan-1][:7] == "Monster":
            print("Monster")
            showStat(dataStatMonster[pilihan-1])
        elif invent[pilihan-1][:6] == "Potion":
            data:list = dataStatPotion[pilihan - len(dataStatMonster) - 1]
            print("Potion")
            display(
f"""Type     : {data[0]}
Quantity : {data[1]}""")
        isExit = YesOrNo(input("<///> Keluar Inventory (Y/N): "))
        if isExit: # jika keluar inventory
            clear()
            break

def monsterInventory(monsterUser:dict) -> list[list[str], list[dict]]:
    # memanggil data monster, monster_inventory dan mencari user yang sesuai
    desc:list[str] = []
    dataStatMonster:list[dict] = []
    # mwmbuat data string monster dan data stat
    for monster in monsterUser["MonsterID"]:
        monsterId:int = int(monster)
        levelMonster:int = level(monsterId, monsterUser)
        stat:dict = get_stats(monsterId, levelMonster)
        maxHp:int = stat["HP"]
        namaMonster:str = stat["Name"]
        hasil:str = "Monster" + " " * (15- len("Monster")) + f"(Name: {namaMonster}, Lvl: {levelMonster}, HP: {maxHp})" # menyusun string info monster
        desc.append(hasil)
        dataStatMonster.append(stat)    
    return [desc, dataStatMonster]

def ballInventory(monsterBall:dict) -> str:
    hasil:str = "Monster Ball" + " " * (15 - len("Monster Ball")) + f"(Qty: {monsterBall["Ball"]})" # menyusun string info monster ball
    return hasil

def potionInventory(potionUser:dict) -> list[list[str], list[list[str]]]:
    inventPotionUser:list[str] = []
    dataPotion:list[list[str]] = []
    # membuat data string potion dan data potion
    for potionType in potionUser:
        if potionType == "Strength":
            type = "ATK"
        elif potionType == "Resilience":
            type = "DEF"
        elif potionType == "Healing":
            type = "Heal"
        quantity:str = potionUser[potionType]
        hasil:str = "Potion" + " " * (15- len("Potion")) + f"(Type: {type}, Qty: {quantity})" # menyusun string info potion
        dataPotion.append([type, quantity])
        inventPotionUser.append(hasil)
    return [inventPotionUser, dataPotion]

# testing sementara
if __name__ == "__main__":
    ...