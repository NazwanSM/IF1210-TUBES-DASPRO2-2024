from src.share import clear, pilihanValid, YesOrNo, pop_element
from src.shop import show_monsters, show_items


def shop_management(monsterShop:dict, itemShop:dict, monsterList:dict, itemList:dict):
    clear()
    print("""<================================================================>
    Irasshaimase! Selamat datang kembali, Mr. Monogram!""")
    print()
    while True:
        action = input(">>> Pilih aksi (lihat/tambah/ubah/hapus/keluar): ").lower()
        if action == "lihat":
            item_type = input(">>> Mau lihat apa? (monster/item): ").lower()
            if item_type == "monster":
                show_monsters(monsterShop, monsterList)
            elif item_type == "item":
                show_items(itemShop)
        elif action == "tambah":
            item_type = input(">>> Mau nambahin apa? (monster/item): ").lower()
            if item_type == "monster":
                add_monster(monsterList, monsterShop)
            elif item_type == "item":
                add_item(itemList, itemShop)
        elif action == "ubah":
            item_type = input(">>> Mau ubah apa? (monster/item): ").lower()
            if item_type == "monster":
                update_monster(monsterList, monsterShop)
            elif item_type == "item":
                update_item(itemShop)
        elif action == "hapus":
            item_type = input(">>> Mau hapus apa? (monster/item): ").lower()
            if item_type == "monster":
                delete_monster(monsterList, monsterShop)
            elif item_type == "item":
                delete_item(itemShop)
        elif action == "keluar":
            print("Dadah Mr. Yanto, sampai jumpa lagi!")
            break
        else:
            print("Aksi tidak valid.")

def add_monster(monsterList:dict, monsterShop:dict):
    # Fungsi untuk menambahkan monster ke dalam shop
    print("ID | Type          | ATK Power | DEF Power | HP   |")
    for monster_id, monster_type, atk_power, def_power, hp in zip(monsterList["ID"], monsterList["Type"], monsterList["ATK_power"], monsterList["DEF_power"], monsterList["HP"]):
        if monster_id not in monsterShop["MonsterID"]:
            print(f"{monster_id:3}| {monster_type:14}| {atk_power:10}| {def_power:10}| {hp:4} |")
    print()

    monsterId = int(input(">>> Masukkan id monster: "))
    if str(monsterId) in monsterList["ID"]:
        index = monsterList["ID"].index(str(monsterId))
        monster_type = monsterList["Type"][index]
        if str(monsterId) in monsterShop["MonsterID"]:
            print(f"{monster_type} sudah ada dalam shop. Operasi tambah dibatalkan.")
        else:
            stok = int(input(">>> Masukkan stok awal: "))
            harga = int(input(">>> Masukkan harga: "))
            
            monsterShop["MonsterID"].insert(index, str(monsterId))
            monsterShop["Stock"].insert(index, str(stok))
            monsterShop["Price"].insert(index, str(harga))
            print(f"{monster_type} telah berhasil ditambahkan ke dalam shop!")
    else:
        print("ID monster tidak ditemukan. Operasi tambah dibatalkan.")
    print()


def add_item(itemList:dict, itemShop:dict):
    # Fungsi untuk menambahkan potion ke dalam shop
    for item in itemList:
        if item not in itemShop["Type"]:
            sudahAda = False
            break
        sudahAda = True
    if sudahAda:
        print("Semua item sudah ada dalam shop. Tidak ada yang perlu ditambahkan.")
        return
    
    print("ID | Type            |")
    for counter, item in enumerate(itemList, start=1):
        if item not in itemShop["Type"]:
            print(f"{counter:<3}| {item:16}|")
    print()

    itemId = int(input(">>> Masukkan id item: "))
    if 1 <= itemId <= counter:
        item = itemList[itemId-1]  # Ambil item berdasarkan indeks
        stok = int(input(">>> Masukkan stok awal: "))
        harga = int(input(">>> Masukkan harga: "))
        itemShop["Type"].append(item)
        itemShop["Stock"].append(str(stok))
        itemShop["Price"].append(str(harga))
        print(f"{item} telah berhasil ditambahkan ke dalam shop!")
    else:
        print("ID item tidak valid. Operasi tambah dibatalkan.")
    print()

def update_monster(monsterList:dict, monsterShop:dict):
    # Fungsi untuk mengubah nilai stok atau harga dari monster
    show_monsters(monsterShop, monsterList)
    monsterId = int(input(">>> Masukkan id monster: "))
    monster_index = next((index for index, monster in enumerate(monsterShop["MonsterID"]) if monster == str(monsterId)), None)

    if monster_index is not None:
        index = monsterList["ID"].index(str(monsterId))
        monster_type = monsterList["Type"][index]
        stok_baru = int(input(">>> Masukkan stok baru: "))
        harga_baru = int(input(">>> Masukkan harga baru: "))

        if stok_baru > 0:
            monsterShop["Stock"][monster_index] = str(stok_baru)

        if harga_baru > 0:
            monsterShop["Price"][monster_index] = str(harga_baru)

        if stok_baru > 0 and harga_baru > 0:
            monsterShop["Stock"][monster_index] = str(stok_baru)
            monsterShop["Price"][monster_index] = str(harga_baru)
            print(f"{monster_type} telah berhasil diubah dengan stok baru sejumlah {stok_baru} dan dengan harga baru {harga_baru}!")
        elif stok_baru > 0:
            monsterShop["Stock"][monster_index] = str(stok_baru)
            print(f"{monster_type} telah berhasil diubah dengan stok baru sejumlah {stok_baru}!")
        elif harga_baru > 0:
            monsterShop["Price"][monster_index] = str(harga_baru)
            print(f"{monster_type} telah berhasil diubah dengan harga baru {harga_baru}!")
        else:
            print("Tidak ada perubahan yang dilakukan.")
    else:
        print("ID monster tidak ditemukan.")
    print()


def update_item(itemShop:dict):
    # Fungsi untuk mengubah nilai stok atau harga dari potion
    show_items(itemShop)
    potionId = int(pilihanValid(input(">>> Masukkan id item: "), [str(i+1) for i in range(len(itemShop["Type"])) ]))

    if 1 <= potionId <= len(itemShop["Type"]):
        potion_index = potionId - 1
        potion_type = itemShop["Type"][potion_index]
        stock_baru = int(input(">>> Masukkan stok baru: "))
        harga_baru = int(input(">>> Masukkan harga baru: "))
        
        if stock_baru > 0 and harga_baru > 0:
            itemShop["Stock"][potion_index] = str(stock_baru)
            itemShop["Price"][potion_index] = str(harga_baru)
            print(f"{potion_type} telah berhasil diubah dengan stok baru sejumlah {stock_baru} dan dengan harga baru {harga_baru}!")
        elif stock_baru > 0:
            itemShop["Stock"][potion_index] = str(stock_baru)
            print(f"{potion_type} telah berhasil diubah dengan stok baru sejumlah {stock_baru}!")
        elif harga_baru > 0:
            itemShop["Price"][potion_index] = str(harga_baru)
            print(f"{potion_type} telah berhasil diubah dengan harga baru {harga_baru}!")
        else:
            print("Tidak ada perubahan yang dilakukan.")
        print()
    else:
        print("ID item tidak valid!")

def delete_monster(monsterList:dict, monsterShop:dict):
    # Fungsi untuk menghapus monster dari shop
    show_monsters(monsterShop, monsterList)
    monsterId = int(input(">>> Masukkan id monster: "))
    monster_index = next((index for index, monsterIdShop in enumerate(monsterShop["MonsterID"]) if monsterIdShop == str(monsterId)), None)

    if monster_index is not None:
        index = monsterList["ID"].index(str(monsterId))
        monster_type = monsterList["Type"][index]
        confirm = YesOrNo(input(f">>> Apakah anda yakin ingin menghapus {monster_type} dari shop (y/n)? "))
        
        if confirm:
            pop_element(monsterShop, monster_index)
        elif confirm.lower() == "n":
            print("Operasi hapus dibatalkan.")
    else:
        print("ID monster tidak ditemukan. Silakan coba lagi.")
    print()


def delete_item(itemShop:dict):
    show_items(itemShop)
    potionId = int(input(">>> Masukkan id item: "))

    potion_index = potionId - 1
    if 0 <= potion_index < len(itemShop["Type"]):
        potion_type = itemShop["Type"][potion_index]
        confirm = YesOrNo(input(f">>> Apakah anda yakin ingin menghapus {potion_type} dari shop (y/n)? "))
        
        if confirm:
            pop_element(itemShop, potion_index)
            print(f"{potion_type} telah berhasil dihapus dari shop!")
        else:
            print("Operasi hapus dibatalkan.")
    else:
        print("ID item tidak ditemukan atau bukan potion. Silakan coba lagi.")
    print()

if __name__ == "__main__" :
    # shop_management()
    ...