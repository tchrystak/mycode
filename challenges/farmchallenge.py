#!/user/bin/ env python3
farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

NE_animals= farms[0]["agriculture"]

for x in NE_animals:
     print(x)



NE_farm = farms[0]["agriculture"]
W_farm = farms[1]["agriculture"]
SE_farm = farms[2]["agriculture"][0]

choice = input("Choose a farm (NE Farm, W Farm, or SE Farm)\n")

if choice == "NE Farm":
    print(NE_farm)
if choice == "W Farm":
    print(W_farm)
if choice == "SE Farm":
    print(SE_farm)
