import json

def read(file):
    with(open(file, "r") as data):
        content = json.loads(data.read())
        return content 
def write(file, jsonobj):
    with(open(file, "w") as data):  
        data.write(jsonobj)

def addRole(role):
    content = read("data.json")
    if role in content:
        print("Registry alread exists")
    else:
        content[role] = []
        jsonobj = json.dumps(content, indent=3)
        write("data.json", jsonobj)

def delRole(role):
    content = read("data.json")
    if role in content:
        del content[role]
        jsonobj = json.dumps(content, indent=3)
        write("data.json", jsonobj)
    else:
        print("Registry doesn't exist")
    

def addEntry(role, dictionary):
    content = read("data.json")
    students = content[role]
    
    if dictionary in students:
        print("Entry was already registered.")
    else:
        students.append(dictionary)
        jsonobj = json.dumps(content, indent=3)
        write("data.json", jsonobj)

def deleteEntry(role, dictionary):
    content = read("data.json")
    try:
        students = content[role]
    except KeyError:
        print("Registry doesn't exist.")
        return;

    if dictionary in students:
        students.pop(students.index(dictionary))
        jsonobj = json.dumps(content, indent=3)
        write("data.json", jsonobj)
    else:
        print("Entry doesn't exist")

