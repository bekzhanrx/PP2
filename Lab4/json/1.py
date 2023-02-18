import json

with open("sample-data.json", 'r') as file:
    data = json.load(file)

print("Interface Status")
print("================================================================================")
print("DN                                                 Description           Speed    MTU")
print("-------------------------------------------------- --------------------  ------  ------")
cnt = 0
for item in data["imdata"]:
    if cnt == 3:
        break
    print(item["l1PhysIf"]["attributes"]["dn"], "                            ",
          item["l1PhysIf"]["attributes"]["speed"], " ", item["l1PhysIf"]["attributes"]["mtu"])
    cnt += 1
