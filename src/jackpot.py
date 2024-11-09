from src.load import getDataUser, showDict, load, loadInvent
from src.share import displayBar, YesOrNo, clear, sleep
from src.rng import random
def jackpot(dataUser:dict, dataMonster:dict, monsterUser:dict):
    clear()
    print(
"""$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$ Apakah Anda siap untuk menguji keberuntungan? $$$$$$$$$$
$$$$$$$$$    Menangkan Monster dengan 600 OC saja !!!   $$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$""")
    displayBar("DAFTAR ITEM")
    data:dict[int] = { # barang jackpot, hardcode
    "Topi": 50 ,
    "Pedang" : 100,
    "Koin" : 200,
    "Potion" : 300,
    "Monster" : 500
    }
    showDict(data)
    barang:list[str] = [] # penyimpanan data barang hasil jackpot dalam array
    for i in data:
        barang.append(i)
    print(f"Your OC : {dataUser["OC"]}")
    isMain:bool = YesOrNo(input("Mulai bermain (Y/N): "))
    while isMain:
        if int(dataUser["OC"]) < 600: # tidak cukup uang
            print("Maaf, anda tidak memiliki cukup OC untuk bermain JACKPOT.")
            sleep(2)
            break 
        dataUser["OC"] = str(int(dataUser["OC"]) - 600)
        max:int = len(data) + 1
        # mengenerate hasil jackpot
        hasil1:int = random(numRange=[1, max])
        hasil2:int = random(numRange=[1, max], seed=(hasil1 * random(numRange=[0, 100])))
        hasil3:int = random(numRange=[1, max], seed=(hasil2 ** hasil1))
        barang1:str = barang[hasil1-1]
        barang2:str = barang[hasil2-1]
        barang3:str = barang[hasil3-1]
        # menampilkan jackpot
        displayJackpot(barang1, barang2, barang3)
        if barang1 == barang2 and barang2 == barang3: # jika mendapat jackpot
            banyakMonster:int = len(dataMonster["ID"])+1
            monsterId = str(random(numRange=[1, banyakMonster]))
            count:int = 0
            while monsterId in monsterUser["MonsterID"] and count < banyakMonster+1: # mencari monster yang tidak dipunyai user
                monsterId = str(int(monsterId) + 1)
                if monsterId == str(banyakMonster):
                    monsterId = "1"
                count += 1
            if count > banyakMonster: # jika tidak menemukan monster yang tidak dimiliki
                dataUser["OC"] = str(int(dataUser["OC"]) + 1500)
                print("Anda telah mempunyai semua monster. Sebagai gantinya anda mendapatkan 1500 OC !!!")
            else: # menambahkan monster
                monsterUser["MonsterID"].append(monsterId)
                monsterUser["Level"].append("1")
                namaMonster = dataMonster["Type"][int(monsterId)-1]
                print(f"JACKPOT!!! Selamat, Anda mendapatkan monster {namaMonster}.")
                print("Monster telah ditambahkan ke inventory Anda.")
        else: # jika tidak memenangkan jackpot
            hadiah:int = data[barang1] + data[barang2] + data[barang3] # mendapat OC sesuai jumlah barang
            dataUser["OC"] = str(int(dataUser["OC"]) + hadiah)
            print(f"{hadiah} OC telah ditambahkan ke akun Anda!")
        print(f"Your OC : {dataUser["OC"]}")
        isMain = YesOrNo(input("Bermain lagi (Y/N): "))

def displayJackpot(hasil1:str, hasil2:str, hasil3:str):
    content:str = f"  {hasil1}  |  {hasil2}  |  {hasil3}  "
    side:int = 75 - len(content)
    if side % 2 == 1:
        content += " "
        side -= 1
    side = int(side/2)
    bar:str = "$" * side
    hasil:str = bar + content + bar
    print(
f"""
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
{hasil}
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
""")

# testing sementara
if __name__ == "__main__":
    userId = 3
    dataUser = getDataUser(userId)
    dataMonster = load("monster")
    monsterUser = loadInvent(userId, "monster")
    jackpot(dataUser, dataMonster, monsterUser)