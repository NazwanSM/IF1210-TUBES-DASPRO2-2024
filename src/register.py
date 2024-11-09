from src.share import sleep

allowed_characters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_-"

def concatenate_list(lst, delimiter):
    result = ''
    for item in lst:
        result += str(item) + delimiter
    return result

def append_to_row(row, item):
    if isinstance(item, list):
        for i in range(len(item)):
            row.append(item[i])
    else:
        row.append(item)

def write_to_csv(csvFile, data):
    with open(csvFile, mode='a', newline='') as file:
        row = ''
        for item in data:
            row += str(item) + ';'
        row = row[:-1] + '\n'
        file.write(row)

def check_valid_input(username, csvFile):
    # Check the characters used in a username
    for char in username:
        if char not in allowed_characters:
            print("\nUsername hanya boleh berisi alfabet, angka, underscore, dan strip!")
            return False
    
    # Check if the username is already in the CSV file
    with open(csvFile, mode='r') as file:
        for line in file:
            row = []
            is_name = False
            for char in line:
                if char == ';':
                    if is_name:
                        break
                    is_name = True
                elif is_name:
                    append_to_row(row, [char])
            if username == concatenate_list(row, ''):  
                print("\nUsername " + username +  " sudah terpakai, silahkan gunakan username lain!")
                return False
    
    return True

def register_manager():
    # CSV file paths
    userFile = r'data\user.csv'
    monsterFile = r'data\monster.csv'
    while True:
    # Input name and password
        inputName = input("Masukkan nama: ")
        inputPass = input("Masukkan password: ")

        # Validate username input
        if not check_valid_input(inputName, userFile):
            sleep(2)
            continue

        # Get the last ID number
        lastID = 0
        with open(userFile, mode='r') as file:
            next(file)  
            for line in file:
                row = []
                for char in line:
                    if char == ';':
                        break
                    append_to_row(row, [char])
                lastID = max(lastID, int(concatenate_list(row, '')))

        # Generate new user ID
        inputID = str(lastID + 1)
        monInPlayerID = inputID

        # Set default values for role and coin
        inputRole = 'agent'
        inputCoin = '0'

        # Read available monster types from monster.csv
        monster_types = []
        with open(monsterFile, mode='r') as file:
            next(file) 
            for line in file:
                row = []
                is_name = False
                for char in line:
                    if char == ';':
                        if is_name:
                            break
                        is_name = True
                    elif is_name:
                        append_to_row(row, [char])
                monster_types.append(concatenate_list(row, ''))
        break
    while True:
        print("\nSilahkan pilih salah satu monster sebagai monster awalmu.")
        for i, monster_type in enumerate(monster_types, start=1):
            print(f"{i}. {monster_type}")

        # Input monster type
        x = int(input("\nMonster pilihanmu: "))
        if x <= 0 or x > len(monster_types):
            print("\nPilihan monster tidak valid.")
            sleep(2)
            continue
        
        monInMonsterID = x
        monInLevelID = 1

        inputMonster = monster_types[x - 1]

        print(f"\nSelamat datang Agent {inputName}. Mari kita mengalahkan Dr. Asep Spakbor dengan {inputMonster}!")
        sleep(2)
        userData = [inputID, inputName, inputPass, inputRole, inputCoin]
        monInventoryData = [monInPlayerID, monInMonsterID, monInLevelID]
        for potion in ["Healing", "Strength", "Resilience"]:
            potionData = [inputID, potion, "0"]
            write_to_csv(r"data\item_inventory.csv", potionData)
        write_to_csv(r"data\monster_inventory.csv", monInventoryData)
        
        if (userData != []):
            write_to_csv(r"data\user.csv", userData)
        return userData