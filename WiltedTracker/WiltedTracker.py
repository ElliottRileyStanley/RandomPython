import pyperclip
import requests
import json

key = "b1c19a93-5b5e-43ca-828b-e83a758631f9"

players = json.load(open(r'WiltedTracker\players.json'))

def getCollection(profileID, uuid, key):
    response = requests.get('https://api.hypixel.net/v2/skyblock/profile?profile=' + profileID + '&key=' + key)
    json = response.json()
    return int(json["profile"]["members"][uuid.replace("-", "")]["player_stats"]["rift"]["dreadfarm_wilted_harvested"])

copyString = ""
seperator = " \u0009 "

for player in players:
    amount = getCollection(player["profileID"], player["uuid"], key)
    print(player["name"] + " - " + str(amount))
    copyString = copyString + str(amount) + seperator

pyperclip.copy(copyString)



