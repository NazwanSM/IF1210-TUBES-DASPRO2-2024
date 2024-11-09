from src.share import clear, pilihanValid, index
from src.load import monster

def shop(dataUser:dict, monsterShop:dict, itemShop:dict, potionInvent:dict, dataMonster:dict, monsterInvent:dict, ballUser:dict):
    owca_coin = int(dataUser["OC"])
    userId = int(dataUser["ID"])
    clear()
    print("""<================================================================>
    Irasshaimase! Selamat datang di SHOP!!""")
    print()
    while True:
        action = input(">>> Pilih aksi (lihat/beli/keluar): ").lower()
        if action == "lihat":
            item_type = input(">>> Mau lihat apa? (monster/item): ").lower()
            if item_type == "monster":
                show_monsters(monsterShop, dataMonster)
            elif item_type == "item":
                show_items(itemShop)
        elif action == "beli":
            print(f"Jumlah O.W.C.A. Coin-mu sekarang {owca_coin}.")
            item_type = input(">>> Mau beli apa? (monster/item): ").lower()
            if item_type == "monster":
                pilihan = int(pilihanValid(input(">>> Masukkan id monster: "), [str(i + 1) for i in range(len(monsterShop["MonsterID"]))]))
                owca_coin = buy_monster(pilihan, owca_coin, monsterShop, dataMonster, userId, monsterInvent)
            elif item_type == "item":
                item_id = int(pilihanValid(input(">>> Masukkan id item: "), [str(i + 1) for i in range(len(itemShop["Type"]))]))
                quantity = int(input(">>> Masukkan jumlah: "))
                owca_coin = buy_item(item_id, quantity, owca_coin, itemShop, potionInvent, ballUser, userId)
        elif action == "keluar":
            print("Mr. Yanto bilang makasih, belanja lagi ya nanti :)")
            break
        else:
            print("Aksi tidak valid.")
    dataUser["OC"] = str(owca_coin)

    
def show_monsters(monsterShop:dict, monster_data:dict):
    print("ID | Type          | ATK Power | DEF Power | HP   | Stok | Harga")
    for i, monster_id in enumerate(monsterShop["MonsterID"], start=1):
        monsterIndex = index(str(monster_id), monster_data["ID"])
        monster_type = monster_data["Type"][monsterIndex]
        atk_power = monster_data["ATK_power"][monsterIndex]
        def_power = monster_data["DEF_power"][monsterIndex]
        hp = monster_data["HP"][monsterIndex]
        stock = monsterShop["Stock"][i-1]
        price = monsterShop["Price"][i-1]

        print(f"{i:3}| {monster_type:14}| {atk_power:10}| {def_power:10}| {hp:4} | {stock:4} | {price:5}")
    print()

def show_items(itemShop:dict):
    print("ID | Type                | Stok | Harga")
    for counter, i in enumerate(range(len(itemShop["Type"])), start=1):
        print(f"{counter:<3}| {itemShop['Type'][i]:20}| {itemShop['Stock'][i]:5}| {itemShop['Price'][i]}")
    print()

def buy_monster(pilihan: int, owca_coin: int, monsterShop: dict, monster_data: dict, userId: int, monsterInventory: dict) -> int:
    monsterId = monsterShop["MonsterID"][pilihan-1]
    monsterIndex = index(str(monsterId), monster_data["ID"])
    monster_type = monster_data["Type"][monsterIndex]
    stock = monsterShop["Stock"][index(str(monsterId), monsterShop["MonsterID"])]
    price = monsterShop["Price"][index(str(monsterId), monsterShop["MonsterID"])]

    if int(stock) > 0 and int(price) <= owca_coin:
        if str(monsterId) not in monsterInventory["MonsterID"]:
            monsterShop["Stock"][index(str(monsterId), monsterShop["MonsterID"])] = str(int(stock) - 1)
            print(f"Berhasil membeli item: {monster_type}. Item sudah masuk ke inventory-mu!")
            monsterInventory["MonsterID"].append(str(monsterId))
            monsterInventory["Level"].append("1")
            return owca_coin - int(price)
        else:
            print(f"Monster {monster_type} sudah ada dalam inventory-mu! Pembelian dibatalkan.")
    elif int(stock) == 0:
        print("Stok monster ini habis!")
    else:
        print("OC-mu tidak cukup.")

    return owca_coin

def buy_item(id:int, quantity:int, owca_coin:int, itemShop:dict, potionInvent:dict, ballUser:dict, userId:int) -> int:
    item = next((p for p in itemShop["Type"] if p == itemShop["Type"][id-1]), None)
    if item:
        stock = itemShop["Stock"][id-1]
        price = itemShop["Price"][id-1]
        total_price = int(price) * quantity
        if int(stock) >= quantity and total_price <= owca_coin:
            itemShop["Stock"][id-1] = str(int(stock) - quantity)
            if item in potionInvent["Type"]:
                index = potionInvent["Type"].index(item)
                potionInvent["Quantity"][index] = str(int(potionInvent["Quantity"][index]) + quantity)
            elif item == "Monster Ball":
                ballUser["Ball"] = str(int(ballUser["Ball"]) + quantity)
            else: # Jika item tidak dimiliki sama sekali oleh user
                potionInvent["Type"].append(item)
                potionInvent["Quantity"].append(str(quantity))
            print(f"Berhasil membeli item: {quantity} {item}. Item sudah masuk ke inventory-mu!")
            return owca_coin - total_price
        elif int(stock) < quantity:
            print("Stok item tidak cukup!")
        else:
            print("OC-mu tidak cukup.")
    else:
        print('item tidak ditemukan.')
    return owca_coin

if __name__ == "__main__":
    # userId = 3
    # dataUser = getDataUser(userId)
    # owca_coin = int(dataUser["OC"])
    # shop(owca_coin, userId)
    ...
