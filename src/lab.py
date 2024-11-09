from src.share import YesOrNo, display, pilihanValid, clear, displayBar
from src.monster import get_stats, monsterList, level

def laboratory(userId:int, dataUser:dict, monsterUser:dict):
    clear()
    while True:
        userName = dataUser["Username"]
        OC = int(dataUser["OC"])
        jumlahPilihan = len(monsterUser["MonsterID"]) + 1
        labMenu(userId, userName, OC, monsterUser, jumlahPilihan) # menampilkan menu
        [pilihan, monsterId, levelMonster] = pilihMonsterLab(monsterUser, jumlahPilihan) # memilih monster yang di upgrade
        if pilihan == 0: # saat memilih keluar
            break
        upgrade(pilihan, monsterId, levelMonster, OC, dataUser, monsterUser) # mengupgrade
        isExit = YesOrNo(input("<///> Keluar (Y/N): "))
        if isExit: # keluar
            break

def labMenu(userId:int, userName:str, OC:int, monsterUser:dict, jumlahPilihan:int):
    print(f"Selamat datang di Lab Dokter Asep. Agent {userName} !!!")
    monsterList(userId, monsterUser)
    print(f"{jumlahPilihan}. Cancel")
    displayBar("UPGRADE PRICE")
    print(
"""1. Level 1 -> Level 2: 300 OC
2. Level 2 -> Level 3: 500 OC
3. Level 3 -> Level 4: 800 OC
4. Level 4 -> Level 5: 1000 OC""")
    print(f"Anda memiliki {OC} OC ")

def pilihMonsterLab(monsterUser:dict, jumlahPilihan:int) -> int:
    while True:
        pilihan = int(pilihanValid(input("<///> Pilih monster: "), [str(i+1) for i in range(jumlahPilihan)]))
        if pilihan == jumlahPilihan:
            return[0, 0, 0]
        monsterId = monsterUser["MonsterID"][pilihan-1]
        levelMonster = level(monsterId, monsterUser)
        if levelMonster == 5:
            print("max level")
        else:
            clear()
            return [pilihan, monsterId, levelMonster]

def upgrade(pilihan:int, monsterId:int, levelMonster:int, OC:int, data:dict, monsterUser:list):
    statMonster = get_stats(monsterId, levelMonster)
    namaMonster:str = statMonster["Name"] 
    if levelMonster == 1:
        hargaUpgrade = 300
    elif levelMonster == 2:
        hargaUpgrade = 500
    elif levelMonster == 3:
        hargaUpgrade = 800
    elif levelMonster == 4:
        hargaUpgrade = 1000
    if hargaUpgrade <= OC:
        display(
f"""{namaMonster} akan di-upgrade ke level {levelMonster + 1}
Harga untuk melakukan upgrade {namaMonster} adalah {hargaUpgrade} OC
Saat ini anda memiliki {OC} OC""")
        isUpgrade = YesOrNo(input("<///> Lanjutkan upgrade (Y/N): "))
        clear()
        if isUpgrade:
            data["OC"] = OC - hargaUpgrade
            monsterUser["Level"][pilihan-1] = str(levelMonster + 1)
            display(f'Selamat, {namaMonster} berhasil di-upgrade ke level {levelMonster + 1} !')
    else:
        print(
f"""Anda hanya memiliki {OC} OC
butuh {hargaUpgrade} OC untuk mengupgrade {namaMonster}""")

# testing sementara
if __name__ == "__main__":
    ...


