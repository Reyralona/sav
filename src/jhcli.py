from jhparser import *

test = parser("src/data.json")

while True:
    os.system('cls')
    option = int(input(
    "[1] = Add Role\n"
    "[2] = Add Entry\n"
    "[3] = Update Entry\n"
    "[4] = Del Role\n" 
    "[5] = Del Entry\n"
    "[6] = Del All Entries\n" 
    "[7] = Clear All\n"
    "[8] = Exit\n"
    "[?] = >> "))

    match option:
        case 1:
            roleName = input("Insert role name >> ")
            if roleName != "":
                test.addRole(roleName)
            else : continue

        case 2:
            roleName = input("Insert role name >> ")
            if roleName != "":
                entryCount = int(input("Insert num of entry elements >> "))
                entry = {}
                if entryCount > 1:
                    for ind in range(entryCount):
                        entryName = input(f"Insert name of element {ind} >> ")
                        entryValue = input(f"Insert value of element {ind} >> ")
                        entry[entryName] = entryValue
                else:
                    entryName = input(f"Insert name of element >> ")
                    entryValue = input(f"Insert value of element >> ")
                    entry[entryName] = entryValue

                test.addEntry(roleName, entry)
            else : continue

        case 3:
            roleName = input("Insert role name >> ")
            if roleName != "":
                elemName = input("Insert an element from the entry to be updated >> ")
                entryCount = int(input("Insert num of entry elements >> "))

                entry = {}
                if entryCount > 1:
                    for ind, each in enumerate(entryCount):
                        entryName = input(f"Insert name of element {ind} >> ")
                        entryValue = input(f"Insert value of element {ind} >> ")
                        entry[entryName] = entryValue
                else:
                    entryName = input(f"Insert name of element >> ")
                    entryValue = input(f"Insert value of element >> ")
                    entry[entryName] = entryValue
                test.updEntry(roleName, test.getEntry(roleName, elemName), entry)
            else : continue

        case 4:
            roleName = input("Insert role name to be deleted >> ")
            if roleName != "":
                test.delRole(roleName)
            else : continue

        case 5:
            roleName = input("Insert role name >> ")
            if roleName != "":
                elemName = input("Insert an element from the entry to be deleted >> ")
                test.delEntry(roleName, test.getEntry(roleName, elemName))
            else : continue

        case 6:
            roleName = input("Insert role name >> ")
            if roleName != "":
                test.delAllEntries(roleName)
            else : continue

        case 7:
            confirmation = input("Clear entire table? Y|N >> ")
            if confirmation != "":
                if str(confirmation).lower() == "y":
                    confirmation = input("Are you sure? This will wipe out everything Y|N >> ")
                    if str(confirmation).lower() == "y":
                        test.clearAll()
                    else : continue
                else: continue
            else : continue
    
        case 8:
            break