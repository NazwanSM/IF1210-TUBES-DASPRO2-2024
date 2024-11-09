from src.share import pilihanValid, YesOrNo, clear, display, isDigit, sleep

def monsterManagement(dataMonster:dict):
    while True:
        clear()
        print(
"""<================================================================>
SELAMAT DATANG DI DATABASE PARA MONSTER !!!
1. Tampilkan semua Monster
2. Tambah Monster Baru""")
        pilihan = int(pilihanValid(input("<///> Pilih perintah: "), ["1", "2"]))
        
        if pilihan == 1: # menampilkan data
            showMonsterData(dataMonster, columnLen=[2, 12, 10, 10, 6])
        else : # menambah monster baru
            [isMade, [monsterID, namaMonster, ATK, DEF, HP]] = buatMonster(dataMonster)
            if isMade:
                dataMonster["ID"].append(str(monsterID))
                dataMonster["Type"].append(str(namaMonster))
                dataMonster["ATK_power"].append(str(ATK))
                dataMonster["DEF_power"].append(str(DEF))
                dataMonster["HP"].append(str(HP))
            else:
                break
        isKeluar:bool = YesOrNo(input("<///> Keluar (Y/N): "))
        if isKeluar: # keluar
            break

def showMonsterData(file:dict, columnLen:list[int]=None):
    if columnLen is None:
        columnLen:list[int] = [(len(category) + 2) for category in file]
    for column in enumerate(file):
        nilai = str(column[1])
        makeRow(nilai, columnLen, id=column[0])
    print()
    for i in file["ID"]:
        for category in enumerate(file):
            nilai = str(file[category[1]][int(i)-1])
            makeRow(nilai, columnLen, id=category[0])
        print()

def makeRow(nilai:str, columnLen:int, id:int):
    space:int = (columnLen[id]-len(nilai))
    print(nilai, space * " " + "|", end=" ")

def buatMonster(data:dict) -> list[bool, list[int, str]]:
    namaMonster:str = data["Type"]
    display("Memulai pembuatan Monster...")
    sleep(2)
    while True:
        nama:str = input("Masukkan Type / Nama : ")
        if nama in namaMonster: # mengecek apa nama sudah digunakan
            print("Nama sudah terdaftar, coba lagi!")
        else:
            monsterID:int = len(namaMonster) + 1
            ATK:int = isDigit(input("Masukkan ATK Power : "))
            DEF:int = inputDEF()
            HP:int = isDigit(input("Masukkan HP : "))
            print("Sedang membuat monster...")
            sleep(3)
            clear()
            display(
f"""Monster baru berhasil dibuat!
Type      : {nama}
ATK Power : {ATK}
DEF Power : {DEF}
HP        : {HP}""")
            isTambah:bool = YesOrNo(input("Tambahkan Monster ke database (Y/N):"))
            if isTambah:
                return [True, [monsterID, nama, ATK, DEF, HP]]
            else:
                isExit:bool = YesOrNo(input("<///> Keluar (Y/N): "))
                clear()
                if isExit:
                    return[False, [0, 0, 0, 0, 0]]

def inputDEF() -> int:
    while True:
        DEF:int = isDigit(input("Masukkan DEF Power (0-50) :"))
        if 0 <= DEF <= 50:
            return DEF
        else:
            print("DEF Power harus bernilai 0-50, coba lagi!")
