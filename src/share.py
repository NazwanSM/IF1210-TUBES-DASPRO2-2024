import os
import time

def YesOrNo(masukan:str) -> str:
    masukan = str.upper(masukan)
    while True:
        if masukan != "Y" and masukan != "N":
            print("Masukan yang valid hanya Y atau N")
            masukan = str.upper(input("<///> Y/N: "))
        else:
            return masukan == "Y"

def pilihanValid(masukan:str, validRange:list[str]) -> int:
    while True:
        if masukan in validRange:
            return masukan
        else:
            print("Masukan tidak valid")
            masukan = input("<///> Pilih perintah: ")

def isDigit(masukan:str) -> int:
    while True:
        valid:bool = False
        for char in masukan:
            if 48 <= ord(char) <= 57:
                valid = True
            else:
                valid = False
                print("Masukkan input bertipe Integer, coba lagi!")
                masukan = input("<///> Masukan : ")
                break
        if valid:
            return int(masukan)

def display(text:str):
    print(f"""<================================================================>
{text}
<================================================================>""")

def displayBar(text:str):
    content:str = text + " "
    arrow:int = 60 - len(content)
    if arrow % 2 == 1:
        content += " "
        arrow -= 1
    arrow = int(arrow/2)
    bar:str = "<" + "=" * arrow + ">"
    print(bar, content, bar)

def pop_element(shop, index):
    """Menghapus elemen dari shop berdasarkan index"""
    for key in shop:
        del shop[key][index]

def split(baris:str, pemisah:str=None) -> list[str]:
    if pemisah is None:
        pemisah = " "
    hasil:list[str] = []
    temp:str = ""
    for char in baris:
        if char != pemisah:
            temp += char
        else:
            hasil.append(temp)
            temp = ""
    hasil.append(temp[:-1])
    return hasil

def arraycsv(fileName:str) -> list[list[str]]:
    with open(f'data\\{fileName}.csv', 'r') as file:
        hasil:list = []
        for line in file:
            row = list(split(line, ";"))
            hasil.append(row)
        return hasil

def index(element, array:list) -> int:
    for [i, ele] in enumerate(array):
        if ele == element:
            return i

def clear():
    os.system("cls")
    print("...")
    os.system("cls")

def sleep(waktu:int=2):
    time.sleep(waktu)

def search(searchIndex:int, searchInput, file:list) -> list:
    hasil = []
    for row in file:
        if searchInput == row[searchIndex]:
            hasil.append(row)
    return hasil

def maxEle(data:list[int]) -> int:
    if len(data) == 0:
        return 0
    hasil = data[0]
    for i in data:
        if i > hasil:
            hasil = i
    return hasil

def minEle(data:list[int]) -> int:
    if len(data) == 0:
        return 0
    hasil = data[0]
    for i in data:
        if i < hasil:
            hasil = i
    return hasil

# pseudolen
def my_len(arr:list) -> int:
    len:int = 0
    for _ in arr:
        len+=1
    return len 

def find_path(nama_folder:str) -> str:
    path:str = ""
    for (root, dirs, files) in os.walk('.', topdown=True):
        if nama_folder in root:
            path = os.path.join(path, root)
            return path
    return path

# print message bergerak
def loadingmsg(msg:str):
    for _ in range(len(msg)-3, len(msg)+1, 1):
        os.system('cls' if os.name=='nt' else 'clear')
        print (msg)
        msg+="."
        sleep(0.5)

if __name__ == "__main__":
    ...
