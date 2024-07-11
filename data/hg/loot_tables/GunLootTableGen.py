import openpyxl
import json
import numpy as np

path = "minecraft_loot.xlsx"

ws = openpyxl.load_workbook(path).active

ammos = []
dic_gun = {}

def generateWeight(weight):
    match weight:
        case 1:
            return 10000
        case 2: 
            return 500
        case 3:
            return 8
        case 4: 
            return 3
        case 5:
            return 1

def grabAmmo():
    for row in ws.iter_rows():
        if row[1].value not in ammos and row[1].value != "ammo":
            ammos.append(row[1].value) 
            dic_gun[row[1].value] = {
                "guns": []
            }
        if row[1].value != "ammo":
            dic_gun[row[1].value]["guns"].append({'name': row[0].value, 'rarity': generateWeight(row[2].value)})

# {
# "9mm":
# {"guns": [{"name": gun, "rarity":1}]}
# }
# 10-rarity/10 

grabAmmo()
# print(dic_gun)



def populateTable():
    for ammo in dic_gun:
        f = open('baseJsonTemplate.json')
        data = json.load(f)
        data["pools"][0]["entries"][0]["name"] = data["pools"][0]["entries"][0]["name"]+ammo
        for gun in dic_gun[ammo]["guns"]:
            data["pools"][1]["entries"].append({
                "type": "minecraft:item",
                "name": "tac:"+gun['name'],
                "weight": gun['rarity']
            })
        with open('loot/'+ammo+'.json', 'w') as wf:
            json.dump(data, wf)


populateTable()

def generateAvgRarity(guns):
    guns = guns['guns']  # Extract the list of guns from the dictionary

    total_rarity = sum(int(gun['rarity']) for gun in guns)
    average_rarity = total_rarity / len(guns)
    print(f'Average rarity: {int(average_rarity)}')
    return int(average_rarity)

def populateMainLoot():
    f = open('loot_table.json')
    data = json.load(f)
    for ammo in dic_gun:
        data["pools"][0]["entries"].append(
        {
          "type": "minecraft:loot_table",
          "name": "hg:loot/"+ammo,
          "weight": generateAvgRarity(dic_gun[ammo])
        })
    with open("loot_table.json", 'w') as wf:
        json.dump(data, wf)

populateMainLoot()