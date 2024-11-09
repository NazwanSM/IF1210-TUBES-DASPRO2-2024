from src.share import clear, sleep
from src.rng import random

def peta(lokasi:tuple[int]=(0,0)) -> list[str, tuple[int]]:
    peta:list[str] = drawPeta(lokasi) # memebuat array peta
    while True:
        clear()
        # Menggambarkan peta
        print("* " * 12)
        for row in peta:
            hasil = ""
            for ele in row:
                if ele == "#":
                    hasil += "  "
                else:
                    hasil += " " + ele
            print(f"*{hasil} *")
        print("* " * 12)

        # Menentukan lokasi user
        lokasi:tuple[int] = locate(peta)
        print(f"Your Location : {lokasi}")

        dataPilihan:list[str] = ["I", "M"] # Pilihan aksi yang selalu ada
        setOptionMove(lokasi, dataPilihan) # menambah pilihan aksi mengenai gerak (U, L, R , D)
        surrounding(peta, lokasi, dataPilihan) # menambah pilihan aksi mengenai tempat (S, LA, A ,dll)
        showOption(dataPilihan) # Menampilkan opsi aksi
        while True:
            pilihan = str.upper(input("<///> "))
            if pilihan not in dataPilihan: # saat memilih aksi yang tidak valid
                pilihanSalah(pilihan)
                continue
            break
        if pilihan in ["U", "D", "L", "R"]: # memilih bergerak
            isValidMove = move(peta, pilihan, lokasi)
            if not isValidMove: # saat gerakan tidak valid, menabrak obstacle
                continue
            if isAmbush(): # saat terkena ambush, ada 5 % kemungkinan
                return["AM", lokasi]
            continue
        return [pilihan, lokasi] # Saat memilih memasuki tempat

def isAmbush() -> bool:
    rngAmbush:int = random(numRange=[0,100])
    chance:int = 5
    # menentukan apakah terkena ambush atau tidak, hanya bisa saat berjalan
    return rngAmbush < chance

def drawPeta(lokasi:tuple[int]) -> list[str]:
    (x, y) = lokasi
    data:list[str] = ["##########",
            "####S##X##",
            "#######X##",
            "####J##X#L",
            "####XXXX##",
            "#X########",
            "#X########",
            "#XXX##A###",
            "##########",
            "####XXXXX#"]
    data[x] = data[x][:y] + "P" + data[x][y+1:]
    return data
    
def move(peta:list, arah:str, lokasi:tuple[int]) -> bool:
    (x, y) = lokasi
    if arah == "U":
        if peta[x-1][y] == "#":
            peta[x] = peta[x][:y] + "#" + peta[x][y+1:]
            peta[x-1] = peta[x-1][:y] + "P" + peta[x-1][y+1:]
            return True
        else:
            pilihanSalahArah(peta[x-1][y])
            return False
    elif arah == "D":
        if peta[x+1][y] == "#":
            peta[x] = peta[x][:y] + "#" + peta[x][y+1:]
            peta[x+1] = peta[x+1][:y] + "P" + peta[x+1][y+1:]
            return True
        else:
            pilihanSalahArah(peta[x+1][y])
            return False
    elif arah == "L":
        if peta[x][y-1] == "#":
            peta[x] = peta[x][:y] + "#" + peta[x][y+1:]
            peta[x] = peta[x][:y-1] + "P" + peta[x][y:]
            return True
        else:
            pilihanSalahArah(peta[x][y-1])
            return False
    elif arah == "R":
        if peta[x][y+1] == "#":
            peta[x] = peta[x][:y] + "#" + peta[x][y+1:]
            peta[x] = peta[x][:y+1] + "P" + peta[x][y+2:]
            return True
        else:
            pilihanSalahArah(peta[x][y+1])
            return False

def showOption(options:list[str]):
    hasil:str = ""
    for opsi in options:
        if opsi == "U":
            hasil += "U : Move Up, "
        elif opsi == "D":
            hasil += "D : Move Down, "
        elif opsi == "L":
            hasil += "L : Move Left, "
        elif opsi == "R":
            hasil += "R : Move Right, "
        elif opsi == "B":
            hasil += "B : Enter Battle, "
        elif opsi == "S":
            hasil += "S : Enter Shop, "
        elif opsi == "LA":
            hasil += "LA : Enter Laboratory, "
        elif opsi == "A":
            hasil += "A : Enter Arena, "
        elif opsi == "J":
            hasil += "J : Enter Jackpot, "
        elif opsi == "I":
            hasil += "I : Open Inventory, "
        elif opsi == "M":
            hasil += "M : Open Menu, "
    print(f"({hasil[:-2]})")

def setOptionMove(lokasi:tuple[int], dataPilihan:list):
    if lokasi[0] == 0:
        dataPilihan.append("D")
    elif lokasi[0] == 9:
        dataPilihan.append("U")
    else:
        dataPilihan.append("U")
        dataPilihan.append("D")
    if lokasi[1] == 0:
        dataPilihan.append("R")
    elif lokasi[1] == 9:
        dataPilihan.append("L")
    else:
        dataPilihan.append("R")
        dataPilihan.append("L")

def locate(peta:list[str]) -> tuple[int]:
    for [i, row] in enumerate(peta):
        for [j, ele] in enumerate(row):
            if ele == "P":
                return (i, j)

def pilihanSalah(pilihan:str):
    if pilihan == "U":
        print("You Can't Move Up")
    elif pilihan == "D":
        print("You Can't Move Down")
    elif pilihan == "L":
        print("You Can't Move Left")
    elif pilihan == "R":
        print("You Can't Move Right")
    elif pilihan == "B":
        print("You Can't Enter Battle")
    elif pilihan == "S":
        print("You Can't Enter Shop")
    elif pilihan == "LA":
        print("You Can't Enter Laboratory")
    elif pilihan == "A":
        print("You Can't Enter Arena")
    elif pilihan == "J":
        print("You Can't Enter Jackpot")
    elif pilihan == "I":
        print("You Can't Open Inventory")
    elif pilihan == "M":
        print("You Can't Open Menu")
    else :
        print("Pilihan tidak valid")
    sleep(2)

def pilihanSalahArah(pilihan:str):
    if pilihan == "X":
        print("You Can't Enter a Bush")
    elif pilihan == "S":
        print("Your Head Bump into Shop. To acces it enter the command")
    elif pilihan == "LA":
        print("Your Head Bump into Laboratory. To acces it enter the command")
    elif pilihan == "J":
        print("Your Head Bump into Jackpot. To acces it enter the command")
    elif pilihan == "A":
        print("Your Head Bump into Arena. To acces it enter the command")
    sleep(2)

def surrounding(peta:list, lokasi:tuple[int], dataPilihan:list):
    (x, y) = lokasi
    if x == 0 or x == 9:
        if x == 9:
            up = peta[x-1][y]
            down = "#"
        else:
            up = "#"
            down = peta[x+1][y]
    else:
        up = peta[x-1][y]
        down = peta[x+1][y]
        
    if y == 0 or y == 9:
        if y == 9:
            left = peta[x][y-1]
            rigth = "#"
        else:
            left = "#"
            rigth = peta[x][y+1]
    else:
        left = peta[x][y-1]
        rigth = peta[x][y+1]
    data = [up, down, left, rigth]
    if "X" in data:
        dataPilihan.append("B")
    if "S" in data:
        dataPilihan.append("S")
    if "L" in data:
        dataPilihan.append("LA")
    if "A" in data:
        dataPilihan.append("A")
    if "J" in data:
        dataPilihan.append("J")

# testing sementara
if __name__ == "__main__":
    lokasi = (0,0)
    print(peta(lokasi))