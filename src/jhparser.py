import json

class parser:
    def __init__(self, file):
        self.file = file
        
    def read(self):
        with(open(self.file, "r") as data):
            content = json.loads(data.read())
            return content 
        
    def write(self, jsonobj):
        with(open(self.file, "w") as data):  
            data.write(jsonobj)

    def clearAll(self):
        with (open(self.file, "w") as data):
            data.write("{}")

    def addRole(self, role):
        content = self.read()
        if role in content:
            print("Registry alread exists")
        else:
            content[role] = []
            jsonobj = json.dumps(content, indent=3)
            self.write(jsonobj)

    def delRole(self, role):
        content = self.read()
        if role in content:
            del content[role]
            jsonobj = json.dumps(content, indent=3)
            self.write(jsonobj)
        else:
            print("Registry doesn't exist")

    def addEntry(self, role, dictionary):
        content = self.read()
        students = content[role]
        if dictionary in students:
            print("Entry was already registered.")
        else:
            students.append(dictionary)
            jsonobj = json.dumps(content, indent=3)
            self.write(jsonobj)

    def updEntry(self, role, oldDict, newDict):
        content = self.read()
        
        if oldDict not in content[role]:
            print("Not found")
            return
       
        for each in content[role]:
            if each == oldDict:
                ind = content[role].index(each)
                content[role][ind] = newDict
    
        jsonobj = json.dumps(content, indent=3)
        self.write(jsonobj)
        

    def delEntry(self, role, dictionary):
        content = self.read()
        try:
            students = content[role]
        except KeyError:
            print("Registry doesn't exist.")
            return;
        if dictionary in students:
            students.pop(students.index(dictionary))
            jsonobj = json.dumps(content, indent=3)
            self.write(jsonobj)
        else:
            print("Entry doesn't exist")

    def delAllEntries(self, role):
        content = self.read()
        content[role] = []
        jsonobj = json.dumps(content, indent=3)
        self.write(jsonobj)

test = parser("src/data.json")