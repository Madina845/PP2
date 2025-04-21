import json

with open("sample-data.json", "r") as f:
    data = json.load(f)

print("Interface Status")
print("=" * 80)
header_format = "{:<50} {:<20} {:<8} {:<6}"
print(header_format.format("DN", "Description", "Speed", "MTU"))
print(header_format.format("-" * 50, "-" * 20, "-" * 8, "-" * 6))

for item in data["imdata"]:
    attributes = item["l1PhysIf"]["attributes"]
    dn = attributes["dn"]
    description = attributes.get("descr", "")
    speed = attributes["speed"]
    mtu = attributes["mtu"]
    print(header_format.format(dn, description, speed, mtu))
