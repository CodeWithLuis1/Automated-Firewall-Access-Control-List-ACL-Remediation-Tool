import json
txtFile = "allow_list.txt"
jsonFile = "remove_list.json"

def clearTxtFile(dataFile):
    cleanData = []
    with open(dataFile, 'r') as file:
        for documentData in file:
            documentData = documentData.strip()
            if documentData.startswith("#") or documentData == "":
                continue
            cleanData.append(documentData)
        return cleanData

def clearJsonFile(jsonDocuement):
    with open(jsonDocuement, 'r') as file:
        readFile = json.load(file)
        return readFile["compromised_ips"]
    

def remove_compromised_ips(allowList, compromisedIps):
    for ip in compromisedIps:
        if ip in allowList:
            allowList.remove(ip)
    return allowList

def updateAllowList(allowList, dataFile):
    with open(dataFile, 'w') as file:
        file.write("\n".join(allowList))
        
def printAllowList(allowList):
    print("Updated Allow List:")
    for ip in allowList:
        print(ip)
        
        
# Main process. Call and execute the functions to update the allow list.
allowList = clearTxtFile(txtFile)
compromisedIps = clearJsonFile(jsonFile)
deleteCompromisedIps = remove_compromised_ips(allowList,compromisedIps)
updateAllowList(deleteCompromisedIps,txtFile)
printAllowList(deleteCompromisedIps)

