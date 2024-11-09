from src.load import loadInvent
from src.share import displayBar, pop_element

def getPotion(userId:int) -> dict:
    potionUser = loadInvent(userId, "potion")
    data = {}
    for [i ,potion] in enumerate(potionUser["Type"]):
        quantityPotion = int(potionUser["Quantity"][i])
        if quantityPotion > 0:
            data[potion] = str(quantityPotion)
    return data

def potionStatus(potionUser:dict) -> dict:
    status = {}
    for potion in potionUser:
        status[potion] = 0
    return status

def tambahPotion(type:str, quanntity:int, dataPotion:dict) -> dict:
    dataPotion[type] += quanntity
    return dataPotion

def potionList(potionUser:dict) -> int:
    displayBar("POTION LIST")
    for [i, potion] in enumerate(potionUser):
        space = 12 - len(potion)
        print(f"{i+1}. {potion} Potion" + space * " " + f"(Qty: {potionUser[potion]})", end="")
        if potion == "Strength":
            print(" - Increase ATK Power")
        elif potion == "Resilience":
            print(" - Increase DEF Power")
        elif potion == "Healing":
            print(" - Restore Health")
        else: 
            print()
    max = len(potionUser) + 1
    print(f"{max}. Cancel")
    return max

def updatePotionUser(potionUser:dict, potionInvent:dict):
    temp = {}
    for [i, typePotion] in enumerate(potionInvent["Type"]):
        quantityPotion = int(potionInvent["Quantity"][i])
        if quantityPotion > 0:
            temp[typePotion] = str(quantityPotion)
        if typePotion in potionUser:
            if potionUser[typePotion] == "0":
                del potionUser[typePotion]
    for typePotion in temp:
        potionUser[typePotion] = temp[typePotion]


def updatePotionInvent(potionUser:dict, potionInvent:dict):
    for [i, typePotion] in enumerate(potionInvent["Type"]):
        if typePotion in potionUser:
            quantityPotion = potionUser[typePotion]
        else:
            quantityPotion = 0
        potionInvent["Quantity"][i] = str(quantityPotion)
if __name__ == "__main__":
    potionUser = getPotion(3)
    # print(potionUser)
    # potionList(potionUser)
    # print(potionStatus(potionUser))
