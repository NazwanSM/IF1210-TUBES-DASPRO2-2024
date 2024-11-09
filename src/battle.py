from src.rng import random
from src.share import display, clear, pilihanValid, sleep, displayBar
from src.monster import get_stats, pilihMonster, level, banyakMonster
from src.potion import potionStatus, potionList

def battle(dataUser:dict, potionUser:dict, monsterUser:dict, monsterBall:dict, ambush:bool=False) -> bool:
    clear()
    kondisi:int = 0
    userId:int = dataUser["ID"]
    namaUser:str = dataUser["Username"]
    [statAgent, statMusuh] = encounter(userId, namaUser, monsterUser) # Encounter dengan musuh, dan user memilih monster
    ronde:int = 0
    status:dict = potionStatus(potionUser) # set status potion untuk tracking
    maxHpMusuh:int = statMusuh["HP"]
    maxHpAgent:int = statAgent["HP"]
    levelMusuh:int = statMusuh["Level"]
    clear()
    if ambush: # jika mengalami ambush, musuh akan mengattack sekali di turn 0
        [isEscape, isCatch] = turnEnemy(ronde, statAgent, statMusuh)
        [hasil, kondisi] = check(isEscape, isCatch, statAgent, statMusuh)
    while kondisi == 0:
        ronde += 1
        [isEscape, isCatch] = turnAlly(ronde, monsterUser, monsterBall, statAgent, statMusuh, status, potionUser, maxHpMusuh, maxHpAgent)
        [hasil, kondisi] = check(isEscape, isCatch, statAgent, statMusuh)
        if kondisi != 0: # check kondisi battle
            break
        [isEscape, isCatch] = turnEnemy(ronde, statAgent, statMusuh)
        [hasil, kondisi] = check(isEscape, isCatch, statAgent, statMusuh)
    clear()
    showStat(statMusuh, maxHpMusuh)           
    print("                     VS                           ")
    showStat(statAgent, maxHpAgent)
    if kondisi == 1: # escape
        display("Anda berhasil kabur dari Battle!")
        sleep()
        return hasil
    elif kondisi == 2: # Kalah
        display("Sayang sekali anda kalah")
        print(
r"""        `;-.          ___,
          `.`\_...._/`.-"`
            \        /      ,
            /()   () \    .' `-._
           |)  .    ()\  /   _.'
           \  -'-     ,; '. <
            ;.__     ,;|   > \
           / ,    / ,  |.-'.-'
          (_/    (_/ ,;|.<`
            \    ,     ;-`
             >   \    /
            (_,-'`> .'
                 (_,'""")
        sleep()
        return hasil
    elif kondisi == 3: # Menang
        hadiah:int = random(numRange=[30, 40]) * levelMusuh
        dataUser["OC"] = str(int(dataUser["OC"]) + hadiah)
        display(f"Selamat anda menang, mendapatkan {hadiah} OC !!!")
        print(
r"""                                ___.
                                L._, \\
               _.,             <  <\\                _
             ,' '              `.   | \\            ( `
          ../, `.               |    .\\`.           \\ \\_
         ,' ,..  .           _.,'    ||\\l            )  '\".
        , ,'   \\           ,'.-.`-._,'  |           .  _._`.
      ,' /      \\ \\        `' ' `--/   | \\          / /   ..\\
    .'  /        \\ .         |\\__ - _ ,'` `        / /     `.`.
    |  '          ..         `-...-\"  |  `-'      / /        . `.
    | /           |L__           |    |          / /          `. `.
   , /            .   .          |    |         / /             ` `
  / /          ,. ,`._ `-_       |    |  _   ,-' /               ` \\
 / .           \\\"`_/. `-_ \\_,.  ,'    +-' `-'  _,        ..,-.    \\`.
.  '         .-f    ,'   `    '.       \\__.---'     _   .'   '     \\ \\
' /          `.'    l     .' /          \\..      ,_|/   `.  ,'`     L`
|'      _.-\"\"` `.    \\ _,'  `            \\ `.___`.'\"`-.  , |   |    | \\
||    ,'      `. `.   '       _,...._        `  |    `/ '  |   '     .|
||  ,'          `. ;.,.---' ,'       `.   `.. `-'  .-' /_ .'    ;_   ||
|| '              V      / /           `   | `   ,'   ,' '.    !  `. ||
||/            _,-------7 '              . |  `-'    l         /    `||
. |          ,' .-   ,' ||               | .-.        `.      .'     ||
 `'        ,'    `\".'    |               |    `.        '. -.'       `'
          /      ,'      |               |,'    \\-.._,.'/'
          .     /        .               .       \\    .''
        .`.    |         `.             /         :_,'.'
          \\ `...\\   _     ,'-.        .'         /_.-'
           `-.__ `,  `'   .  _.>----''.  _  __  /
                .'        /\"'          |  \"'   '_
               /_|.-'\\ ,\".             '.'`__'-( \\
                 / ,\"'\"\\,'               `/  `-.|\"""")
        sleep()
        return hasil
    elif kondisi == 4:
        clear()
        sleep()
        return hasil

def encounter(userId:int, namaUser:str, monsterUser:dict) -> list:
    idMusuh:int = random(numRange=[1, banyakMonster()])
    levelMusuh:int = random(numRange=[1,5])
    statMusuh:dict = get_stats(idMusuh, levelMusuh)
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
    showStat(statMusuh)
    monsterId:int = pilihMonster(userId, monsterUser, withList=True)
    levelMonster:int = level(monsterId, monsterUser)
    statAgent:dict = get_stats(monsterId, levelMonster)
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
    print("Entering Battle...")
    sleep(3)
    return [statAgent, statMusuh]

def showStat(stat:dict, maxHp:int=None) -> str:
    if maxHp is None:
        maxHp = stat["HP"]
    display (
f"""Name      : {stat["Name"]}
ATK Power : {stat["Atk"]}
DEF Power : {stat["Def"]}
HP        : {stat["HP"]}/{maxHp}
Level     : {stat["Level"]}""")

def turnAlly(number:int, monsterUser:dict, monsterBall:dict, allies:dict, enemies:dict, status:list, potionUser:dict, maxHpMusuh:int, maxHpAgent:int) -> list[bool]:
    while True:
        clear()
        showStat(enemies, maxHpMusuh)
        print("                                         VS                                         ")
        showStat(allies, maxHpAgent)
        displayBar(f"Turn {number} ({allies["Name"]})")
        print(
f"""1. Attack
2. Use Potion
3. Use Monster Ball
4. Escape""")
        pilihan =int(pilihanValid(input("<///> Pilih perintah: "), ["1", "2", "3", "4"])) # pilihan aksi
        if pilihan == 1: # attack
            attack(allies["Atk"], enemies["Def"], allies["Name"], enemies["Name"], enemies)
            return [False, False]
        elif pilihan == 2: # Menggunakan potion
            maxPilihan:int = potionList(potionUser)
            isCancel:bool = usePotion(status, potionUser, maxPilihan, allies, maxHpAgent)
            if isCancel:
                continue
            return [False, False]
        elif pilihan == 3: # menggunakan monster ball
            isCatch:bool = catch(enemies, monsterUser, monsterBall)
            sleep(3)
            if isCatch:
                return [False, True] 
        else: # escape
            return [True, False]

def turnEnemy(number:int, allies:dict, enemies:dict) -> list[bool]:
    displayBar(f"Turn {number} ({enemies["Name"]})")
    attack(enemies["Atk"], allies["Def"], enemies["Name"], allies["Name"], allies)
    clear()
    return[False, False]

def catch(enemies:dict, monsterUser:dict, monsterBall:dict):
    levelMonster:int = enemies["Level"]
    namaMonster:str = enemies["Name"]
    monsterId = str(enemies["ID"])
    while True:
        if monsterBall["Ball"] == 0:
            print("Anda tidak memiliki Monster Ball dalam inventory!")
            return False
        elif monsterId in monsterUser["MonsterID"]:
            print(f"Anda sudah memiliki monster {namaMonster} dalam inventory!")
            return False
        else :
            isCatch:bool = randomCatch(levelMonster)
            monsterBall["Ball"] -= 1
            if isCatch:
                print(f"{namaMonster} Berhasil diitangkap !!! ")
                monsterUser["MonsterID"].append(monsterId)
                monsterUser["Level"].append(str(levelMonster))
                stat = get_stats(monsterId, levelMonster)
                showStat(stat)
                print(f"Sisa Monster Ball Anda : {monsterBall["Ball"]}")
                return True
            else:
                print(f"Yah anda belum berhasil mendapatkan monster {namaMonster} !!! ")
                print(f"Sisa Monster Ball Anda : {monsterBall["Ball"]}")
                return False
            
def randomCatch(levelMonster:int) -> bool:
    number:int = random(numRange=[0,100])
    data:dict[int] = {
        "1": 75,
        "2": 50,
        "3": 25,
        "4": 10,
        "5": 5
    }
    chance:int = data[str(levelMonster)]
    return number < chance # menentukan apakah tertangkap atau tidak
    
def attack(Atk:int, Def:int, attackerName:str, defenderName:str, defender:list):
    lowATK = int(Atk * 7/10)
    highATK = int(Atk * 13/10)
    rngATK:int = random(numRange=[lowATK, highATK])
    DEF:int = rngATK * (Def/100)
    damage = int(rngATK - DEF)
    print(f"{attackerName} attack {defenderName} dealing {damage} damage !!!")
    defender["HP"] -= damage
    if defender["HP"] < 0:
        defender["HP"] = 0
    sleep(3)

def usePotion(status:list, potionUser:dict, maxPilihan:int, allies:dict, maxHp:int) -> bool:
    while True:
        pilihan = int(pilihanValid(input("<///> Pilih potion: "), [str(i+1) for i in range(maxPilihan)]))
        if pilihan-1 == len(status):
            clear()
            return True
        typePotion:str = [potion for potion in potionUser][pilihan-1]
        quantity = int(potionUser[typePotion])
        if quantity == 0:
            print(f"{typePotion} potion sudah habis")
        elif status[typePotion] == "1":
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
            status[typePotion] = str(1)
            sleep(2)
            return False

def check(isEscape:bool, isCatch:bool, agent:dict, musuh:dict) -> list[bool, int]:
    if isEscape:
        return [False, 1]
    elif isCatch:
        return [True, 4]
    elif agent["HP"] == 0:
        return [False, 2]
    elif musuh["HP"] == 0:
        return [True, 3]
    else:
        return [False, 0]

# testing sementara
if __name__ == "__main__":
    ...