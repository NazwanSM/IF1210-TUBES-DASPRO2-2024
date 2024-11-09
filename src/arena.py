from src.battle import pilihMonster, showStat, banyakMonster
from src.potion import getPotion, potionStatus, potionList
from src.load import load, loadInvent, showDict
from src.monster import level, get_stats
from src.share import display, sleep, clear, pilihanValid, displayBar, maxEle, minEle
from src.rng import random

def arena(dataUser:dict, potionUser:dict, monsterUser:dict):
    clear()
    statDasar = enterArena(dataUser, monsterUser) #Mengambil stat dasar monster user
    statAgent:dict = {}
    for data in statDasar: # Mengcopy data statDasar ke statAgent
        statAgent[data] = statDasar[data]
    hasilLatihan = { # Penyimpanan data hasil latihan
        "Total Hadiah": 0,
        "Jumlah Stage": 0,
        "Damage diberikan": 0,
        "Damage diterima": 0,
        "Potion digunakan": 0,
        "Total turn": 0,
        "Battle terlama": 0,
        "Battle tersingkat": 0
    }
    dataRonde:list[int] = [] # Penyimpanan data turn yang dipakai tiap stage
    dataPotion = potionStatus(potionUser) # Penyimpanan data potion yang dipakai dalam pertempuran
    maxHpAgent:int = statDasar["HP"]
    for i in range(1,6): # loop 5 kali untuk 5 stage
        print(f"Memasuki Ronde {i}...")
        sleep()
        statAgent["Def"] = statDasar["Def"] # Meneysuaikan def kembali ke statDasar, menghilangkan efek potion resilience
        statAgent["Atk"] = statDasar["Atk"] # Meneysuaikan def kembali ke statDasar, menghilangkan efek potion strength
        [isMenang, kondisi] = battleArena(potionUser, statAgent, i, hasilLatihan, dataRonde, dataPotion, dataUser, maxHpAgent) #Dilakukan battle
        # Mengecek apakah menang atau tidak
        if isMenang:
            continue
        else:
            break
    hasilPotion:int = 0
    for typePotion in dataPotion: # menghitung jumlah total potion digunakan
        hasilPotion += dataPotion[typePotion]
    # Memasukkan data ke data hasil latihan
    hasilLatihan["Potion digunakan"] = hasilPotion
    hasilLatihan["Battle terlama"] = maxEle(dataRonde)
    hasilLatihan["Battle tersingkat"] = minEle(dataRonde)

    # Kondisi saat menyelesaikan arena
    if kondisi == 1:
        display("GAME OVER !, Anda mengakhiri battle")
        showDict(hasilLatihan)
    elif kondisi == 2:
        display("GAME OVER !, Anda kalah")
        showDict(hasilLatihan)
    elif kondisi == 3:
        display("CONGRATS !, Anda Menang ")
        showDict(hasilLatihan)
    sleep(3)

def enterArena(dataUser:dict, monsterUser:dict) -> dict: # Dipanggil saat memasuki arena pertama kali
    namaUser:str = dataUser["Username"]
    userId:int = dataUser["ID"]
    display("Selamat datang di Arena !!! ")
    monsterId = pilihMonster(userId, monsterUser, withList=True) # memilih monster yang digunakan
    levelMonster = level(monsterId, monsterUser)
    statAgent = get_stats(monsterId, levelMonster)
    print(
r"""
  _,-""`""-~`)
(`~_,=========\
 |---,___.-.__,\
 |        o     \ ___  _,,,,_     _.--.
  \      `^`    /`_.-"~      `~-;`     \
   \_      _  .'                 `,     |
     |`-                           \'__/ 
    /                      ,_       \  `'-. 
   /    .-""~~--.            `"-,   ;_    /
  |              \               \  | `""`
   \__.--'`"-.   /_               |'
              `"`  `~~~---..,     |
                             \ _.-'`-.
                              \       \
                               '.     /
                                 `"~"`""")
    print(f"RAWRR, Agent {namaUser} mengeluarkan monster {statAgent["Name"]} !!!")
    showStat(statAgent)
    return statAgent

def battleArena(potionUser:dict, statAgent:dict, arena:int,  hasilLatihan:dict, dataRonde:list, dataPotion:dict, dataUser:dict, maxHpAgent:int) -> bool:
    clear()
    dataHadiah:list[int] = [30, 50, 100, 200, 400] # data hadiah OC tiap stage, hardcode
    kondisi:int = 0
    idMusuh:int = random(numRange=[1, banyakMonster()])
    levelMusuh:int = arena
    statMusuh = get_stats(idMusuh, levelMusuh)
    print(
r"""           _.------.                        .----.__
           /         \_.       ._           /---.__  \
          |  O    O   |\\___  //|          /       `\ |
          |  .vvvvv.  | )   `(/ |         | o     o  \|
          /  |     |  |/      \ |  /|   ./| .vvvvv.  |\
         /   `^^^^^'  / _   _  `|_ ||  / /| |     |  | \
       ./  /|         | O)  O   ) \|| //' | `^vvvv'  |/\\
      /   / |         \        /  | | ~   \          |  \\
      \  /  |        / \ Y   /'   | \     |          |   ~
       `'   |  _     |  `._/' |   |  \     7        /
         _.-'-' `-'-'|  |`-._/   /    \ _ /    .    |
    __.-'            \  \   .   / \_.  \ -|_/\/ `--.|_
 --'                  \  \ |   /    |  |              `-
                       \uU \UU/     |  /   :F_P:""")
    print(f"RAWRR, Monster {statMusuh["Name"]} telah muncul !!!") 
    sleep()
    ronde:int = 0
    status:dict = potionStatus(potionUser) # Membuat dictionary untuk mentrack potion mana yang sudah dipakai
    maxHpMusuh:int = statMusuh["HP"]
    clear()
    while kondisi == 0:
        ronde += 1
        isEscape = turnArena(hasilLatihan, dataPotion, ronde, statAgent, statMusuh, status, potionUser, maxHpMusuh, maxHpAgent)
        [hasil, kondisi] = check(isEscape, statAgent, statMusuh) # check hasil battle
        if kondisi != 0:
            break
        turnMusuhArena(hasilLatihan, ronde, statAgent, statMusuh)
        [hasil, kondisi] = check(isEscape, statAgent, statMusuh) # check hasil battle
    clear()
    if kondisi == 3: # Jika menang
        hadiah = dataHadiah[arena-1]
        hasilLatihan["Total Hadiah"] += hadiah
        hasilLatihan["Total turn"] += ronde
        hasilLatihan["Jumlah Stage"] = arena
        dataRonde.append(ronde)
        dataUser["OC"] = str(int(dataUser["OC"]) + hadiah)
        display(f"Selamat anda telah menyelesaikan ronde {arena}, mendapatkan {hadiah} OC !!!")
    sleep()
    return [hasil, kondisi]

def turnArena(hasilLatihan:dict, dataPotion:dict, number:int, allies:dict, enemies:dict, status:list, potionUser:dict, maxHpMusuh:int, maxHpAgent:int) -> bool:
    while True:
        clear()
        # Menampilkan stat
        showStat(enemies, maxHpMusuh)
        print("                    VS                           ")
        showStat(allies, maxHpAgent)
        displayBar(f"Turn {number} ({allies["Name"]})")
        print(
f"""1. Attack
2. Use Potion
3. Escape""")
        pilihan = int(pilihanValid(input("<///> Pilih perintah: "), ["1", "2", "3"])) # Memilih aksi
        if pilihan == 1: # Attack
            dmg = attackArena(allies["Atk"], enemies["Def"], allies["Name"], enemies["Name"], enemies)
            hasilLatihan["Damage diberikan"] += dmg
            return False
        elif pilihan == 2: # Menggunakan potion
            maxPilihan = potionList(potionUser)
            isCancel = usePotionArena(status, dataPotion, potionUser, maxPilihan, allies, maxHpAgent)
            if isCancel:
                continue
            return False
        else: # Escape
            return True

def turnMusuhArena(hasilLatihan:dict, number:int, allies:dict, enemies:dict):
    displayBar(f"Turn {number} ({enemies["Name"]})")
    dmg = attackArena(enemies["Atk"], allies["Def"], enemies["Name"], allies["Name"], allies)
    hasilLatihan["Damage diterima"] += dmg
    clear()

def attackArena(Atk:int, Def:int, attackerName:str, defenderName:str, defender:dict) -> int:
    lowATK = int(Atk * 7/10)
    highATK = int(Atk * 13/10)
    rngATK:int = random(numRange=[lowATK, highATK])
    DEF:int = rngATK * (Def/100)
    damage = int(rngATK - DEF) # ATk dikurangi dengan def% menghasilkan damage sebenarnya
    print(f"{attackerName} attack {defenderName} dealing {damage} damage !!!")
    defender["HP"] -= damage
    if defender["HP"] < 0: # Jika hp dibawah 0 akan di set ke 0
        defender["HP"] = 0
    sleep()
    return damage

def usePotionArena(status:list, dataPotion:dict, potionUser:dict, maxPilihan:int, allies:dict, maxHp:int) -> bool:
    while True:
        pilihan = int(pilihanValid(input("<///> Pilih potion: "), [str(i+1) for i in range(maxPilihan)])) # Memilih type potion
        if pilihan-1 == len(status): # jika memilih cancel
            clear()
            return True
        typePotion:str = [potion for potion in potionUser][pilihan-1]
        quantity = int(potionUser[typePotion])
        if quantity == 0: # jika quantity potion 0
            print(f"{typePotion} potion sudah habis")
        elif status[typePotion] == "1": # jika potion sudah digunakan
            print("sudah digunakan")
        else:
            print(f"{typePotion} potion digunakan")
            quantity -= 1
            potionUser[typePotion] = str(quantity)
            if typePotion == "Strength":
                allies["Atk"] += int(5 / 100 * allies["Atk"])
            elif typePotion == "Resilience":
                allies["Def"] += int(5 / 100 * allies["Def"])
            elif typePotion == "Healing":
                allies["HP"] += int(25 / 100 * maxHp)
                if allies["HP"] > maxHp:
                    allies["HP"] = maxHp
            status[typePotion] = str(1) # mengeset status potion ke sudah digunakan
            dataPotion[typePotion] += 1 # menambahkan hitungan ke potion yang digunakan
            sleep()
            return False

def check(isEscape:bool, agent:dict, musuh:dict) -> list[bool, int]:
    if isEscape: # escape
        return [False, 1]
    elif agent["HP"] == 0: # jika agent kalah
        return [False, 2]
    elif musuh["HP"] == 0: # jika musuh kalah
        return [True, 3]
    else: # battle berlanjut
        return [False, 0]

# testing sementara
if __name__ == "__main__":
    userId = 3
    potionUser = getPotion(userId)
    dataUser = load("user", userId)
    monsterUser = loadInvent(userId, "monster")
    arena(dataUser, potionUser, monsterUser)