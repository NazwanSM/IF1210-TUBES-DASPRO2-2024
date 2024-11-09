from src.share import arraycsv, search, pilihanValid, clear, index, displayBar
from src.load import loadData, loadInvent

def statMonster(monsterId:int, statIndex:int) -> str:
    data:list[str] = arraycsv("monster")
    hasil:list[str] = search(0, str(monsterId), data)[0]
    return hasil[statIndex] # mengembalikan stat monster yang diinginkan

def get_stats(id:int, level:int) -> dict:
    if level == 1:
        pengaliLevel:int = 1
    else:
        pengaliLevel:int = ((level - 1) * 10 + 100) / 100
    stat:dict = {
        "ID" : id,
        "Name": statMonster(id, 1),
        "Atk": int(int(statMonster(id, 2)) * pengaliLevel),
        "Def": int(int(statMonster(id, 3)) * pengaliLevel),
        "HP": int(int(statMonster(id, 4)) * pengaliLevel),
        "Level": level
    }
    return stat

def monsterList(userId:int, data:dict=None):
    if data is None:
        data:dict = loadInvent(userId, "monster")
    displayBar("MONSTER LIST")
    for [i, element] in enumerate(data["MonsterID"]):
        monsterID:str = element
        levelMonster:int = level(monsterID, data)
        stat:dict = get_stats(monsterID, levelMonster)
        monsterName:str = stat["Name"]
        monsterlist:str = f"{i+1}. {monsterName}"
        space:int = 15 - len(monsterlist)
        print(monsterlist, " " * space + f"(Lvl: {levelMonster})")

def pilihMonster(userId:int, monsterUser:dict, withList:bool=False) -> int:
    maxPilihan:int = len(monsterUser["MonsterID"]) + 1
    if withList:
        monsterList(userId, monsterUser)
    while True:
        pilihan = int(pilihanValid(input("<///> Pilih monster untuk bertarung : "), [f'{i+1}' for i in range(maxPilihan-1)]))
        clear()
        return int(monsterUser["MonsterID"][pilihan-1])

def banyakMonster() -> int:
    return len(loadData("monster")["ID"])

def level(monsterId:int, data:dict) -> int:
    hasil:str = data["Level"][index(str(monsterId), data["MonsterID"])]
    return int(hasil)

# testing
if __name__ == "__main__":
    monsterUser = loadInvent(3, "monster")